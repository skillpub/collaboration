# skillpub

Skillpub is technology and collaboration tool for personal or team tasks automation and sharing them within team or entire organization through channels like Slack, email, Telegram, and others. This technology improves productivity, mobility and engagement throughout an organization, it provides platform for building a Virtual Assistant for team. With every automated and shared task employees are getting more and more free to complete creative and responsible tasks while the Virtual Assistant handle routine tasks instead of them.    

# core technology 

Skillpub can take any script writed in high level language (Python), analize its inputs, prints, images or graphs display, other interactions with user and build connectors to this script from channles like Slack, email, Telegram, and others.
Script author doesn't think about how to connect with different channels, how to control access, how to monitor that script works fine when colegues run it, how to save logs, how to balance load if there are to much coleagues run this scripts and so on, basicly author do nothing to prepare script for sharing, no changes to code, Skillpub does all of this stuff. Author just drop script to Skillpub platform and tell to Skillpub which colleagues have the right to run a script.  

# pricing

Skillpub is free to use and unlimited in functionality for all channels except Slack, for Slack - 10 users are free, for more users need to buy license on www.skillpub.org.

# use cases


# quickstart

The Skillpub is distributed as a Python package on the Python Package Index (PyPI) and hosted on your server. 
The server requarements are 
  Linux machine (CentOS, Ubuntu, Debian, ... )
  Python 3.6 and above with pip

If you are familiar with Python and pip you can just run the line bellow otherwise you need to spend some time googling how to install Python 3 and pip on linux server (there are a lot of good instructions).

sudo pip install skillpub

or, more reliable in some cases

sudo python3 -m pip install skillpub

Then create a folder where you will store shared scripts (we will imagen that we are building Virtual Assstant for NASA team and name this folder nasahelper, you choose your folder name)

mkdir nasahelper

Navigate to this folder

cd nasahelper

And run Skillpub

skillpub

It will create config file and folder for shared scripts (skills).
Check it out by command

ls

Config file will looks like 

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

Slack token is "Bot User OAuth Access Token". To get it do the steps bellow

create Slack App - https://api.slack.com/apps/new 
create a Bot User for this App:
  Head to your [app's settings page](https://api.slack.com/apps) and click the Bot Users feature in the navigation menu.
  You'll be presented with a button marked Add a Bot User, and when you click on it, you'll see a screen where you can configure your app's bot user
  Once you've completed these fields, click the Add Bot User button and then Save Changes.
Install the App to a workspace:
  On your [app's settings page](https://api.slack.com/apps) again, click the OAuth & Permissions settings item in the navigation menu.
  On this page, click a button marked Install App to your Workspace.
  You'll see a permissions authorization page, where you should click Authorize and then you will see your "Bot User OAuth Access Token".








