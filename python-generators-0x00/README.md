# ALX_prodev Database Scripts

This directory contains Python scripts for managing the ALX_prodev MySQL database with a focus on Python generators.

## Task 1: Getting Started with Python Generators
- **Objective**: Create a generator to stream rows from an SQL database.
- **Files**:
  - `seed.py`: Python script to set up the database, populate it, and stream rows.
  - `.env`: Stores sensitive database credentials.
  - `.gitignore`: Excludes sensitive files from version control.
- **Instructions**:
  - a) Set up the `ALX_prodev` database with a `user_data` table containing:
    - `user_id` (Primary Key, UUID, Indexed)
    - `name` (VARCHAR, NOT NULL)
    - `email` (VARCHAR, NOT NULL)
    - `age` (DECIMAL, NOT NULL)
  - b) Populate the database with sample data from `user_data.csv`.
- **Prototypes**:
  - `def connect_db()`: Connects to the MySQL database server.
  - `def create_database(connection)`: Creates the `ALX_prodev` database if it does not exist.
  - `def connect_to_prodev()`: Connects to the `ALX_prodev` database.
  - `def create_table(connection)`: Creates the `user_data` table if it does not exist.
  - `def insert_data(connection, data)`: Inserts data into the database if it does not exist.
- **Status**: Completed.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Update `.env` with your MySQL credentials (e.g., `DB_PASSWORD=your_password`).
  - Ensure `user_data.csv` is present with columns: `user_id,name,email,age`.
- **Notes**: The script assumes a local MySQL server. Run with `python seed.py` after setup.

## Task 2: Generator that Streams Rows from an SQL Database
- **Objective**: Create a generator that streams rows from an SQL database one by one.
- **Files**:
  - `0-stream_users.py`: Python script with a generator function to fetch rows from `user_data`.
- **Instructions**:
  - a) Write a function using a generator to fetch rows one by one from the `user_data` table.
  - Use the `yield` Python generator.
  - Prototype: `def stream_users()`.
  - The function should have no more than 1 loop.
- **Status**: Completed.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Ensure `.env` is configured with MySQL credentials.
  - Run with `python 0-stream_users.py` after database setup.
- **Notes**: Assumes the `user_data` table is populated via `seed.py`.

## Task 3: Batch Processing Large Data
- **Objective**: Create a generator to fetch and process data in batches from the users database.
- **Files**:
  - `1-batch_processing.py`: Python script with functions to fetch and process batches.
- **Instructions**:
  - a) Write a function `stream_users_in_batches(batch_size)` that fetches rows in batches.
  - b) Write a function `batch_processing(batch_size)` that processes each batch to filter users over the age of 25.
  - Use no more than 3 loops in your code.
  - Your script must use the `yield` generator and include a `return` statement as per review feedback.
- **Prototypes**:
  - `def stream_users_in_batches(batch_size)`
  - `def batch_processing(batch_size)`
- **Status**: Completed.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Ensure `.env` is configured with MySQL credentials.
  - Run with `python 1-batch_processing.py` after database setup.
- **Notes**: Assumes the `user_data` table is populated via `seed.py`. Filters users where `age > 25`. Uses `return None` to signal end of data stream.

## Task 4: Simulate Fetching Paginated Data from the Users Database Using a Generator to Lazily Load Each Page
- **Objective**: Simulate fetching paginated data from the users database using a generator to lazily load each page.
- **Files**:
  - `2-lazy_paginate.py`: Python script with a generator function to lazily load pages.
- **Instructions**:
  - Implement a generator function `lazy_paginate(page_size)` that implements `paginate_users(page_size, offset)` to fetch the next page when needed, starting with an offset of 0.
  - Use only one loop.
  - Include the `paginate_users` function in your code.
  - Use the `yield` generator.
- **Prototype**:
  - `def lazy_paginate(page_size)`
- **Status**: In progress.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Ensure `.env` is configured with MySQL credentials.
  - Run with `python 3-lazy_paginate.py` after database setup.
- **Notes**: Assumes the `user_data` table is populated via `seed.py`. Lazily loads pages starting at offset 0.

### Task 5: Use a Generator to Compute a Memory-Efficient Aggregate Function (Average Age) for a Large Dataset
- **Objective**: Use a generator to compute a memory-efficient aggregate function (i.e., average age) for a large dataset.
- **Files**:
  - `4-stream_ages.py`: Python script with a generator to compute average age.
- **Instructions**:
  - Implement a generator `stream_user_ages()` that yields user ages one by one.
  - Use the generator in a different function to calculate the average age without loading the entire dataset into memory.
  - Your script should print "Average age of users: average_age".
  - Use no more than two loops in your script.
  - You are not allowed to use the SQL `AVERAGE`.
- **Prototypes**:
  - Implicit: `def stream_user_ages()` and `def calculate_average_age()`
- **Status**: In progress.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Ensure `.env` is configured with MySQL credentials.
  - Run with `python 4-stream_ages.py` after database setup.
- **Notes**: Assumes the `user_data` table is populated via `seed.py`. Computes average age manually without SQL `AVG()`.