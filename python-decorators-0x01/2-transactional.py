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

def transactional(func):
    """Decorator to manage database transactions with commit or rollback."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Transaction failed: {e}")
            raise
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Updating user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')