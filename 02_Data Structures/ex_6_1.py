"""Exercise 3:

Encapsulate code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments."""

def count_letter(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    return count

print(count_letter('hello', "l"))