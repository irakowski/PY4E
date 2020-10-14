"""Exercise 3: Write a program to read through a mail log, build a histogram using 
a dictionary to count how many messages have come from each email address, 
and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}"""

filename = input('Enter a filename: ')

try:
    file = open(filename, 'r')
except:
    print('File could not be opened')
    quit()

emails = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    emails[words[1]] = emails.get(words[1], 0) + 1
print(emails)

count = list(emails.values())
for key, value in emails.items():
    if value == max(count):
        print(key, value)
