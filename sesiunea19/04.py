"""
Interactiunea cu tabelul orders
"""

# CRUD operations/methods
# CREATE
# READ
# UPDATE
# DELETE
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE ORDER

# pentru a crea o comanda completa, avem nevoie de
# un order, iar apoi avem nevoie de order items,
# care includ produsele/caracteristicile produselor

# 1. cream o comanda
order_query = """
    INSERT INTO orders (customer_id, order_date)
    VALUES (3, '16.10.2023');
"""
cursor.execute(order_query)
connection.commit()

# # 2. adaugam linii de comanda
order_items_query = """
    INSERT INTO order_items (order_id, product_id, quantity, total_price)
    VALUES (?, ?, ?, ?);
"""
order_items = [
    (2, 2, 1, 120),
    (2, 1, 2, 51)
]
cursor.executemany(order_items_query, order_items)
connection.commit()


# # READ/GET ORDER BY ID
get_order_by_id_and_items_query = """
SELECT orders.id, orders.customer_id, orders.order_date, order_items.product_id, order_items.quantity, order_items.total_price
FROM orders
LEFT JOIN order_items ON orders.id = order_items.order_id
WHERE orders.id = ?;
"""

cursor.execute(get_order_by_id_and_items_query, (1,))
order_and_items = cursor.fetchall()
print(order_and_items)

for row in order_and_items:
    print(row)
    order_id, customer_id, order_date, product_id, quantity, total_price = row
    print(f"Order ID: {order_id}, Customer ID: {customer_id}, Order Date: {order_date}")
    print(f"Product ID: {product_id}, Quantity: {quantity}, Total Price: {total_price}")

# # READ/GET ALL ORDERS
cursor.execute("""
SELECT id, customer_id, order_date FROM orders;
""")

orders = cursor.fetchall()
print(orders)

for order in orders:
    print(order)
print(f'No Orders {len(orders)}')

# UPDATE ORDER
update_quantity_query = """
UPDATE order_items SET quantity= ? WHERE order_id= ? AND product_id = ?;
"""
new_quantity = 23
order_id = 1
product_id = 2

cursor.execute(update_quantity_query, (new_quantity, order_id, product_id,))
connection.commit()

# # DELETE ORDER
#
delete_order_query = """ DELETE FROM orders WHERE id= ?;"""
cursor.executemany(delete_order_query, [(4,), (5,), (6,), (7,)])
connection.commit()