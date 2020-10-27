"""The program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, scan for a tag that is in a particular 
position relative to the first name in the list, follow that link and repeat the process 
a number of times and report the last name you find."""

##TESTING 
##http://py4e-data.dr-chuck.net/known_by_Lorena.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter valid url:  ')
count = input('Enter count: ')
position = input('Enter position: ')
try:
    count = int(count)
except:
    print('Count value must be a number')
    quit()

try:    
    position =int(position)
except:
    print('Position value should be a number')
    quit()

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#For a given number of times, retrieve anchortags on the page, go to the link at a given positon
for _ in range(count):
    a_tags = soup.find_all('a')
    links = list()
    for tag in a_tags:
        links.append(tag.get('href', None))
    print(f'Retriving link {links[position-1]}')
    html = urllib.request.urlopen(links[position-1], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

