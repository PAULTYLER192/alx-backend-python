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

def stream_users_in_batches(batch_size):
    """Generator to fetch rows from user_data table in batches."""
    connection = None
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        # Fetch and yield batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
        
    except mysql.connector.Error as err:
        print(f"Error streaming data: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

def batch_processing(batch_size):
    """Generator to process batches and filter users over 25."""
    # Single loop over the batch generator
    for batch in stream_users_in_batches(batch_size):
        # Single loop to filter within each batch
        filtered_batch = [user for user in batch if float(user[3]) > 25]  # age is at index 3
        if filtered_batch:
            yield filtered_batch
        
    # Total loops: 1 (outer) + 1 (list comprehension) = 2

if __name__ == "__main__":
    # Test the functions with a batch size of 2
    batch_size = 2
    print(f"Processing users in batches of {batch_size}:")
    for batch in batch_processing(batch_size):
        print(f"Batch of users over 25: {batch}")