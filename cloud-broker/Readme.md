# Cloud Broker

## ssh into IBM cloud device: VM running Ubuntu
```
ssh root@169.62.6.72
```

## Spin up an Alpine container.
#### Accepts all connections on port 5000
#### Docker Network: hw3-network-tx2

```
docker run -ti --rm --name cloud-broker -p 0.0.0.0:5000:1883 --network hw3-network-tx2  alpine ash
```

### Cloud broker
```
apk add mosquitto
apk add mosquitto-clients
apk add nano
mosquitto -v
```


