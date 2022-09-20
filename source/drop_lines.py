#make sure things were correctly added to db

import sqlite3
from re import L
import random
import os

def connect_db():
    conn = sqlite3.connect('Quixbugs.db')
    c = conn.cursor()
    return c, conn

def get_prog_length(c, conn):
    c.execute("SELECT id, prog,length,line_num FROM programs")
    rows = c.fetchall()
    return rows

def get_lines(c, conn, prog_id):
    c.execute("SELECT line_number, line FROM lines WHERE prog_id =" +str(prog_id))
    rows = c.fetchall()
    return rows

def check_empty(c, conn, id, rand):
    c.execute("SELECT line FROM lines WHERE prog_id =" +str(id) + " AND line_number =" + str(rand))
    line = c.fetchone()
    if line[0] == "\n":
        return True
    else:
        return False

def write_random_drop(name, rand, rows):
    with open("data/random_drop/" + name + "_" + str(rand) + ".py", "w") as f:
        for row in rows:
            line_num, line = row
            if line_num == rand:
                #get the whitespace on LHS of line 
                whitespace = line[:len(line) - len(line.lstrip())]
                f.write(whitespace + "<insert>\n")
            else:
                f.write(line)

def write_bug_drop(name, buggy_line_num, rows):
    with open("data/bug_drop/" + name + "_" + str(buggy_line_num) + ".py", "w") as f:
        for row in rows:
            line_num, line = row
            if line_num == buggy_line_num:
                whitespace = line[:len(line) - len(line.lstrip())]
                f.write(whitespace + "<insert>\n")
            else:
                f.write(line)

def make_dir(path):
    if os.path.exists(path):
        os.system("rm -r " + path)
    os.mkdir(path)

def main():
    c, conn = connect_db()
    rows = get_prog_length(c, conn)
    make_dir("data/random_drop")
    make_dir("data/bug_drop")
    for prog in rows:
        id, name, length, line_num = prog
        if line_num is None: 
            print(prog)
        #generate a random number between one and length 
        rand = random.randint(1, length)
        is_empty = check_empty(c, conn, id, rand)
        while rand == line_num or is_empty:
            rand = random.randint(1, length)
            is_empty = check_empty(c, conn, id, rand)
        #write the program to a file with the name of the program and the random number
        rows = get_lines(c, conn, id)
        write_random_drop(name, rand, rows)
        write_bug_drop(name, line_num, rows)
    

if __name__ == "__main__":
    main()