"""The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers in the file."""
##Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
##Actual data: http://py4e-data.dr-chuck.net/comments_1003385.html 


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter valid url:  ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the paragraph tags
span_tags = soup.find_all('span')
nums = list()
for tag in span_tags:
    nums.append(int(tag.string))

print(f'{sum(nums)}')

