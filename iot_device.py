import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import json

dht = adafruit_dht.DHT11(board.D4)
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

while True:
    try:
        temp = dht.temperature
        humidity = dht.humidity
        data = {"temperature": temp, "humidity": humidity, "device": "sensor1"}
        mqtt_client.publish("home/sensors", json.dumps(data))
        time.sleep(10)
    except:
        continue
