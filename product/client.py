import requests

url = 'http://127.0.0.1:8000/api/'
respond = requests.get(url, params={"q": "smth"}, json={"username": "admin", "password": "3030"})
print(respond.json())
