import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Insert sample data
sample_data = [
    ("Alice", "alice@example.com", 30.0),
    ("Bob", "bob@example.com", 28.0),
    ("Charlie", "charlie@example.com", 35.5)
]
cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", sample_data)
conn.commit()
print("Sample data inserted successfully.")

# Verify data (optional)
cursor.execute("SELECT * FROM users")
print("Users in table:", cursor.fetchall())

# Close the connection
conn.close()