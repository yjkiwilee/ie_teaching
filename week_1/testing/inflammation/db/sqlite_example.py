# Original code: Function that performs a database query
import sqlite3

def connect_to_database(db_path):
    """Return a connection to a SQLite database."""
    # connection - a live communication channel between the app and the database
    return sqlite3.connect(db_path)

def query_database(sql, conn = None):
    """Execute a query in the given database connection"""
    
    # Check if connection has been provided
    if not conn:
        raise ValueError("Database connection must be provided.")

    # cursor - used to traverse and manipulate results returned by a query
    cursor = conn.cursor()
    # we pass a string named 'sql' that contains our SQL query
    cursor.execute(sql)
    # fetchall - returns a list of tuples containing all rows of our result
    result = cursor.fetchall()
    conn.close()
    return result