import requests
import shutil
import time
import json

print('Trying to connect to server...')
while True:
    try:
        r = requests.post('http://127.0.0.1:3001/log', data = {'msg': 'Establishing Connection!'})
        if r.status_code == 200:
            print('Connection established!')
            break
        else:
            time.sleep(1)
            pass
    except Exception as e:
        print('Unable to establish connection to server! Please see error message below for more details.')
        print(e)
        time.sleep(5)
        pass

print('Waiting for Data check')
while True:
    try:
        r = requests.get('http://127.0.0.1:3001/datatrigger', stream=True)
        bool_trigger = r.raw.read(1)
        if r.status_code == 200:
            if str(bool_trigger, 'utf-8') == 't':
                print('All files uploaded!')
                break
            else:
                pass
    except Exception as e:
        print(e)
        time.sleep(5)
        pass
    
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

print('Waiting for Render Trigger')
while True:
    r = requests.get('http://127.0.0.1:3001/startrender', stream=True)
    bool_trigger = r.raw.read(1)
    if r.status_code == 200:
        if str(bool_trigger, 'utf-8') == 't':
            print('Start Blender-Gen!')
            break
        else:
            pass

