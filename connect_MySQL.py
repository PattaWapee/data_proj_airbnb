import mysql.connector
from mysql.connector import Error, connect

# Create a MySQL connection object

def create_server_connection(host_name, user_name, user_password, db_name=None):
    connection = None
    if db_name:
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
    else:
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    return connection

def create_database(connection, db_name):
    cursor = connection.cursor()
    query = "CREATE DATABASE " + db_name
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    return cursor

def close_connection(connection, cursor=None):
    try:
        if cursor is not None:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    except Error as e:
        print("Error: ", e)
"""
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")
    return cursor
    """

def execute_query(connection, query, multi=False):
    cursor = connection.cursor()
    try:
        if multi:
            # Split the query into separate statements
            statements = query.split(';')
            for statement in statements:
                if statement.strip():
                    cursor.execute(statement + ';')
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")
    return cursor

