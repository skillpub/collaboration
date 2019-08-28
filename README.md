# What is it:question:

The Skillpub is **technology and collaboration tool** for personal or team tasks **automation and sharing** automated tasks within a team or an entire organization through channels like Slack, Telegram, and others. Task automation and sharing boosts :rocket: productivity, mobility and engagement. It provides a base for **building a Virtual Assistant** for you, your team or organization. With every automated and shared task people are getting free to complete creative and responsible tasks :smirk: while the Virtual Assistant handles routine tasks :man_technologist:.

#  Core Technology :gem:

The technology is to take **script writed in high level language** (Python), analize its inputs/outputs, images or graphs display, other interactions with user and **build connectors to this script from channles like Slack, Telegram, and others**. Imagine that you described your skill as a script and gave it to **software robot**. And from that moment it is his skill, you and your colugues can ask him any time to run this skill and give results.
As a script author you don't think about how to connect with different channels, how to control access, how to monitor that script works fine when colegues run it, how to save logs, how to balance load if there are too many coleagues running script and so on, Skillpub does all of this so author doesn't need to think about what is that software robot, how it works, Skillpub will understand script by itself. Author **just drop script to the Skillpub platform and tell to Skillpub which colleagues have the right to run this script**.

# Pricing 

The Skillpub is free to use with unlimited functionality :tada: for all channels except Slack, **for Slack - :keycap_ten: users are free**, for more users, you need to buy a license on www.skillpub.org.

# For whom 

For teams who are in charge of Servers, Services on Servers, API's, Data Bases, Analytical reports and other information technology items. 

For tasks like
 - to fetch diagnostic information from multiple data sources, gather metrics/logs and analyzing them 
 - to take an action in case of incident, rerouting users requests, server rebooting, lounching new instances, and many other actions
 - to give easy access via messengers to your teams APIs for team members and other coleagues
 - to provide analytical reports by the request through messengers, reports with graphs, images, tables, files, etc.
 
These things are trivial to automate and share, you can do much more with high level lenguages (like Python), rich coommunication services (like Slack) and smart script sharing platforms (like Skillpub :sunglasses:). You can do amazing things for your team.

# Quickstart

The Skillpub is distributed as a **Python package** on the Python Package Index (PyPI) and hosted on your server. 
The server requarements are 
  - Linux machine (CentOS, Ubuntu, Debian, ... )
  - Python 3.6 and above with pip

If you are familiar with Python and pip you can just run the line bellow otherwise you need to spend some time googling how to install **Python 3 and pip on Linux server**.

```
sudo pip install skillpub
```

or, more reliable in some cases

```
sudo python3 -m pip install skillpub
```

Then create a folder where you will build your Virtual Assstant (we will imagen that we are building *Virtual Assstant for NASA team* and name this folder *nasahelper*, you choose your folder name)

```
mkdir nasahelper
```

Navigate to this folder

```
cd nasahelper
```

And run Skillpub

```
skillpub
```

It will create config file and folder for shared scripts (*skills*).
Check it out by command `ls` and then `cat config.json`

Config file will looks like 

```json
{
    "users": {
        "bob": {"channels": {"slack" : "bob", "telegram": 1001}},
        "alice": {"channels": {"slack" : "alice" , "telegram": 1002}}
    },

    "publishers": ["bob"],

    "channels": {
        "slack": {"token": "xoxb-XXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXX"},
        "telegram": {"token": "XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
    },

    "license": "free"
}
```
**Slack token** is **"Bot User OAuth Access Token"** in terms of Slack documentation. To get it do the steps bellow

- Create **Slack App** - https://api.slack.com/apps/new. 
- Create a **Bot User** for this App:
  - Head to your [app's settings page](https://api.slack.com/apps) and click the **Bot Users** feature in the navigation menu.
  - You'll be presented with a button marked **Add a Bot User**, and when you click on it, you'll see a screen where you can configure your app's bot user.
  - The important here - **Display name**. We choose *NasaHelper*. You choose your.
  - Once you've completed these fields, click the **Add Bot User** button and then **Save Changes**.
- Install the **App to a workspace**:
  - On your [app's settings page](https://api.slack.com/apps) again, click the **OAuth & Permissions** settings item in the navigation menu.
  - On this page, click a button marked **Install App to your Workspace**.
  - You'll see a permissions authorization page, where you should click **Authorize** and then you will see your **"Bot User OAuth Access Token"**.

**Telegram token** is the token to access the HTTPS Telegram API. 
You can get it from **Telegram bot [BotFather](https://telegram.me/botfather)**. Read more [here](https://core.telegram.org/bots).

So, now you can put your token into config file.

As you can guess **Users** part in config has user name and identificators of this user in different channels.
For Slack this identificator is **Slack user name**. For **Telegram** it's **user_id**.
 
Publishers are users who have access to Skillpub Web Application to work with scripts (it's well known [JupyterLab](https://jupyterlab.readthedocs.io)).

So, supposing our NASA team have 5 users and only Slack channel, config can be like:

```json
{
    "users": {
        "james": {"channels": {"slack" : "james"}},
        "john": {"channels": {"slack" : "john"}},
        "mary": {"channels": {"slack" : "mary"}},
        "robert": {"channels": {"slack" : "robert"}},
        "patricia": {"channels": {"slack" : "patricia"}}
    },

    "publishers": ["james","john","mary"],

    "channels": {
        "slack": {"token": "xoxb-qwertyuiopa-123456789012-asdfghjklzxcvbnm123456"}
    },

    "license": "free"
}
```
Config is ready, RUN ```skillpub``` :exclamation:

Go to your **Slack messenger**, left menu, press :heavy_plus_sign: in section **Apps** or **Direct Messages**, find your bot (our is *NasaHelper*) and open chat whith it. It should be online (little circle next to name should be green).

Text to your bot ```hello```, you'll see the answer.

Now go to the folder *skills* (as you remember it was created when we first time run Skillpub).
You will see *hello.py* script, open it, you'll see the code, play whith it, use the Power :muscle: of Python. Skillpub will apply changes automatically when you save file. For training purposes we have prepared a script that could be used in NASA - [this one](skills/iss.py). Copy it to yor *skills* folder. Text to your bot `iss location` or `iss speed` or `iss people`, you'll see the International Space Station current location, speed, and astronauts photos. As you can see in script - it's pure Python, nothing about connections with any channels. 

That is all for Quickstart, all other things in our Tutorial. Just a few poins to add here:
 - Pyhton file in folder *skills* can be run from channel (Slack in our example)
 - file name - is command to run
 - first line in file in triple quote is skill help, text to your bot ```help``` to see it
 - text to your bot ```publisher```, or just ```pub``` to get a link to Skillpub Web Application ([JupyterLab](https://jupyterlab.readthedocs.io)), check it out. Remember you must be in publishers list in config. The link will be like - http://server-01p.nasa.com:8888/lab/workspaces/james/?token=a123... The hostname (*server-01p.nasa.com* in our example) is what Skillpub can get as a default hostname of your server. If you need to change it add to the config ```"jupyter":{"host":"your host name or IP"}```
 - to manage access to scripts put them to subfolders in folder skills, and add subfolder name to user groups like this ```"james": {"groups":["subfolder 1","subfolder 2"], "channels": {"slack" : "james"}}```
 - to pass arguments to your script text them after command, like this ```hello blabla bla```, in script you can access them as usual for Python - ```sys.argv```

For more details and examples go to our Tutorial. Thanks for attention, see you :wave:

P.S. here is the example of config file with subfolders, host name, etc. - [config.json](config.json)
