# https://itunes.apple.com/search?entity=song&limit=l&term=weezer

# You get a standard JSON file 
# JSON - JavaScript Object
# Nowadays it is typically used as language agnostic format for exchanging data between computers.


import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=l&term=weezer" + sys.argv[1])
print(response.json())