import requests

url = "http://localhost:9696/score"
client = {"job": "management", "duration": 400, "poutcome": "success"}

result = requests.post(url, json=client).json()

print(result)