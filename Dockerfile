# set base image (host OS)
FROM python:3.8 AS client

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY app/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app/src/ .

# python file to connect to node server and collect 3D Object file and camera data file

RUN python -u get_files.py



FROM nytimes/blender:latest AS blender
COPY ./blender-gen-container /workspace/blender_gen_TUBerlin
WORKDIR /workspace/blender_gen_TUBerlin
COPY --from=client /code/parameters.json .
COPY --from=client /code/object.ply ./models

RUN blender --background --python main.py

FROM pytorch/pytorch:latest
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx
RUN pip install opencv-python scipy argparse urllib3 numpy

COPY ./Industrial6DPoseEstimation /workspace/SSPE_TUBerlin
WORKDIR /workspace/SSPE_TUBerlin

COPY --from=blender /workspace/blender_gen_TUBerlin/DATASET ./DATASET
COPY --from=blender /workspace/blender_gen_TUBerlin/cfg ./cfg
COPY --from=blender /workspace/blender_gen_TUBerlin/config.py .
COPY --from=blender /workspace/blender_gen_TUBerlin/models/object.ply ./DATASET/object

RUN python3 create_meta_data.py
ENTRYPOINT [ "python3", "blender_train.py", "cfg/object.data", "yolo-pose.cfg", "backup/init.weights" ]
#ENTRYPOINT ["python3", "train.py"]
#RUN python3 blender_train.py blender_3dbox.data yolo-pose.cfg backup/init.weights