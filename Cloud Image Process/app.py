import paho.mqtt.client as mqtt
import base64

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("topic/hw3")

def on_message (client, userdata, msg):
  print(msg.topic)
  with open("/mnt/hw3-s3/transmitted_image.jpg","wb") as head_shot:
    head_shot.write(base64.b64decode(msg.payload))
    head_shot.close()

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message


### Cloud Broker is the name of the container running the MQTT broker on the cloud
client.connect("cloud-broker",1883,60)

client.loop_forever()

