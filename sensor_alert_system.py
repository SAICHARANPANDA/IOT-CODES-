import sqlite3
import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt

dht = adafruit_dht.DHT11(board.D4)
db = sqlite3.connect('sensor_data.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS readings (timestamp TEXT, temperature REAL, humidity REAL)')
db.commit()

mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

threshold_temp = 30

while True:
    try:
        temp = dht.temperature
        humidity = dht.humidity
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO readings VALUES (?, ?, ?)', (timestamp, temp, humidity))
        db.commit()
        if temp > threshold_temp:
            mqtt_client.publish("home/alerts", f"Temperature Alert! {temp}C at {timestamp}")
        time.sleep(10)
    except Exception:
        continue
