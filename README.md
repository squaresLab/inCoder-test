# InCoder test 

Divided into two main sections: data, and source. `data` contains four sub-repositories each with slightly modified versions of the Python programs from the Quixbugs dataset, and `source` contains the Python scripts used to generate this data. 

## Data 

FILE structure:

```
data  
│
└───python_programs
│       bitcount.py 
│       kheapsort.py
│       ......
│       
└───trimmed_programs
│       bitcount.py 
│       kheapsort.py
│       ......
│       
└───bug_drop
│       bitcount.py 
│       kheapsort.py
│       ......
│       
└───random_drop
        bitcount.py 
        kheapsort.py
        ......
```

### `python_programs` 
The initial Python programs from the Quixbugs dataset, which each contain a one-line bug

### `trimmed_programs`
Each program from `python_programs` with the trailing comments and whitespace removed 

### `bug_drop` 
Each program from `trimmed_programs` with the buggy line removed, line number given in file name

### `random_drop` 
Each program from `trimmed_programs` with a random line removed, line number given in file name

# Source

```
source 
│
└───read_programs.py       
└───build_db.py
└───drop_lines.py

```

## `read_programs.py`
Simply removes the trailing comments and whitespace from each program in `python_programs`, and writes the new programs to `trimmed_programs` 

## `build_db.py` 
Creates a SQLite databse called `Quixbugs`, with two tables, `programs` and `lines`. Programs contains information about each file as a whole, whereas line contains data on each individual line within the program.  

```
programs
+------------+
| Field      | 
+------------+
| id         | 
| prog       | --> program name (text)
| length     | --> number of lines (integer)
| true_bug   | --> the buggy line (text)
| true_patch | --> the patch line (text)
| line_num   | --> the line where the bug occurs (integer)
+------------+
```

```
lines
+------------+
| Field      | 
+------------+
| id         | 
| prog_id    | --> foreign key to `programs` table
| line_number| --> current line number (integer)
| line       | --> current line (text)
| is_bug     | --> True if line matches the bug (boolean)
+------------+
```

## `drop_lines.py` 

Drop lines uses the `Quixbugs` database created above to create `data/bug_drop` and `data/random_drop`. For each program in the databse, we query the length of the program, and then select a random number between 1 and length to drop. We assert that the line is not the same as the buggy line, and contains code (is != newline character). Then, all lines excluding the one to be dropped are written to `data/random_drop/<program_name>_random_drop#.py`, with <insert> written in place of the dropped line. For `data/bug_drop`, we query the buggy line for the program in question, and then re-write the program to this file with <insert> in place of the bug).  


