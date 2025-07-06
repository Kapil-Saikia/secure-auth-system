import requests

url = "http://127.0.0.1:5000/register"

data = {
    "username": "kapil",
    "email": "kapil@example.com",
    "password": "secure123"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
