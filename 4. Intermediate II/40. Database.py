# SQLite browser can be downloaded for free from, https://sqlitebrowser.org/dl/

# Import the library
import sqlite3 as sl

# Create a connection to new database
connection = sl.connect("training.db")

with connection:    # Alternative way to open and close
    # Execute the following db command
    connection.execute("""
        CREATE TABLE COMPANY (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            zipcode INTEGER
        );
    """)
    # Remember to check that the query is enclosed with docstring three double quotes

# Alternate way to create query and pass parameters
sql = 'INSERT INTO COMPANY (id, name, zipcode) values(?, ?, ?)'
data = [
    (1, 'SiriSarah LLC', 84054),
    (2, 'Alphabet', 94043),
    (3, 'Meta', 94025)
]

with connection:
    connection.executemany(sql, data)

with connection:
    data = connection.execute("SELECT * FROM COMPANY WHERE zipcode == 84054")
    for row in data:
        print(row)