import requests

# URL-ul de bază pentru JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# ID-ul postului pe care îl vom modifica
post_id = 1

# Datele pentru actualizarea postului
update_data = {
    "title": "Titlu actualizat",
    "body": "Acesta este corpul actualizat al postului.",
    "userId": 1
}

# Realizăm actualizarea folosind metoda PUT
response_put = requests.put(f"{base_url}/posts/{post_id}", data=update_data)

# Afișăm răspunsul pentru requestul PUT
print("Răspuns pentru actualizarea postului folosind PUT:")
print(response_put.json())

# Acum realizăm o actualizare parțială folosind metoda PATCH
patch_data = {
    "title": "Titlu parțial actualizat"
}

# Actualizare folosind PATCH
response_patch = requests.patch(f"{base_url}/posts/{post_id}", data=patch_data)

# Afișăm răspunsul pentru requestul PATCH
print("\nRăspuns pentru actualizarea parțială a postului folosind PATCH:")
print(response_patch.json())
