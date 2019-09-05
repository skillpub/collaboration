
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
Here is an example file - *skills/hello.py*

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

and example file - *skills/hello.py*

```python
print("Hello from Outerspace! :wave:")
```

James from NASA can run Python scripts from both Chat Apps 

**Slack**

<img src="images/hello.png" width="30%" hight="30%"> 

**Telegram**

<img src="images/hello_t.png" width="30%" hight="30%">

#

### Command line arguments from Chat App to script

Everything you passed after script name in Chat App can be accessed as usual for Python via sys.argv.

Example - calculator in chat, (skills/calc.py)[https://github.com/skillpub/collaboration/blob/master/skills/calc.py].
With usage "calc 100*64 - (3000\*0.75 + 100)\*12".

Code

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



#

### Text outputs redirection to Chat App
### Images/graphs redirection to Chat App
### Sending files from the script to Chat App as attachments
### Input requests redirection to Chat App
### Inputing files from Chat App to script
### Automatic "help" generation
### Logging
### User access control
### Alias for mentions in groups or channels
### Web interface for scripts management and development


