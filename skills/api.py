'''uses web API'''
from urllib.request import urlopen
from urllib.error import HTTPError
import json

try:
    data = urlopen("http://api.open-notify.org/astros.json").read().decode()
    data = json.loads(data)
    for astro in data["people"]:
        print(astro["name"])
except HTTPError as e:
    print(str(e))
