# https://itunes.apple.com/search?entity=song&limit=l&term=weezer

# You get a standard JSON file 
# JSON - JavaScript Object
# Nowadays it is typically used as language agnostic format for exchanging data between computers.

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# Please remove the weezer from the link, you have to type weezer on the terminal 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=l&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])