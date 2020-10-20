"""
Exercise 3: Write a program that reads a file and prints 
the letters in decreasing order of frequency. Your program should convert all the input 
to lower case and only count the letters a-z. Your program should not count spaces, 
digits, punctuation, or anything other than the letters a-z. Find text samples from several 
different languages and see how letter frequency varies between languages. 
Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies."""
import string

filename = input('Enter a file path:')
try: 
    file = open(filename, 'r')
except:
    print('Incorrect path. No such file found')
    quit()

acc = ''
for line in file:
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.translate(line.maketrans('','', '1234567890'))
    line = line.lower()
    words = line.split()
    if len(words) < 1:
        continue
    for word in words: 
        acc = acc + word

letters = dict()
for i in acc:
    letters[i] = letters.get(i, 0) + 1

list_to_sort = list()
for key, value in letters.items():
    list_to_sort.append((value, key))

list_to_sort.sort(reverse=True)

for key, value in list_to_sort:
    print(value, key)

