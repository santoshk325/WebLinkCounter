import urllib2
import BeautifulSoup
b=0
input = raw_input("What website(use http://www.websitename.com\n")
request = urllib2.Request(input)
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
for a in soup.findAll('a', href=True):
  b=b+1
  print a
print b
