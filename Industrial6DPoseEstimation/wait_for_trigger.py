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

print('Waiting for Training Trigger')
while True:
    try:
        r = requests.get('http://127.0.0.1:3001/starttrain', stream=True)
        bool_trigger = r.raw.read(1)
        if r.status_code == 200:
            if str(bool_trigger, 'utf-8') == 't':
                print('Start SSPE!')
                break
            else:
                pass
    except Exception as e:
        print('Unable to establish connection to server! Please see error message below for more details.')
        print(e)
        time.sleep(5)
        pass