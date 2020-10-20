"""Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from 
(i.e., the whole email address). At the end of the program, 
print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}"""

filename = input("Please enter filename: ")
try:
    file = open(filename, 'r')
except:
    print('This file could not be opened')
    quit()

dns = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1].split('@')
    dns[email[1]] = dns.get(email[1], 0) +1

print(dns)