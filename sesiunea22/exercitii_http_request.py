'''
Folosim Simple Books API, descris aici : https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client. Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor, client name si email ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.
'''

import requests

class BooksAPIClient:

    token = ''
    client_name = ''
    email = ''
    base_url = 'https://simple-books-api.glitch.me'
    def __init__(self, client_name, email, token = ''):
        self.client_name = client_name
        self.email = email

        if not token:
            self.token = self.authenticate()
        else:
            self.token = token

    def authenticate(self):
        url = f'{self.base_url}/api-clients'
        body = {'clientName': self.client_name, 'clientEmail': self.email}
        response = requests.post(url, json=body)
        return response.json()['accessToken']

    def get_orders(self):
        url = f'{self.base_url}/orders'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_books(self):
        url = f'{self.base_url}/books'
        response = requests.get(url)
        return response.json()

    def submit_order(self, book_id, customer_name):
        url = f'{self.base_url}/orders'
        headers = {"Authorization": f"Bearer {self.token}"}
        body = {'bookId': book_id, 'customerName': customer_name}
        response = requests.post(url, headers=headers, json=body)
        return response.json()

    def delete_order(self, order_id):
        url = f'{self.base_url}/orders/{order_id}'
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(url, headers=headers)
        return response




api_client = BooksAPIClient('george', 'email@dotrandom123.com', 'd7bac69cfcf52059858676ca6353016bec7b8f3f3796ff9cd2a03077603c5263')
# print(api_client.get_orders())
# print(api_client.get_books())
# print(api_client.submit_order(1,'george'))
print(api_client.get_orders())
print(api_client.delete_order('2O7QiOki75mlsIhB7puW7'))
print(api_client.get_orders())
