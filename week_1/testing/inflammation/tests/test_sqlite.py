import pytest
import sqlite3
from pathlib import Path
from db.sqlite_example import connect_to_database, query_database

@pytest.fixture()
def database_connection():
    # If the database already exists, delete it
    if Path("test.db").exists():
        Path.unlink("test.db")
    # Create a new test database and enter some data
    conn = sqlite3.connect("test.db")
    
    # Return the DB connection
    return conn

@pytest.fixture()
def setup_database(database_connection):
    # Add data to database
    cur = database_connection.cursor()
    cur.execute("CREATE TABLE Animals(Name, Species, Age)")
    cur.execute("INSERT INTO Animals VALUES ('Bugs', 'Rabbit', 6)")

    # Return the connection
    yield database_connection

    # Remove the database
    cur.execute("DROP TABLE Animals")
    Path.unlink("test.db")

def test_connect_to_db_type():
    """
    Test that connect_to_database function returns sqlite3.Connection
    """
    conn = connect_to_database('test.db')
    assert isinstance(conn, sqlite3.Connection)
    conn.close()

def test_connect_to_db_name():
    """
    Test that connect_to_database function connects to correct DB file
    """
    conn = connect_to_database('test.db')
    cur = conn.cursor()
    # List current databases https://www.sqlite.org/pragma.html#pragma_database_list
    cur.execute('PRAGMA database_list;')
    # Unpack the three parameters returned
    db_index, db_type, db_filepath = cur.fetchone()
    # Extract just the filename from the full filepath
    db_filename = Path(db_filepath).name
    assert db_filename == 'test.db'

def test_query_database(setup_database):
    """
    Test that query_database retrieves the correct data
    """
    # Get connection from fixture
    conn = setup_database
    # Use query_database to retrieve data
    sql = "SELECT * FROM Animals"
    result = query_database(sql, conn=conn)
    # Result returned is a list (cursor.fetchall)
    assert isinstance(result, list)
    # There should just be one record
    assert len(result) == 1
    # That record should be the data we added
    assert result[0] == ("Bugs", "Rabbit", 6)

def test_query_database_without_connection():
    """
    Test the `query_database` function without a provided connection
    """
    sql = 'SELECT * FROM Animals'
    # ensure that we get a TypeError
    with pytest.raises(TypeError):
        query_database(sql)