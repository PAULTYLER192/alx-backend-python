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
- **Status**: In progress.
- **Dependencies**: Requires `mysql-connector-python` and `python-dotenv` (install with `pip install mysql-connector-python python-dotenv`).
- **Setup**:
  - Ensure `.env` is configured with MySQL credentials.
  - Run with `python 0-stream_users.py` after database setup.
- **Notes**: Assumes the `user_data` table is populated via `seed.py`.