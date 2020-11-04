"""This application will read roster data in JSON format, parse the file, 
and then produce an SQLite database that contains a User, Course, and Member table and 
populate the tables from the data file."""

import json
import sqlite3

conn = sqlite3.connect('roasterdb.sqlite')

cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        name TEXT UNIQUE
        );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title TEXT UNIQUE
        );

    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
        );
    ''')

filename= input('Enter file name: ')
if len(filename) < 1:
    filename = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],
try:
    data = open(filename,'r')
except:
    print('File couldn\'t be openned')
   
str_data = data.read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]
    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()