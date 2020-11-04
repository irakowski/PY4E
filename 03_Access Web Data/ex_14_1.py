"""This application will read the mailbox data (mbox.txt) and 
count the number of email messages per organization (i.e. domain name of the email address) 
inserting records into a database with the following schema to maintain the counts.
CREATE TABLE Counts (org TEXT, count INTEGER)"""
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = input("Please enter filename: ")
try:
    file = open(filename, 'r')
except:
    print('This file could not be opened')
    quit()

for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1].split('@')
    org = email[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()