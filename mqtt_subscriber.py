import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    temp = payload['temperature']
    humidity = payload['humidity']
    print(f"Temp: {temp}°C | Humidity: {humidity}%")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("home/sensors")
client.on_message = on_message
client.loop_forever()
