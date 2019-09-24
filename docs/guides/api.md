# API's

Aceess API is bacicaly two lines. 

Example
```python
from urllib.request import urlopen
data = urlopen("http://api.open-notify.org/astros.json").read().decode()
```

API response is in ```data``` variable

Probably this data is JSON, so just use

```python
import json
data = json.loads(data)
```

Now you can access ```data``` as a dictionary, like ```data["message"]```.  
