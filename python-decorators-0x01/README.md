# ALX Backend Python

This repository contains Python scripts for various backend tasks, including database operations and decorators.

## Directory: python-decorators-0x01

### Task 0: Logging Database Queries
- **Objective**: Create a decorator that logs database queries executed by any function.
- **Files**:
  - `0-log_queries.py`: Python script with a decorator to log SQL queries.
- **Instructions**:
  - Complete the code by writing a decorator `log_queries` that logs the SQL query before executing it.
  - Prototype: `def log_queries()`
  - Use `sqlite3` and `functools` imports.
- **Prototype**:
  - `def log_queries()`
- **Status**: Completed.
- **Dependencies**: Requires `sqlite3` (included with Python).
- **Setup**:
  - Ensure `users.db` exists with a `users` table (e.g., columns: `id`, `name`, `email`, `age`).
  - Run with `python 0-log_queries.py` after setup.
- **Notes**: Logs queries with timestamps to the console. Assumes the query is passed as the first argument or keyword `query`.

### Task 1: Handle Database Connections with a Decorator
- **Objective**: Create a decorator that automatically handles opening and closing database connections.
- **Files**:
  - `1-with_db_connection.py`: Python script with a decorator to manage database connections.
- **Instructions**:
  - Implement a decorator `with_db_connection` that opens a database connection, passes it to the function, and closes it afterward.
  - Prototype: `def with_db_connection()`
  - Use `sqlite3` and `functools` imports.
- **Prototype**:
  - `def with_db_connection()`
- **Status**: Completed.
- **Dependencies**: Requires `sqlite3` (included with Python).
- **Setup**:
  - Ensure `users.db` exists with a `users` table (e.g., columns: `id`, `name`, `email`, `age`).
  - Run with `python 1-with_db_connection.py` after setup.
- **Notes**: Automates connection handling with commit/rollback and error handling.

### Task 2: Transaction Management Decorator
- **Objective**: Create a decorator that manages database transactions by automatically committing or rolling back changes.
- **Files**:
  - `2-transactional.py`: Python script with a decorator to manage transactions.
- **Instructions**:
  - Implement a decorator `transactional(func)` that ensures a function running a database operation is wrapped inside a transaction. If the function raises an error, rollback; otherwise commit the transaction.
  - Copy the `with_db_connection` decorator from Task 1 into the script.
  - Use `sqlite3` and `functools` imports.
- **Prototype**:
  - `def transactional()`
- **Status**: In progress.
- **Dependencies**: Requires `sqlite3` (included with Python).
- **Setup**:
  - Ensure `users.db` exists with a `users` table (e.g., columns: `id`, `name`, `email`, `age`).
  - Run with `python 2-transactional.py` after setup.
- **Notes**: Ensures data consistency with commit/rollback, stacked with connection handling.
- 

### Task 3: Retry Database Queries
- **Objective**: Create a decorator that retries database operations if they fail due to transient errors.
- **Files**:
  - `3-retry_on_failure.py`: Python script with a decorator to retry failed operations.
- **Instructions**:
  - Implement a `retry_on_failure(retries=3, delay=2)` decorator that retries the function a certain number of times if it raises an exception.
  - Paste the `with_db_connection` decorator from Task 1.
  - Use `time`, `sqlite3`, and `functools` imports.
- **Prototype**:
  - `def retry_on_failure(retries=3, delay=2)`
- **Status**: In progress.
- **Dependencies**: Requires `sqlite3` and `time` (included with Python).
- **Setup**:
  - Ensure `users.db` exists with a `users` table (e.g., columns: `id`, `name`, `email`, `age`).
  - Run with `python 3-retry_on_failure.py` after setup.
- **Notes**: Retries up to 3 times with a 1-second delay (as specified) on transient errors like database locks.