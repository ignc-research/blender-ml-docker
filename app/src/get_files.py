import requests
import shutil
import time
import json

r1 = requests.get('http://127.0.0.1:3001/send3d', stream=True)
if r1.status_code == 200:
    with open('object.ply', 'wb') as f:
        for chunk in r1.iter_content(1024):
            f.write(chunk)
r11 = requests.post('http://127.0.0.1:3001/log', data = {'msg': 'Received 3D Object File!'})
print('Received 3D Object File!')

r2 = requests.get('http://127.0.0.1:3001/sendjson')
if r2.status_code == 200:
    parameters = r2.json()
    with open('parameters.json', 'w') as outfile:
        json.dump(parameters, outfile)
r21 = requests.post('http://127.0.0.1:3001/log', data = {'msg': 'Received Parameter JSON File!'})
print('Received Parameter JSON File!')

print('Waiting for Start Trigger')
while True:
    r = requests.get('http://127.0.0.1:3001/sendtrigger', stream=True)
    bool_trigger = r.raw.read(1)
    if r.status_code == 200:
        if str(bool_trigger, 'utf-8') == 't':
            print('Start Blender-Gen!')
            break
        else:
            pass

