import urllib.request
import urllib.parse
  
# trying to read the URL but with no internet connectivity
try:
    x = urllib.request.urlopen('https://www.google.com')
    print(x.read())
  
# Catching the exception generated     
except Exception as e :
    print(str(e))