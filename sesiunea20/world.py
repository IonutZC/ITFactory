import sqlite3
connection = sqlite3.connect("world.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS continents(
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code TEXT NOT NULL
    );
    """
)
'''
AF
NA
OC
AN
AS
EU
SA
'''
cursor.execute(
    """
       INSERT INTO continents(continent_name , continent_code)
       VALUES ('Africa', 'AF'),
       ('Europe', 'EU'),
       ('North America', 'NA'),
       ('South America', 'SA'),
       ('Antartica', 'AT'),
       ('Australia', 'OC'),
       ('Asia', 'AS');
       """
)
connection.commit()
connection.close()