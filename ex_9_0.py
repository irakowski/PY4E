"""Exercise 1: [wordlist2]

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn't matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary."""

filename = input('Enter filename: ')
try:
    file = open(filename, 'r')
except:
    print("This file could not be opened")
    quit()

words_dict = dict()
count = 0
for line in file:
    words = line.split()
    for word in words: 
        #words_dict = words_dict.get(word, 0) + 1
        if word not in words_dict:
            words_dict[word] = 1
        else: 
            words_dict[word] += 1
        
print(words_dict)
