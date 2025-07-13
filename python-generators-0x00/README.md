# ALX_prodev Database Scripts

This directory contains Python scripts for managing the ALX_prodev MySQL database.

## Task 1: Getting Started with Python Generators
- **Objective**: Create a generator that streams rows from an SQL database one by one.
- **Files**:
  - `seed.py`: Python script to set up the database, populate it, and stream rows.
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
- **Status**: In progress.
- **Dependencies**: Requires `mysql-connector-python` (install with `pip install mysql-connector-python`).
- **Notes**: Update `DB_CONFIG['password']` in `seed.py` with your MySQL root password. Ensure `user_data.csv` is present with columns: `user_id,name,email,age`.