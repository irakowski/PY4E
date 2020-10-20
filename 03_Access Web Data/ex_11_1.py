"""Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
"""
import re

reg = input("Enter a regular expression: ")
try:
    pattern = re.compile(reg)
except:
    print("Not a valid regular expression")
    quit()

file = open('/home/inna/Documents/mbox.txt', 'r')
matched_lines = 0
for line in file:
    match = pattern.search(line)
    if match is not None:
        matched_lines += 1
print(f'mbox.txt had {matched_lines} lines that matched {reg}')