#fhand = open('/home/inna/Documents/mbox-short.txt')

"""Exercise 2: Figure out which line of the above program is still not properly guarded.
See if you can construct a text file which causes the program to fail and 
then modify the program so that the line is properly guarded and test 
it to make sure it handles your new text file.

Exercise 3: Rewrite the guardian code in the above example without two if statements. 
Instead, use a compound logical expression using the 
and logical operator with a single if statement.
"""

filename = input('Enter the file name: ')
try:
    file = open(filename, 'r')
except:
    print('File cannot be opened:', filename)
    exit()

for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])