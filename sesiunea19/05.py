"""Join-uri:

Join-urile sunt comenzi SQL prin care putem combina/ lua simultan
datele din doua sau mai multe tabele, pe baza coloanei de legatura
(foreign key).

Tipuri de JOIN-uri:

1. INNER JOIN:
- obtinem inregistrarile care fac match la valori din ambele tabele.

2. LEFT (OUTER) JOIN:
- obtinem toate inregistrarile din tabelul din stanga +
inregistrarile din tabelul din dreapta care fac match

3. RIGHT (OUTER) JOIN:
- obtinem toate inregistrarile din tabelul din dreapta +
inregistrarile din tabelul din stanga care fac match

4. FULL (OUTER) JOIN:
- se returneaza toate inregsitrarile din ambele tabele, cand se
face match fie in tabelul din stanga, fie in tabelul din dreapta"""

import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

#ex de inner join
query = """
SELECT orders.id , users.username
FROM orders
INNER JOIN users ON orders.customer_id == users.id;
"""

cursor.execute(query)
print(cursor.fetchall())

#ex de left join
query = """
SELECT orders.id , orders.order_date, users.username, users.email
FROM users
LEFT JOIN orders ON orders.customer_id == users.id;
"""
cursor.execute(query)
print(cursor.fetchall())

# #ex de right join
query = """
SELECT orders.id , orders.order_date, users.username, users.email
FROM orders
LEFT JOIN users ON orders.customer_id == users.id;
"""
cursor.execute(query)
print(cursor.fetchall())
