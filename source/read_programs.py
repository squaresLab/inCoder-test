import os 
import sys
import json 

def get_programs(path):
    """Return a list of programs in the given path"""
    prog_paths = []
    for file in os.listdir(path):
        if "_test" in file or file == 'node.py':
            continue
        if file.endswith(".py"):
            prog_paths.append(os.path.join(path, file))
    return prog_paths

def trim_program(prog_path):
    """Trim the given program to only include the code"""
    with open(prog_path, "r") as f:
        lines = f.readlines()
    code = []
    for line in lines:
        if '"""' in line:
            break 
        code.append(line)
    return code

def remove_first_line(code):
    if code[0].startswith("#"):
        code = code[1:]
    elif code[0] == "\n":
        code = code[1:]
    return code

def main():
    path = "data/python_programs"
    prog_paths = get_programs(path)
    if not os.path.exists("data/trimmed_programs"):
        os.mkdir("data/trimmed_programs")
    for prog_path in prog_paths:
        code = trim_program(prog_path)
        code = remove_first_line(code)
        with open("data/trimmed_programs/" + prog_path.split("/")[-1], "w") as f:
            f.writelines(code)

        
    

if __name__ == "__main__":
    main()