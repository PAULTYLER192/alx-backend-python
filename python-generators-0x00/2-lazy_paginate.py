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

def paginate_users(page_size, offset):
    """Helper function to fetch a page of users from user_data table."""
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error paginating data: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

def lazy_paginate(page_size):
    """Generator to lazily load paginated data from user_data table."""
    offset = 0
    while True:
        # Fetch the next page
        page = paginate_users(page_size, offset)
        if not page:
            return None  # Signal end of data with return
        yield page
        offset += page_size

if __name__ == "__main__":
    # Test the generator with a page size of 2
    page_size = 2
    print(f"Lazy loading users in pages of {page_size}:")
    for page in lazy_paginate(page_size):
        if page is not None:
            print(f"Page: {page}")
        else:
            print("End of data stream.")