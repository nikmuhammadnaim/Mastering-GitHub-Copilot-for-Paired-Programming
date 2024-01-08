import requests
import json

# Send a POST request to the /checksum endpoint
response = requests.post(
    "http://localhost:8000/checksum",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"text": "Hello, world! My name is Nik Muhammad Naim."})
)
print(response.json())

# Send a POST request to the /generate endpoint
response = requests.post(
    "http://localhost:8000/generate",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"length": 30})
)
print(response.json())
