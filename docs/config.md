# Config

Skillpub Config is JSON file with semantic parts:

 - [users](https://github.com/skillpub/collaboration/blob/master/docs/config.md#users)
 - [channels](https://github.com/skillpub/collaboration/blob/master/docs/config.md#channels)
 - [publishers](https://github.com/skillpub/collaboration/blob/master/docs/config.md#publishers)
 - [jupyter](https://github.com/skillpub/collaboration/blob/master/docs/config.md#jupyter)
 - [license](https://github.com/skillpub/collaboration/blob/master/docs/config.md#license)

At the end of this description you can find example with all these parts.

### Users

```
"users" : {
    "UNIQ_USER_NAME": { "channels" : {}, "groups" : [] }
}
```

UNIQ_USER_NAME is string

Supported channels are "slack" and "telegram".

```
"channels": {"slack" : "USER_NAME_IN_SLACK", "telegram": ISER_ID_IN_TELEGRAM}
```

USER_NAME_IN_SLACK is string
ISER_ID_IN_TELEGRAM is integer

Groups mean access to scripts placed in subfolders of *skills* folder.

```
"groups": ["SUBFOLDER_1", "SUBFOLDER_2"]
```

For example

```
|-- skills
    |-- hello.py
    |-- admin
        |-- logs.py
```

To grant access to script logs.py use

```
"groups": ["admin"]
```

# 

### Channels

#

### Publishers

#

### Jupyter

#

### License

#

### Config example

```
{
    "users": {
        "james": {"groups":["science","ufo_contacts"], "channels": {"slack" : "james", "telegram" : 1001}},
        "john": {"groups":["science"], "channels": {"slack" : "john"}},
        "mary": {"channels": {"slack" : "mary"}},
        "robert": {"channels": {"slack" : "robert"}},
        "patricia": {"channels": {"slack" : "patricia"}}
    },

    "publishers": ["james","john","mary"],

    "channels": {
        "slack": {"token": "xoxb-qwertyuiopa-123456789012-asdfghjklzxcvbnm123456"},
        "telegram": {"token": "123456789:QWERTYUIOPasdfghjklZXCVBNMqwertyuio"}
    },
    
    "jupyter": {"host": "helper.nasa.com"},

    "license": "free"
}
```
