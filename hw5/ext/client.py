import requests

url = "http://localhost:9696/score"
client = {"job": "student", "duration": 280, "poutcome": "failure"}


result = requests.post(url, json=client).json()

print(result)