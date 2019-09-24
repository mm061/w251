FROM ubuntu

# build this: e.g docker build -t mqtt-cv .
# to run this container, do:
# on the host:
# make sure you're in the X environment
# xhost + 
# docker run --rm --privileged -e DISPLAY -v /tmp:/tmp -ti mqtt-cv bash

RUN apt update

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install -y python-opencv python-pip vim-tiny mosquitto-clients libopencv-dev
RUN pip install paho-mqtt
RUN pip install numpy

WORKDIR /

COPY app.py /usr/src/app/

CMD ["python","/usr/src/app/app.py"]
