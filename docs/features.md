
# Features

- [Running a regular Python script by the request via Chat App, with no extra coding for Chat App interfacing](#running-a-regular-python-script-by-the-request-via-chat-app-with-no-extra-coding-for-chat-app-interfacing)
- [Supported Chat Apps : Slack, Telegram](#supported-chat-apps--slack-telegram)
- [Command line arguments from Chat App to script](#command-line-arguments-from-chat-app-to-script)
- [Text outputs redirection to Chat App](#text-outputs-redirection-to-chat-app)
- [Images/graphs redirection to Chat App](#imagesgraphs-redirection-to-chat-app)
- [Sending files from the script to Chat App as attachments](#sending-files-from-the-script-to-chat-app-as-attachments)
- [Input requests redirection to Chat App](#input-requests-redirection-to-chat-app)
- [Inputing files from Chat App to script](#inputing-files-from-chat-app-to-script)
- [Automatic "help" generation](#automatic-help-generation)
- [Logging](#logging)
- [User access control](#user-access-control)
- [Alias for mentions in groups or channels](#alias-for-mentions-in-groups-or-channels)
- [Web interface for scripts management and development](#web-interface-for-scripts-management-and-development)

# 

### Running a regular Python script by the request via Chat App, with no extra coding for Chat App interfacing

Pyhton file in folder *skills* can be run from Chat App. 
Example - *skills/hello.py*

```python
print("Hello from Outerspace! :wave:")
```
 
And how it looks in Slack

<img src="images/hello.png" width="30%" hight="30%">

#

### Supported Chat Apps : Slack, Telegram

With simple configuration bellow

```json
{ 
    "users": {
        "james": {"channels": {"slack" : "james", "telegram": 1001}}
    },
    
    "channels": {
        "telegram": {"token": "123456789:QWER_1234567890qwertyu-iopasdfghjklz"},
        "slack": {"token": "xoxb-qwertyuiopa-123456789012-asdfghjklzxcvbnm123456}
    }
}
```

User James can run Python scripts from both Chat Apps 

**Slack**

<img src="images/hello.png" width="30%" hight="30%"> 

**Telegram**

<img src="images/hello_t.png" width="40%" hight="40%">

#

### Command line arguments from Chat App to script

Everything you passed after script name in Chat App can be accessed as usual for Python via sys.argv.

Example - calculator in chat.
With usage "calc 100*64 - (3000\*0.75 + 100)\*12".

Script *skills/calc.py*

```python
import sys
import re

expression = ' '.join(sys.argv[1:])

not_allowed_symbols = re.findall('[^0-9)(*\-+./ ]',expression)

if len(not_allowed_symbols) != 0:
    print("only symbols 0-9 . - + / * () are allowed")
    sys.exit()

try:    
    res = eval(expression)
    print(res)
    
except ZeroDivisionError:
    print("oops.. divided by zero")

except Exception as e:
    print("your expression seems incorrect")
````

Usage

<img src="images/calc.png" width="40%" hight="40%"> 

#

### Text outputs redirection to Chat App

As we showed in previous examples all *outputs* are redirected to Chat App.

#

### Images/graphs redirection to Chat App

You just use the habitual Python modules for showing images.

Example 1 - `Image`, *skills/iss.py*

```python
from urllib.request import urlopen
from PIL import Image

commands = sys.argv

if "look" in commands:
    wiki_page = urlopen("https://en.wikipedia.org/wiki/International_Space_Station").read().decode()
    first_image = urlopen('https:'+re.findall('src="(//upload.wikimedia.org/wikipedia.+?\.jpg)"',wiki_page)[0])
    image = Image.open(first_image)
    image.show()
```

<img src="images/iss_look.png" width="50%" hight="50%"> 

Example 2 - `matplotlib`, *skills/sin.py*

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi)
y = np.sin(x)

plt.stem(x, y)
plt.show()
```

<img src="images/matplotlib.png" width="50%" hight="50%"> 

#

### Sending files from the script to Chat App as attachments

We added to the print function the ability to output files as an attachment. Here is the example - *skills/patents.py*

```python
from urllib.request import urlopen

data = urlopen("https://data.nasa.gov/api/views/gquh-watm/rows.csv?accessType=DOWNLOAD").read().decode()

print({"nasa_patents.csv":data})
```

The syntax is `print({"filename.ext": "file content, string or bytes"})`

In Slack it looks like

<img src="images/patents.png" width="100%" hight="100%"> 

#

### Input requests redirection to Chat App

#

### Inputing files from Chat App to script

#

### Automatic "help" generation

#

### Logging

#

### User access control

#

### Alias for mentions in groups or channels

#

### Web interface for scripts management and development
