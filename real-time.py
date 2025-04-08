import joblib
import random 
import time
model = joblib.load('irrigation_model.pkl')

def get_sensor_data():
    soil = random.randint(300, 800)  
    temp = random.randint(25, 40)   
    return soil, temp

def send_notification(message):
    print(f"📱 Alert: {message}")

while True:
    soil, temp = get_sensor_data()
    print(f"🌱 Soil: {soil}, 🌡 Temp: {temp}")

    prediction = model.predict([[soil, temp]])
    if prediction[0] == 1:
        send_notification("Irrigation needed! 🌧 Soil moisture is low.")
    else:
        print("✅ No irrigation needed.")

    time.sleep(10)  