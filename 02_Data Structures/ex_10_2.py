"""Exercise 2: This program counts the distribution of the hour of 
the day for each of the messages. You can pull the hour from the "From" line
by finding the time string and then splitting that string into parts using the colon character. 
Once you have accumulated the counts for each hour, print out the counts, one per line, 
sorted by hour as shown below.

Sample Execution:

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1"""

filename = input("Enter a filename path: ")
try:
    file = open(filename, 'r')
except:
    print("Incorrect path. No such file found")
    quit()

h = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    time = words[5]
    hours, minutes, sec = time.split(":")
    h[hours] = h.get(hours, 0) + 1

h_list = list()
for key, value in h.items():
    h_list.append((key, value))

h_list.sort()

for key, value in h_list:
    print(key, value)


