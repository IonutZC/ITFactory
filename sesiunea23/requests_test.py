import requests



response = requests.get('http://127.0.0.1:8000').json()
print(response)


response = requests.post('http://127.0.0.1:8000/add/', json={
    "name":"name_2",
    "description":"description"
})


response = requests.get('http://127.0.0.1:8000').json()
print(response)