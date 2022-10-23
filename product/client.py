import requests

url = 'http://127.0.0.1:8000/api/'
params={"q": "smth"}
payload = {"title": 'Product 1', "description": 'smth', "price": 211.60}

# respond = requests.get(url, params=params, json=payload),
respond = requests.get(url, json=payload)
print(respond.json())
