```uses web API```
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    data = urlopen("http://api.open-notify.org/astros.json").read().decode()
    data = json.loads(data)
    print(data)
except HTTPError as e:
    print(str(e))
