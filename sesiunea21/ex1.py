import requests

# URL-ul de bază pentru JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Alegem un utilizator, de exemplu utilizatorul cu ID-ul 1
user_id = 1

# Facem un request pentru a obține postările utilizatorului cu ID-ul ales

response = requests.get(f"{base_url}/posts", params={"userId": user_id})

# Verificăm dacă requestul a fost cu succes
if response.status_code == 200:
    posts = response.json()

    # Afișăm primele 3 postări
    for post in posts[:3]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")

    # Calculăm și afișăm numărul de postări rămase
    remaining_posts = len(posts) - 3
    if remaining_posts > 0:
        print(f"+{remaining_posts} more posts")
else:
    print("Failed to fetch posts")
