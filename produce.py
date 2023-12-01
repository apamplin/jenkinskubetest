import paho.mqtt.client as mqtt
import json
import random
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect('10.1.103.32', 1883, 60)
while True:
    num = random.randint(0, 100)
    payload = {
        "num": num
    }
    client.publish('test', json.dumps(payload))
    print(f"Published THE COOLEST data: {payload}")
    time.sleep(5)
