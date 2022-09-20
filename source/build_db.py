import os 
import sys 
import json

from re import L
import sqlite3

def build_db():
    conn = sqlite3.connect('Quixbugs.db')
    c = conn.cursor()
    return c, conn

def drop_tables(c, conn):
    c.execute("DROP TABLE programs")
    c.execute("DROP TABLE lines")
    conn.commit()

def create_prog_table(c, conn):
    c.execute('''CREATE TABLE IF NOT EXISTS programs
                (id integer primary key, prog text, length integer, true_bug text, true_patch text, line_num integer)''')
    conn.commit()

def create_lines_table(c, conn):
    c.execute('''CREATE TABLE IF NOT EXISTS lines
                (id integer primary key, prog_id integer, line_number integer, line text, is_bug boolean)''')
    conn.commit()

def get_programs(path):
    prog_paths = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            prog_paths.append(os.path.join(path, file))
    return prog_paths

def get_line_data(name):
    path = "data/py-lines/" + name
    with open(path, "r") as f:
        data = json.load(f)
    buggy_line = data["buggy_line"]
    correct_line = data["correct_line"]
    return buggy_line, correct_line

def get_code(prog_path):
    with open(prog_path, "r") as f:
        code = f.readlines()
    return code

def process_lines(code, buggy_line):
    buggy_line_num = None
    for i, line in enumerate(code):
        if line == buggy_line or line+'\n' == buggy_line:
            buggy_line_num = i+1
            break
    return buggy_line_num

def add_program(c, conn, name, length, buggy_line, correct_line, buggy_line_number):
    c.execute("INSERT INTO programs VALUES (NULL, ?, ?, ?, ?, ?)", (name, length, buggy_line, correct_line, buggy_line_number))
    conn.commit()
    return c.lastrowid

def main():
    c, conn = build_db()
    drop_tables(c, conn)
    create_prog_table(c, conn)
    create_lines_table(c, conn)
    missing_files = ['depth_first_search.py', 'shunting_yard.py', 'reverse_linked_list.py', 'wrap.py']
    path = "data/trimmed_programs"
    prog_paths = get_programs(path)
    for prog_path in prog_paths:
        name = prog_path.split("/")[-1]
        if name in missing_files:
            continue
        code = get_code(prog_path)
        buggy_line, correct_line = get_line_data(name)
        buggy_line_number = process_lines(code, buggy_line)
        last_row_id = add_program(c, conn, name, len(code), buggy_line, correct_line, buggy_line_number)
        for i, line in enumerate(code):
            c.execute("INSERT INTO lines VALUES (NULL, ?, ?, ?, ?)", (last_row_id, i+1, line, i+1 == buggy_line_number))
            conn.commit()
    conn.close()
        

if __name__ == "__main__":
    main()