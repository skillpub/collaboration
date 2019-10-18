# Grafana

We will take advantage of the Grafana server side rendering feature that can render any panel on the server. To verify that this feature works try the *Direct link rendered image* in the panel share dialog. If you do not get an image when opening this link read [here](https://grafana.com/docs/administration/image_rendering/) how to configure this feature.

<img src="../images/grafa_1.png" width="60%" hight="60%">

Create API key ([how to](https://grafana.com/docs/http_api/auth/)) or get cookie from your browser session.

Here is the example how to copy cookie from Chrome:
- Log in to Grafana
- Go to any Grafana panel *Direct link rendered image*
- Hit F12 to open the developer console (macOS: Cmd+Opt+J)
- Look at the Network tab
- Refresh the page
Right click the request in the Network tab, and select "Copy as cURL"

This will give you the curl command with cookie.

In 19 lines of code bellow *[skills/grafa.py](../../skills/grafa.py)* we put *Direct link rendered image* into string panel_url with panelId as argument```panelId={}```, then we show all panels with ids stored in array ```panels```.

``` python
'''Grafana dashboards'''
import os, random
from PIL import Image

panel_url = "http://127.0.0.1:3000/render/d-solo/XXXXXX/demo?orgId=1&panelId={}&width=1000&height=500"
api_key = "Authorization: Bearer eyJrXXXXXXXXXXXXXXXXXXXXXXXXXXXXiOjF9"
cookie = "Cookie: grafana_session=5384XXXXXXXXXXXXXXeae"

auth_header = api_key # or cookie, whatever will work with your Grafana installation
panels = ['1','2'] # place here panels ids you want to get  

for panelId in panels:  
    file_tmp = "panel_{}.png".format(str(random.randint(1,10000)))
    os.system("curl -o {} '{}' -H '{}'".format(file_tmp, panel_url.format(panelId), auth_header))

    image = Image.open(file_tmp)
    image.show()

    os.remove(file_tmp)
```

In Slack it looks like

<img src="../images/grafa_2.png" width="60%" hight="60%">


