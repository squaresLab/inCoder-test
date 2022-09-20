from typing import List

import json
import os
import torch
torch.cuda.empty_cache()

from math import exp, log
torch.set_printoptions(precision=15)

import tokenizers
from math import log2
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
tokenizers_version = tuple(int(n) for n in tokenizers.__version__.split('.'))
if tokenizers_version < (0, 12, 1):
    print("warning: Your tokenizers version looks old and you will likely have formatting issues. We recommend installing tokenizers >= 0.12.1")

# set BIG_MODEL to use the 6.7B parameter model
BIG_MODEL = False

# use a GPU
CUDA = True

# print intermediate outputs of infilling
VERBOSE = True

if BIG_MODEL:
    model_name = "facebook/incoder-6B"

    # the arguments added below will load a half precision version of the model,
    # which requires less RAM than loading the full float32 version.  this 
    # should fit in ~16GB of RAM
    # NOTE: half precision should *not* be used if you plan to fine-tune the
    # model. You'll need full precision and a lot of GPU memory. We have not
    # tested fine-tuning in `transformers` (the model was trained in fairseq)
    if CUDA:
        kwargs = dict(
            revision="float16", 
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
        )
    else:
        kwargs = dict(
            low_cpu_mem_usage=True,
        )
else:
    model_name = "facebook/incoder-1B"
    kwargs = {}

print("loading model")
model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
print("loading tokenizer")
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("loading complete")

if CUDA:
    # if you plan to fine-tune the model, you should not use half precision.
    model = model.half().cuda()

# signals the start of a document
BOS = "<|endoftext|>"
# signals the end of a generated infill
EOM = "<|endofmask|>"

def make_sentinel(i):
    # signals (1) a location to insert an infill and (2) the start of the infill generation
    return f"<|mask:{i}|>"

def generate(input: str, max_to_generate: int=128, temperature: float=0.2):
    """
    Do standard left-to-right completion of the prefix `input` by sampling from the model
    """
    input_ids = tokenizer(input, return_tensors="pt").input_ids
    if CUDA:
        input_ids = input_ids.cuda()
    max_length = max_to_generate + input_ids.flatten().size(0)
    if max_length > 2048:
        print("warning: max_length {} is greater than the context window {}".format(max_length, 2048))
    with torch.no_grad():
        output = model.generate(input_ids=input_ids, do_sample=True, top_p=0.95, temperature=temperature, max_length=max_length, return_dict_in_generate=True, output_scores=True)
        #print(output["sequences"].shape)
        #print(output["scores"][0].shape)
        #print(len(output["scores"]))

        #logprobs = output["scores"][0]
        #print(logprobs.shape)

        #generated_ids = output["sequences"][0, input_ids.size(1):]
        #vocab_size = output["scores"][0].shape[-1]

        #print(generated_ids)
        #print(vocab_size)

        #logprob_gen_token0 = torch.softmax(output["scores"][0], dim=-1)[0, generated_ids[0]]
        #print(logprob_gen_token0)

        #logprobs0 = torch.softmax(output["scores"][0], dim=-1)
        #logprobs1 = torch.softmax(output["scores"][1], dim=-1)
        #print(logprobs0.sum())
        #print(logprobs1.sum())
        #print(logprobs0[0, generated_ids[0]])
        #print(logprobs1[0, generated_ids[1]])

        #probs = []
        #for i in range(0, len(generated_ids)):
            #log_prob = torch.log_softmax(output["scores"][i], dim=-1)[0, generated_ids[i]]
            ##log_prob = torch.log(token_prob[0, generated_ids[i]])
            #probs.append(log_prob)
        #print(probs)



    # pass clean_up_tokenization_spaces=False to avoid removing spaces before punctuation, e.g. "from ." -> "from."
    detok_hypo_str = tokenizer.decode(output["sequences"].flatten(), clean_up_tokenization_spaces=False)
    if detok_hypo_str.startswith(BOS):
        detok_hypo_str = detok_hypo_str[len(BOS):]
    return detok_hypo_str

