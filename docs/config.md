# Config

Skillpub Config is JSON file with semantic parts:

 - [users](https://github.com/skillpub/collaboration/blob/master/docs/config.md#users)
 - [channels](https://github.com/skillpub/collaboration/blob/master/docs/config.md#channels)
 - [publishers](https://github.com/skillpub/collaboration/blob/master/docs/config.md#publishers)
 - [jupyter](https://github.com/skillpub/collaboration/blob/master/docs/config.md#jupyter)
 - [license](https://github.com/skillpub/collaboration/blob/master/docs/config.md#license)

At the end of this description you can find example with all these parts.

### Users

```json
"users" : {
    "USER_NAME": { "channels" : {}, "groups" : [] }
}
```

USER_NAME is string

Supported channels are "slack" and "telegram".

```
"channels": {"slack" : "SLACK_USER_NAME", "telegram": TELEGRAM_USER_ID}
```

SLACK_USER_NAME is string

TELEGRAM_USER_ID is integer

Groups mean access to scripts placed in subfolders of *skills* folder.

```json
"groups": ["SUBFOLDER_1", "SUBFOLDER_N"]
```

For example

```
|-- skills
    |-- hello.py
    |-- admin
        |-- logs.py
```

To grant access to script logs.py use

```json
"groups": ["admin"]
```

# 

### Channels

Supported channels are "slack" and "telegram".

```json
"channels": {
    "slack": {"token": "xoxb-XXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXX"},
    "telegram": {"token": "XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
}
```

**Slack token** is **"Bot User OAuth Access Token"** in terms of Slack documentation. To get it do the steps bellow

- Create **Slack App** - https://api.slack.com/apps/new. 
- Create a **Bot User** for this App:
  - Head to your [app's settings page](https://api.slack.com/apps) and click the **Bot Users** feature in the navigation menu.
  - You'll be presented with a button marked **Add a Bot User**, and when you click on it, you'll see a screen where you can configure your app's bot user.
  - The important here - **Display name**.
  - Once you've completed these fields, click the **Add Bot User** button and then **Save Changes**.
- Install the **App to a workspace**:
  - On your [app's settings page](https://api.slack.com/apps) again, click the **OAuth & Permissions** settings item in the navigation menu.
  - On this page, click a button marked **Install App to your Workspace**.
  - You'll see a permissions authorization page, where you should click **Authorize** and then you will see your **"Bot User OAuth Access Token"**.

**Telegram token** is the token to access the HTTPS Telegram API. 
You can get it from **Telegram bot [BotFather](https://telegram.me/botfather)**. Read more [here](https://core.telegram.org/bots).

#### Slack Interactive Components (buttons)

To use Interactive Components like buttons in Slack, you'll need to configure the Request URL (when you push the button Slack sends request to this URL). Skillpub supports only HTTP request, since it was born to work in internal networks, so better you configure HTTPS proxy wich recieve requests from Slack and forward them to Skillpub as http requests.  

The default Skillpub web service to listen requests is http://[IP or domain]:5000/slackaction, where [IP or domain] is your server where Skillpub is running.

If you need to change default port (5000) do it as follow

```json
"channels": {
    "slack": {"token": "xoxb-XXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXX", "requests": {"port": 65000}}
}
```

In Slack do these steps to route requests to your proxy

- Head to your [app's settings page](https://api.slack.com/apps) and click the **Interactive Components** feature in the navigation menu.
- Switch the Interactivity toggle to on.
- Configure the Request URL: https://[your proxy domain]/path/to/somewhere 
- Click the Save Changes button.

#

### Publishers

Publishers are users who have access to Skillpub web-based user interface.

```json
"publishers": ["USER_NAME_1","USER_NAME_N"],
```

#

### Jupyter

With "jupyter" option, you can change the default hostname of Skillpub web-based user interface.

```json
"jupyter": {"host": "HOST_NAME_OR_IP"},
```

#

### License

```json
"license": "free"
```

Here you'll place the token when using the paid version.

#

### Config example

```json
{
    "users": {
        "james": {"groups":["science","ufo_contacts"], "channels": {"slack" : "james", "telegram" : 1001}},
        "john": {"groups":["science"], "channels": {"slack" : "john"}},
        "mary": {"channels": {"slack" : "mary"}},
        "robert": {"channels": {"slack" : "robert"}},
        "patricia": {"channels": {"slack" : "patricia"}}
    },

    "channels": {
        "slack": {"token": "xoxb-qwertyuiopa-123456789012-asdfghjklzxcvbnm123456"},
        "telegram": {"token": "123456789:QWERTYUIOPasdfghjklZXCVBNMqwertyuio"}
    },
    
    "publishers": ["james","john","mary"],
    
    "jupyter": {"host": "helper.nasa.com"},

    "license": "free"
}
```
