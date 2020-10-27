"""Exercise 2: Write a program to look for lines of the form

`New Revision: 39772`
and extract the number from each of the lines using a regular expression 
and the findall() method. Compute the average of the numbers and print out the average.
Enter file:mbox.txt
38549.7949721
Enter file:mbox-short.txt
39756.9259259"""
import re

filename = input("Enter file path: ")
try:
    file = open(filename, 'r')
except:
    print('No such file')
    quit()

values = []
for line in file:
    line = line.strip()
    matches = re.findall(r'[0-9]+', line)
    if len(matches) > 0:
        for i in matches:
            values.append(int(i))
print(f'There are {len(values)} values with sum={sum(values)}')