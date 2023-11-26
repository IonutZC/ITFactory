import requests
respons = requests.get('https://google.ro')
print(respons.status_code)
print((respons.content))
