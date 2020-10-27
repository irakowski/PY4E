"""Exercise 3: Use urllib to replicate the previous exercise of 
(1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and 
(3) counting the overall number of characters in the document. 
Don’t worry about the headers for this exercise, simply show the 
first 3000 characters of the document contents."""


import urllib.request
import re 

url = input('Enter valid url: ')
url_verification = re.search(r'^(?P<http>https?://|www\d{0,3}[.]|)(?P<host>[a-z0-9.\-]+[.][a-z]{2,4})/.*', url)
if url_verification is not None:
    url = url_verification.group()
else:
    print('Could not parse url address. Please verify provided link')
    quit()

with urllib.request.urlopen(url) as response:
    print()
    count = 0
    text = ''
    for line in response:
        for character in line:
            count +=1
        text = text + line.decode().strip()
    print(text[:30]) 
    print(f'Total # of characters: {count}')
