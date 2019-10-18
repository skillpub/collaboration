'''Grafana dashboards'''
import os, random
from PIL import Image

panel_url = "http://127.0.0.1:3000/render/d-solo/XXXXXX/demo?orgId=1&panelId={}&width=1000&height=500"
api_key = "Authorization: Bearer eyJrXXXXXXXXXXXXXXXXXXXXXXXXXXXXiOjF9"
cookie = "Cookie: grafana_session=5384XXXXXXXXXXXXXXeae"
auth_header = api_key # or cookie, whatever will work with your Grafana installation

for panelId in ['1','2']:  
    file_tmp = "panel_{}.png".format(str(random.randint(1,10000)))
    os.system("curl -o {} '{}' -H '{}'".format(file_tmp, panel_url.format(panelId), auth_header))

    image = Image.open(file_tmp)
    image.show()

    os.remove(file_tmp)
