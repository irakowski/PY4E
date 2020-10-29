"""The program will prompt for a URL, read the XML data from that URL using urllib 
and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file.
Data: 
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

try:
    f = urllib.request.urlopen(url, context=ctx).read()
except:
    print('Verify your url')
    quit()

print(f'Retrieving {url}')

data = f.decode()
print(f'Retrieved {len(data)} characters')
root = ET.fromstring(data)

nums = list()
for count in root.findall('.//count'):
    nums.append(int(count.text))
print(f'Sum: {sum(nums)}')


