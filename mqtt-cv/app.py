## Captures head shot and publishes it to the MQTT broker
## Press 's' to save and 'esc' to exit

import numpy as np
import cv2
import base64
import paho.mqtt.client as mqtt

cap = cv2.VideoCapture(1)


while(True):
	ret, frame = cap.read();

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,h,w) in faces:
		img = cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
		cropped_img = img[y:y+h,x:x+w]

	if len(faces) > 0:
		cv2.imshow('Press s to Save',cropped_img)
	
	k = cv2.waitKey(1);

	if k==27:
		break
	elif k == ord('s'): # use s key to save
		if len(faces) > 0:
			#cv2.imwrite('head_image.png',cropped_img)
			msg = cv2.imencode('.jpg',cropped_img)[1]
			msg_out = base64.b64encode(msg)			
			client = mqtt.Client()
			client.connect("iot-broker",1883,60)
			client.publish("topic/hw3", msg_out);
			client.disconnect();
cv2.destroyAllWindows()
