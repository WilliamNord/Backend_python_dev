import mysql.connector

def get_db():
    """Kobler til MariaDB-databasen og returnerer tilkoblingen."""
    connection = mysql.connector.connect(
        host="localhost",
        user="backend-user",
        password="sterktpassord",
        database="backend_db"
    )
    return connection