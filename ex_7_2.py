"""Exercise 2: Write a program to prompt for a file name,
and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475
When you encounter a line that starts with "X-DSPAM-Confidence:"
pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam 
confidence values from these lines. When you reach the end of the file, 
print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.

Exercise 3. Add a harmless Easter Egg to the program """

filename = input('Enter the file name: ')
try:
    file = open(filename, 'r')
except:
    if filename == "help":
        print("Try using full path to the file. Good luck!")
    else:
        print('File cannot be opened:', filename)
    exit()

total = 0
count = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        num = float(line[line.find(':')+1:].lstrip())
        total += num
print(f"Average spam confidence: {total/count}")
