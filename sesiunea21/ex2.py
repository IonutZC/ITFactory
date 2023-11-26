import requests

# URL-ul de bază pentru JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Alegem un post și un album, de exemplu cele cu ID-ul 1
post_id = 1
album_id = 1

# Facem un request pentru a obține comentariile postului ales
response_comments = requests.get(f"{base_url}/posts/{post_id}/comments")

# Verificăm dacă requestul pentru comentarii a fost cu succes
if response_comments.status_code == 200:
    comments = response_comments.json()

    # Afișăm comentariile
    print("Comentarii pentru postul ales:")
    for comment in comments:
        print(f"Name: {comment['name']}\nEmail: {comment['email']}\nBody: {comment['body']}\n")
else:
    print("Failed to fetch comments")

# Facem un request pentru a obține fotografiile albumului ales
response_photos = requests.get(f"{base_url}/albums/{album_id}/photos")

# Verificăm dacă requestul pentru fotografii a fost cu succes
if response_photos.status_code == 200:
    photos = response_photos.json()

    # Afișăm fotografiile
    print("Fotografii pentru albumul ales:")
    for photo in photos:
        print(f"Title: {photo['title']}\nURL: {photo['url']}\n")
else:
    print("Failed to fetch photos")
