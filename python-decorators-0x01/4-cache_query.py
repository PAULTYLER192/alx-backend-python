import time
import sqlite3 
import functools


query_cache = {}

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

def cache_query(func):
    """Decorator to cache query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = args[0] if args else kwargs.get('query', '')
        if query in query_cache:
            print(f"Using cached result for query: {query}")
            return query_cache[query]
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print(f"Caching result for query: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")