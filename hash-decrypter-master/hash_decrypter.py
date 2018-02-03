
from urllib2 import urlopen
print """
-------------------------------------------
|          Ayrus the hash decrypter           |
-------------------------------------------
        
"""
haSH = raw_input('Please Enter a valid hash: ')
request_url = "http://suryaveer.000webhostapp.com/?hash=" + haSH
string = urlopen(request_url).read()
print '\n'+string
