import sqlite3

# Connecting to or create the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Creating users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age REAL NOT NULL
    )
''')
conn.commit()
print("Users table created successfully.")

# Closing the connection
conn.close()