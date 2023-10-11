import requests

url = "http://127.0.0.1:5000/lectures/"

lecture_data = {
    "title": "Physics 101",
    "lecturer_name": "Dr. Smith",
    "start_time": "10:00",
    "end_time": "11:00",
    "room": "Room 102"
}

response = requests.get(url, json=lecture_data)

print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

try:
    print("JSON Response: ", response.json())
except requests.exceptions.JSONDecodeError:
    print("No JSON received")
