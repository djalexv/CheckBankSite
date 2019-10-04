import requests

r = requests.get('https://alfabank.ru/' )
print(r.status_code)
