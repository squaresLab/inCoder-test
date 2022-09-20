import os 
import json

def get_patch(prog_name):
    root_path = 'data/py-lines'
    with open(os.path.join(root_path, prog_name+'.py')) as f:
        data = json.load(f)
        return data["correct_line"]

random_infill_path = 'data/random_drop_infill'
bug_infill_path = 'data/bug_drop_infill'

random_infill_files = os.listdir(random_infill_path)
bug_infill_files = os.listdir(bug_infill_path)

for file in bug_infill_files:
    prog_name = file.split('/')[-1].split('.')[0]
    true_patch = get_patch(prog_name)
    infill_patch = get_infill(file)
    print()
    print(f'### PROGRAM: {prog_name}\nGT patch:\n{true_patch}')
    for i, patch in enumerate(infill_patch):
        print(f'Infill {i}:\n{patch}')
    print()
    