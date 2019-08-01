'''some data about International Space Station'''
from urllib.request import urlopen
import json
import re
import random

data = json.loads(urlopen("http://api.open-notify.org/iss-now.json").read())['iss_position']

print('*International Space Station Current Location* :earth_americas: :satellite:')
print('https://www.google.com/maps/search/?api=1&query={},{}'.format(data['latitude'],data['longitude']))

print('*People In Space* :face_with_cowboy_hat:')
data = json.loads(urlopen("http://api.open-notify.org/astros.json").read())
for astro in data['people']:
    try:
        astro_name = astro['name']
        wiki_page = urlopen('https://en.wikipedia.org/wiki/'+astro['name'].replace(' ','_')).read().decode()
        first_image = urlopen('https:'+re.findall('src="(//upload.wikimedia.org/wikipedia.+?\.jpg)"',wiki_page)[0]).read()
        __executor__.call('send_file',{astro['name']+'.jpg':first_image})
    except:
        try:
            gender = json.loads(urlopen('https://api.genderize.io/?name='+astro['name'].split(' ')[0]).read())["gender"]
            if gender == "male": emoji = ' :male-astronaut:'
            else: emoji = ' :female-astronaut:'
        except:
            emoji = ''
        print(astro['name'] + emoji)
