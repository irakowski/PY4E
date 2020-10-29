"""The program will prompt for a URL, load json data from that URL  
and then parse and extract the comment counts from the json data, 
compute the sum of the numbers in the file.
Data: 
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
"""
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
try:
    f = urllib.request.urlopen(url, context=ctx)
except:
    print('Verify your url')
    quit()

print(f'Retrieving {url}')

data = f.read().decode()
print(f'Retrieved {len(data)} characters')

js = json.loads(data)
#print(json.dumps(js, indent=2))
comments = js['comments']
print(f'Comments Count: {len(comments)}')
nums = list()
for item in comments:
    nums.append(item.get('count'))

print(f'Sum: {sum(nums)}')