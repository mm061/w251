FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 mosquitto python3-pip sudo mosquitto-clients nano

RUN pip3 install paho-mqtt

COPY app.py /usr/src/app/

RUN sudo apt-get update
RUN sudo apt-get install -y automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git
