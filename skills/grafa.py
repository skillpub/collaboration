'''grafana dashboards'''

import os, random
from PIL import Image

api_key = "eyJrIjoiXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXIiwiaWQiOjF9"
render_url = "http://10.10.10.10:3000/render/d-solo"

dashboards = {
    'mydashboard' : ['/TXSTREZ/mydashboard\?orgId\=1\&panelId\=4\&width\=1000\&height\=500\&tz\=Europe%2FMoscow',
                     '/TXSTREZ/mydashboard\?orgId\=1\&panelId\=5\&width\=1000\&height\=500\&tz\=Europe%2FMoscow'
                    ],
    'streaming' : ['/VYrfz82Wz/streaming\?orgId\=1\&panelId\=2\&width\=1000\&height\=500\&tz\=Europe%2FMoscow']
}

commands = ["mydashboard", "streaming"]
argv = ' '.join(sys.argv)

command = next((command for command in commands if command in argv), None)

if command is None:
    print({'buttons':['grafa mydashboard', 'grafa streaming']})

if command == 'mydashboard':
    for panel in dashboards['mydashboard']:
        
        file_tmp = '/home/chernikovanv/nasahelper/tmp/grafa_graph_{}.png'.format(str(random.randint(1,10000)))
        cmd = 'curl -o {} -H "Authorization: Bearer {}" {}{}'.format(file_tmp, api_key, render_url, panel)
        os.system(cmd)

        image = Image.open(file_tmp)
        image.show()

        os.remove(file_tmp)
