"""Exercise 2: Change your socket program so that it counts the number 
of characters it has received and stops displaying any text after 
it has shown 3000 characters. The program should retrieve the entire document 
and count the total number of characters and display the count of the number of 
characters at the end of the document."""

import socket
import re

url = input("Enter url: ")
url_verification = re.search(r'^(?P<http>https?://|www\d{0,3}[.]|)(?P<host>[a-z0-9.\-]+[.][a-z]{2,4})/.*', url)
if url_verification is not None:
    link = url_verification.group('host')
else:
    print('Could not parse url address. Please verify provided link')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for i in range(3):    
        print('Connecting...')
    try:
        s.connect((link, 80))
    except:
        print("Failed to connect. Make sure the url exists")
        quit()

    cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    s.send(cmd)

    count = 0
    text = ''
    while True:
        data = s.recv(512)
        count = count + len(data)
        text = text + data.decode()

        if len(data) < 1:
            break

print(text.strip('\n')[:301])
print(f'Total # of characters {count}')

