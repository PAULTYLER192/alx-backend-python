import os
import mysql.connector
import csv
import uuid
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE')
}

def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_database(connection):
    """Creates the ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

def create_table(connection):
    """Creates the user_data table if it does not exist with required fields."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                age DECIMAL(5,2) NOT NULL,
                INDEX (user_id)
            )
        """)
        cursor.close()
        print("Table user_data created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, data):
    """Inserts data into the database if it does not exist."""
    try:
        cursor = connection.cursor()
        # Check if data already exists
        cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (data[0],))
        if cursor.fetchone() is None:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, data)
            connection.commit()
            print(f"Inserted data for user_id: {data[0]}")
        else:
            print(f"Data for user_id: {data[0]} already exists, skipping.")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")

def stream_users(connection):
    """Generator to stream rows from user_data table one by one."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        for row in cursor:
            yield row
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error streaming data: {err}")

# Main execution
if __name__ == "__main__":
    # Connect to MySQL server
    db_connection = connect_db()
    if db_connection:
        # Create database
        create_database(db_connection)
        db_connection.close()

        # Connect to ALX_prodev
        prodev_connection = connect_to_prodev()
        if prodev_connection:
            # Create table
            create_table(prodev_connection)

            # Insert data from user_data.csv
            with open('user_data.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row if present
                for row in reader:
                    # Ensure user_id is a UUID string if not already
                    if not row[0] or row[0].strip() == "":
                        row[0] = str(uuid.uuid4())
                    insert_data(prodev_connection, row)

            # Test the generator
            print("Streaming users:")
            for user in stream_users(prodev_connection):
                print(f"User: {user}")

            prodev_connection.close()