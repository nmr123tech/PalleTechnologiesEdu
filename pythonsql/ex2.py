import mysql.connector
from mysql.connector import Error


# Function to connect to MySQL and show databases
def show_databases():
    connection = None  # Initialize the connection variable
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            auth_plugin='mysql_native_password'  # Ensure compatibility with MySQL authentication
        )

        if connection.is_connected():
            print("Connected to MySQL server successfully!")

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Execute the query to show databases
            cursor.execute("SHOW DATABASES")

            # Fetch and display databases
            print("Databases:")
            for db in cursor:
                print(f" - {db[0]}")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # Ensure connection is closed
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")


# Run the function
if __name__ == "__main__":
    show_databases()
