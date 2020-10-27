"""Exercise 5: Change the socket program so that it only shows 
data after the headers and a blank line have been received. 
Remember that recv receives characters (newlines and all), not lines.
"""
import socket
import re

url = input('Enter url: ')
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
        print('Failed to connect. Make sure the url exists')
        quit()

    cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()

    s.send(cmd)

    text =''
    while True:
        data = s.recv(512)
        text += data.decode()
        if len(data) < 1:
            break
    # Look for the end of the header (2 CRLF)
    header_end = text.find('\r\n\r\n')

    # Skip past the header and printout data
    print(text[header_end+4:])