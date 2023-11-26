import sqlite3
connection = sqlite3.connect("world.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS countries(
    country_code VARCHAR(2) PRIMARY KEY,
    country_name VARCHAR (50) NOT NULL,
    country_id INT NOT NULL,
    population INT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES continents (continent_id)
    );
    """
)
# cursor.execute(
#     """
#     INSERT INTO countries(country_code, country_name, country_id, population)
#     VALUES('FE', 'Romania', 2,  19054854848 ),
#     ('RO', 'Oomania', 3,  29054854848 ),
#     ('US', 'Rmania', 2,  79054854848 ),
#     ('FR', 'Roania', 2,  69054854848 ),
#     ('GE', 'Romani', 3,  39054854848 ),
#     ('MD', 'Rmania', 5,  59054854848 ),
#     ('MN', 'Romnia', 2,  99054854848 ),
#     ('OP', 'Romana', 1,  49054854848 ),
#     ('RT', 'Romaia', 7,  29054854848 ),
#     ('GB', 'Romnia', 4,  39054854848 ),
#     ('LN', 'Roania', 2,  45058581816 );
#      """
# )
# connection.commit()
cursor.execute(
    """
    SELECT * FROM  countries ORDER BY country_name
    """
)
countris2323 = cursor.fetchall()
print(countris2323)

cursor.execute(
    """
    SELECT COUNT(*) FROM countries
    """
)
countries_count = cursor.fetchone()
print(countries_count)

cursor.execute(
    """
   SELECT * FROM  countries WHERE population > 50000000000
   """
)

pop_contry = cursor.fetchall()
print(pop_contry)

cursor.execute(
    """
    SELECT country_name FROM countries WHERE country_name LIKE "O%"
    """
)
filtred_counties = cursor.fetchall()
print(filtred_counties)


cursor.execute(
    """
    SELECT continents.continent_name , SUM(countries.population) AS total_population
    FROM  countries  
    JOIN  continents ON countries.country_id = continents.continent_id
    GROUP BY continents.continent_name
    """
)

countries_cnt = cursor.fetchall()
print(countries_cnt)

cursor.close()
