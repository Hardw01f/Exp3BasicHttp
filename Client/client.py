import requests

r = requests.get('http://13.230.219.38/hi')
print(r.text)