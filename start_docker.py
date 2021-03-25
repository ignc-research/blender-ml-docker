import subprocess
import requests

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
#sudo docker build --network host --no-cache -t train-assist . && 
#sudo docker run --gpus all -it --rm train-assist
docker_build = subprocess.run(["docker", "build", "--network", "host", "--no-cache", "-t", "train-assist", "."])
docker_run = subprocess.run(["docker", "run", "--gpus", "all", "-it", "--rm", "train-assist"])


