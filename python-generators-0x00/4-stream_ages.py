import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration from .env
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),  # Must be set in .env
    'database': os.getenv('DB_DATABASE', 'ALX_prodev')
}

def stream_user_ages():
    """Generator to yield user ages one by one from user_data table."""
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield float(row[0])  # Yield age as float
    except mysql.connector.Error as err:
        print(f"Error streaming ages: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

def calculate_average_age():
    """Calculate average age using the generator without loading all data into memory."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age}")
    else:
        print("Average age of users: N/A")

if __name__ == "__main__":
    calculate_average_age()