import requests

# URL-ul de bază pentru JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# ID-ul utilizatorului pentru care vom face filtrarea
user_id = 1

# Facem un request pentru a obține lista de todos neîncheiate (completed = false) pentru utilizatorul ales
response = requests.get(f"{base_url}/todos", params={"userId": user_id, "completed": "false"})

# Verificăm dacă requestul a fost cu succes
if response.status_code == 200:
    todos = response.json()

    # Afișăm lista de todos neîncheiate
    print("Lista de 'todos' neîncheiate pentru utilizatorul ales:")
    for todo in todos:
        print(f"ID: {todo['id']}\nTitle: {todo['title']}\n")
else:
    print("Failed to fetch todos")
