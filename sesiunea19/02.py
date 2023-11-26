"""
Interactiunea cu tabelul users
"""

# CRUD operations/methods
# CREATE
# READ
# UPDATE
# DELETE

import sqlite3
connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CREATE
# user 1
# are completate doar campurile obligatorii
cursor.execute(
    """
    INSERT INTO users (username, email, password, first_name, last_name)
    VALUES ('georgef12', 'george@email.com', 'pass123456', 'George', 'Fluture' )
    """
)

connection.commit()

# user 2
# are completate toate campurile (inclusiv cele optionale)
# adaugam valori intr-un mod dinamic
user_query = """
    INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

cursor.execute(user_query, ('alinapopa', 'alina@gmail.com', 'alina111', 'Alina', 'Popa',
              'str. trandafirilor nr.34', 'Brasov', '356745', 'Romania'))
connection.commit()

# user 3 si user 4
#adaugarea mai multor inregistrari in tabelul users deodata
user_query_3_4 = """
    INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
users_to_create_list = [
    ('paulamarc', 'paulamarc@gmail.com', 'paula222', 'Paula', 'Marc',
      'str. 1 mai, bl. 23, ap. 21', 'Deva', '330125', 'Romania'),
    ('bobdavid', 'david_bob@yahoo.com', '123456', 'David', 'Bob',
      'str. florilor, nr.45', 'Iasi', '254433', 'Romania')]

cursor.executemany(user_query_3_4, users_to_create_list)
connection.commit()

# READ / GET ALL USERS
cursor.execute("""SELECT * FROM users;""")

users = cursor.fetchall()
# print(users)
#
# for user in users:
#     print(user)

# READ/ GET USER BY ID
get_by_id_query = """ SELECT * FROM users WHERE id = ?;"""
cursor.execute(get_by_id_query, (1,))

user = cursor.fetchone()
print(user)
print(user[1])


# GET USER BY username
get_user_by_username = """ SELECT * FROM users WHERE username = ?;"""
cursor.execute(get_user_by_username, ('criss123',))

username = cursor.fetchone()
print(username)

# UPDATE USER
# schimbam username-ul si email-ul pentru user-ul cu id-ul 1
cursor.execute(
    """
    UPDATE users SET last_name='Marcu'
    WHERE id = 1;
    """
)
connection.commit()

# DELETE USER
cursor.execute(
    """
    DELETE FROM users
    WHERE id = 2;
    """
)
connection.commit()