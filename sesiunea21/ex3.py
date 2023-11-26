import requests

# URL-ul de bază pentru JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Datele pentru noul post
new_post_data = {
    "title": "Titlu exemplu",
    "body": "Acesta este corpul postului de exemplu.",
    "userId": 1
}

# Crearea unui post nou fără a specifica un ID
response_without_id = requests.post(f"{base_url}/posts", data=new_post_data)

# Afisăm răspunsul pentru requestul fără ID
print("Răspuns pentru crearea postului fără ID specificat:")
print(response_without_id.json())

# Acum încercăm să creăm un post nou specificând un ID
new_post_data_with_id = new_post_data.copy()
new_post_data_with_id["id"] = 101  # Alegem un ID arbitrar

# Crearea unui post nou cu ID specificat
response_with_id = requests.post(f"{base_url}/posts", data=new_post_data_with_id)

# Afisăm răspunsul pentru requestul cu ID
print("\nRăspuns pentru crearea postului cu ID specificat:")
print(response_with_id.json())
