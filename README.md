# blender-ml-docker
## How to run:
This docker container can be run in one of two ways. Variant 1 is used when the container needs to be run automatically without user input and Variant 2 can be used for debugging purposes. Regardless of what Variant is used, the container needs both the Frontend (Available at ignc-research/blender-ml-web) and the Node Server (Available at ignc-research/blender-ml-server) to function.

#### Note that the server must be up and running before either of the FE or BE in order to ensure complete connectivity.

### Variant 1:
Use the **start_docker.py** file to build and run the container. The user does not need to do anything further when running this variant.

### Variant 2:
Use the following command to build the container:
```
sudo docker build –network host –no-cache -t train-assist .
```
Optionally, the argument `--build-arg TRAINREPO=./mmdetect ` can be added to the build command, to change the training repository from the default of SSPE to MMDetect. This also requires a compatible version of the MMDetect directory to be added to the root folder.

Finally, the following command is used to run the container:
```
sudo docker run –gpus all –rm train-assist
```
This will start the training process and end once training has been stopped or finished.
