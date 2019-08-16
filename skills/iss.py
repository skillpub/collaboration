'''some data about International Space Station'''
from urllib.request import urlopen
import json
import re
import random
import sys
import time
from PIL import Image

commands = sys.argv

if "location" in commands:

    data = json.loads(urlopen("http://api.open-notify.org/iss-now.json").read())['iss_position']

    print('*ISS Current Location* :earth_americas: :satellite:')
    print('https://www.google.com/maps/search/?api=1&query={},{}'.format(data['latitude'],data['longitude']))

if "people" in commands:
    
    print('*People In Space* :face_with_cowboy_hat:')
    data = json.loads(urlopen("http://api.open-notify.org/astros.json").read())
    for astro in data['people']:
        try:
            astro_name = astro['name']
            wiki_page = urlopen('https://en.wikipedia.org/wiki/'+astro['name'].replace(' ','_')).read().decode()
            first_image = urlopen('https:'+re.findall('src="(//upload.wikimedia.org/wikipedia.+?\.jpg)"',wiki_page)[0])
            image = Image.open(first_image)
            image.show()
        except:
            try:
                gender = json.loads(urlopen('https://api.genderize.io/?name='+astro['name'].split(' ')[0]).read())["gender"]
                if gender == "male": emoji = ' :male-astronaut:'
                else: emoji = ' :female-astronaut:'
            except:
                emoji = ''
            print(astro['name'] + emoji)

if "speed" in commands:
    
    from math import sin, cos, sqrt, atan2, radians
    
    if "average" in commands:
        answer = input("what time interval? (in minutes)")
        try:
            measure_interval = 60*int(answer)
        except:
            print("didn't get you")
            sys.exit()
    else:
        measure_interval = 1 # sec
    
    data = json.loads(urlopen("http://api.open-notify.org/iss-now.json").read())['iss_position']
    lat1 = radians(float(data['latitude']))
    lon1 = radians(float(data['longitude']))
    
    if measure_interval >= 60 : print("ok, I'll send you result ...")
    time.sleep(measure_interval)
    
    data = json.loads(urlopen("http://api.open-notify.org/iss-now.json").read())['iss_position']
    lat2 = radians(float(data['latitude']))
    lon2 = radians(float(data['longitude']))
    
    # approximate radius of earth in km
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    speed = distance/measure_interval
    
    print('*ISS speed* : '+str(round(speed,2)) + ' km/s')
