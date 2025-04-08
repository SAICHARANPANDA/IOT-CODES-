import random

class TrafficSensor:
    def get_traffic_data(self):
        return random.randint(0, 50)

class TrafficLightController:
    def control_traffic_light(self, cars):
        if cars > 30:
            print(f"High Traffic Detected: {cars} Cars")
            print("Action: Green Light Extended for 60 seconds\n")
        elif cars > 10:
            print(f"Moderate Traffic: {cars} Cars")
            print("Action: Green Light for 30 seconds\n")
        else:
            print(f"Low Traffic: {cars} Cars")
            print("Action: Red Light Activated\n")

def main():
    sensor = TrafficSensor()
    controller = TrafficLightController()

    print("=-=-=-= Smart Traffic Control System =-=-=-=")

    while True:
        try:
            choice = int(input("Press 1 to read traffic data | Press 0 to exit: "))
        except ValueError:
            print("Invalid input. Please enter 0 or 1.\n")
            continue

        if choice == 0:
            print("System Stopped.")
            break
        elif choice == 1:
            cars_detected = sensor.get_traffic_data()
            controller.control_traffic_light(cars_detected)
        else:
            print("Invalid option. Please press 0 or 1.\n")

if __name__ == "__main__":
    main()
