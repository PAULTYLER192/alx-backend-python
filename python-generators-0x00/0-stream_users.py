import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration from .env
DB_CONFIG = {
    'host': os.getenv('DB_HOST', ''),
    'user': os.getenv('DB_USER', ''),
    'password': os.getenv('DB_PASSWORD', ''),  # Must be set in .env
    'database': os.getenv('DB_DATABASE', '')
}

def stream_users():
    """Generator to stream rows from user_data table one by one."""
    connection = None
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        # Yield rows one by one (single loop)
        for row in cursor:
            yield row
        
    except mysql.connector.Error as err:
        print(f"Error streaming data: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Test the generator
    print("Streaming users:")
    for user in stream_users():
        print(f"User: {user}")