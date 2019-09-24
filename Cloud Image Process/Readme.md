# Cloud Image Process
### app.py decodes binary data back to jpeg format.

## Connect the VSI to Cloud Object storage

### Install Packages:
```
sudo apt-get update
sudo apt-get install automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
./autogen.sh
./configure
make
sudo make install
```

### Enter Credentials:
```
nano /$HOME/.cos_creds
chmod 600 $HOME/.cos_creds
```

### Mount bucket
```
sudo s3fs hw3-s3 /mnt/hw3-s3 -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.direct.us-east.cloud-object-storage.appdomain.cloud
```

### Run app.py
```
python3 /usr/src/app/app.py
```

### Output:
```
root@44b5fd8448a3:/# python3 /usr/src/app/app.py
Connected with result code 0
topic/hw3
```
