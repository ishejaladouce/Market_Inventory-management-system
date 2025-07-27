import mysql.connector
from db.db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def connect_to_database():
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        ssl_disabled=False  # Or use ssl_ca="path/to/cert.pem" if needed
    )
    return connection
