import requests

r = requests.get('http://localhost:8080/hi')
print(r.text)