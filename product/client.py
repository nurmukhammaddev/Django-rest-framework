import requests

url = 'http://127.0.0.1:8000/api/'
params={"q": "smth"}
payload = {"username": 'nurmuhammad', 'password': '3030'}

respond = requests.get(url, params=params, json=payload)
print(respond.json())
