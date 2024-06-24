##3 To download type python3 -m install mysql-connector-python

import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert data into the table
c.execute('''
INSERT INTO users (name, email) VALUES (?, ?)
''', ('John Doe', 'john.doe@example.com'))

c.execute('''
INSERT INTO users (name, email) VALUES (?, ?)
''', ('Jane Smith', 'jane.smith@example.com'))

# Commit the changes and close the connection
conn.commit()
conn.close()