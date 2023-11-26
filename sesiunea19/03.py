"""
Interactiunea cu tabelul products
"""

# CRUD operations/methods
# CREATE
# READ
# UPDATE
# DELETE

import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE PRODUCT
product_query = """
    INSERT INTO products (name, category, price, stock_count, description)
    VALUES (?, ?, ?, ?, ?);
"""
products = [
    ("birou negru", "mobilier", 120, 2, "birou negru descriere"),
    ("pitic de gradina", "gradina", 56.99, 5, "pitic gradina descriere"),
    ("ghiveci flori alb", "gradina", 25.45, 10, "ghiveci flori descriere")
]
cursor.executemany(product_query, products)
connection.commit()

# READ PRODUCT (BY ID)
get_product_by_id_query = """
    SELECT * FROM products
    WHERE id = ?;
"""

cursor.execute(get_product_by_id_query, (1,))
product = cursor.fetchone()

# READ/GET ALL PRODUCTS
cursor.execute("""
    SELECT name, category, price FROM products;
""")

products_list = cursor.fetchall()
print(products)

for product in products:
    print(product)


# UPDATE PRODUCT
cursor.execute("""
    UPDATE products SET name='birou alb'
    WHERE id = 1;
""")



connection.commit()