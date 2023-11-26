"""
DateBase - vom crea baza de date folosind libraria sqlite3 si
vedem baza de date cu ajutorul aplicatiei SQLITESTUDIO
"""

import sqlite3
#cream o baza de date si stabilim conexiunea catre aceasta
connection = sqlite3.connect("marketplace.db")

#pentru a executa comenzi/query-uri SQL si a interactiona cu datele din baza de db vom folosi database cursor
cursor = connection.cursor()

# CREAREA TABELELOR

# tabelul users
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
    );
    """
)

# tabelul products
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_count INTEGER DEFAULT 1,
    description TEXT
    );
    """
)


# # tabelul orders
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES users(id)
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 0,
    total_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );
    """
)

connection.commit()
connection.close()

#https://sqlitestudio.pl/ - aplicatie pt a vedea baza de date creata