def infill(parts: List[str], max_to_generate: int=128, temperature: float=0.2, extra_sentinel: bool=True, max_retries: int=1):
    """
    Generate infills to complete a partial document, e.g.
    [A C E] -> [A B C D E], where B and D are infills that have been generated.
    parts: List[str]. list of parts of the document. One string will be
            inserted in between each element, i.e. infilling N-1 locations for a list
            of length N.
    max_to_generate: int. maximum number of tokens to generate. Keep in mind
            that the model context size is 2048.
    temperature: float. temperature parameter for sampling.
    extra_sentinel: bool. we recommend setting this to True, as it makes it
            easier for the model to end generated infills. See the footnote in 
            section 2.2 of our paper for details.
    max_retries: int. if > 1, use rejection sampling to keep sampling infills until
            all infills sample a completion token.
    returns a dictionary containing the following:
        text:  str, the completed document (with infills inserted)
        parts:  List[str], length N. Same as passed to the method
        infills:  List[str], length N-1. The list of infills generated
        retries_attempted:  number of retries used (if max_retries > 1)
    """
    assert isinstance(parts, list)
    retries_attempted = 0
    done = False

    while (not done) and (retries_attempted < max_retries):
        retries_attempted += 1

        if VERBOSE:
            print(f"retry {retries_attempted}")
        
        ## (1) build the prompt
        if len(parts) == 1:
            prompt = parts[0]
        else:
            prompt = ""
            # encode parts separated by sentinel
            for sentinel_ix, part in enumerate(parts):
                prompt += part
                if extra_sentinel or (sentinel_ix < len(parts) - 1):
                    prompt += make_sentinel(sentinel_ix)
        
        infills = []
        complete = []

        done = True

        ## (2) generate infills
        for sentinel_ix, part in enumerate(parts[:-1]):
            complete.append(part)
            prompt += make_sentinel(sentinel_ix)
            # TODO: this is inefficient as it requires re-encoding prefixes repeatedly
            completion = generate(prompt, max_to_generate, temperature)
            completion = completion[len(prompt):]
            if EOM not in completion:
                if VERBOSE:
                    print(f"warning: {EOM} not found")
                completion += EOM
                done = False
            completion = completion[:completion.index(EOM) + len(EOM)]
            infilled = completion[:-len(EOM)]
            infills.append(infilled)
            complete.append(infilled)
            prompt += completion
        complete.append(parts[-1])
        text = ''.join(complete)

    if VERBOSE:
        print("generated text:")
        print(prompt)
        print()
        print("parts:")
        print(parts)
        print()
        print("infills:")
        print(infills)
        print()
        print("restitched text:")
        print(text)
        print()
    
    return {
        'text': text, # str, the completed document (with infills inserted)
        'parts': parts, # List[str], length N. Same as passed to the method
        'infills': infills, # List[str], length N-1. The list of infills generated
        'retries_attempted': retries_attempted, # number of retries used (if max_retries > 1)
    } 

def infill_code(code, max_to_generate=128, temperature=0.2):
    # this will sometimes generate extra functions! this can be avoided by truncating generation when e.g. a """ is produced
    parts = code.split("<insert>")
    result = infill(parts, max_to_generate=max_to_generate, temperature=temperature)
    #print("completed document:")
    #print(result["text"])
    return result

def make_dir(path):
    if os.path.exists(path):
        os.system("rm -r " + path)
    os.mkdir(path)

def get_programs(path):
    """Return a list of programs in the given path"""
    prog_paths = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            prog_paths.append(os.path.join(path, file))
    return prog_paths

if __name__ == "__main__":

    make_dir('data/bug_drop_infill')
    make_dir('data/random_drop_infill')

    path = "data/bug_drop"
    prog_paths = get_programs(path)

    for prog_path in prog_paths:
        prog_name = prog_path.split('/')[-1].split('.')[0]
        with open(prog_path, 'r') as f1:
            code = f1.read()
            result = infill_code(code)
            with open('data/bug_drop_infill/' + prog_path.split('/')[-1], 'w') as f2:
                json.dump(result, f2)
    
    path = "data/random_drop"
    prog_paths = get_programs(path)

    for prog_path in prog_paths:
        prog_name = prog_path.split('/')[-1].split('.')[0]
        with open(prog_path, 'r') as f1:
            code = f1.read()
            result = infill_code(code)
            with open('data/random_drop_infill/' + prog_path.split('/')[-1], 'w') as f2:
                json.dump(result, f2)

    #code = '''\
    #def bitcount(n):
    #count = 0
    #while n:
    #    <insert>
    #    count += 1
    #return count'''
    #result = infill_code(code)
    #print(result)