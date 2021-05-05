import subprocess
import requests
import time

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
print('Waiting for build command')
while True:
    try:
        r = requests.get('http://127.0.0.1:3001/dockerrequest')
        if r.status_code == 200:
            data = r.json()
            print(data["Dimensions"])
            #time.sleep(10)
            break
        else:
            time.sleep(1)
            pass
    except Exception as e:
        #print(e)
        time.sleep(5)
        pass
#sudo docker build --network host --no-cache -t train-assist . && 
#sudo docker run --gpus all -it --rm train-assist
if data["Dimensions"] == 2.5:
    print('test')
    docker_build = subprocess.run(["docker", "build", "--network", "host", "--no-cache", "-t", "train-assist", "."])
    docker_run = subprocess.run(["docker", "run", "--network", "host", "--gpus", "all", "-it", "--rm", "train-assist"])

elif data["Dimensions"] == 2:
    docker_build = subprocess.run(["docker", "build", "--build-arg", "TRAINREPO=./mmdetect", "--network", "host", "--no-cache", "-t", "train-assist", "."])
    docker_run = subprocess.run(["docker", "run", "--gpus", "all", "-it", "--rm", "train-assist"])


