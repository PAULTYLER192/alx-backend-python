import time
import sqlite3 
import functools

def with_db_connection(func):
    """Decorator to automatically handle database connection opening and closing."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Database error: {e}")
            raise
        finally:
            conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=2):
    """Decorator to retry a function on failure due to transient errors."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(conn, *args, **kwargs)
                except sqlite3.OperationalError as e:
                    last_exception = e
                    attempt_num = attempt + 1
                    if attempt_num == retries:
                        print(f"Max retries ({retries}) reached. Last error: {e}")
                        raise
                    print(f"Attempt {attempt_num} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            raise last_exception  # Should not reach here due to max retries check
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)