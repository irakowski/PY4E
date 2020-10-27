"""Exercise 1: Pprompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract 
the host name for the socket connect call. Add error checking using try and 
except to handle the condition where the user enters an improperly formatted or non-existent URL."""

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
    #s.sendall("GET / HTTP/1.1\r\nHost: www.hostname.com\r\n\r\n")
    s.send(cmd)

    while True:
        data = s.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
