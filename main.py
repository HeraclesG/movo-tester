import json
import time
import websocket
import math
import requests

# Define the car's initial position and parameters
lat = 36.729433888888884
lon = 3.029525
speed = 20
course = 0
step = 0.1  # Adjust this value to control the speed of the car

def update_position():
    global lat, lon, speed, course, step

    # Update the position based on the current speed and course
    lat += math.sin(math.radians(course)) * speed * 0.001
    lon += math.cos(math.radians(course)) * speed * 0.001

    # Increase the speed up to a maximum
    # speed = speed + 0.001
    # if speed > 30:
    #     speed = 0

    # Gradually change the course
    course = (course + 0.1) % 360

    return {
        "id": 123456789012346,  # Replace with your device ID
        "time": int(time.time() * 1000),
        "lat": lat,
        "lon": lon,
        "speed": speed,
        "course": course,
        "altitude": 100.0,
        "accuracy": 5.0,
        "battery": 80.0
    }

def main():
   while True:
    # Send the POST request
    # url = "http://134.122.96.221:5055"
    # url = "http://movoauto.com:5055"
    url = "http://127.0.0.1:5055"
    position_data = update_position()
    response = requests.post(url, data=position_data)

    # Check the response status code
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    # Wait for 1 second before sending the next request
    time.sleep(5)

if __name__ == "__main__":
    main()