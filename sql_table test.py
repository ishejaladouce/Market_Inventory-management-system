import mysql.connector
from db.db_config import connect_db

def describe_products_table():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        print("Connected to DB, running DESCRIBE...")
        cursor.execute("DESCRIBE products")
        columns = cursor.fetchall()

        print("Your 'products' table structure:")
        for column in columns:
            print(column)

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error:", e)

describe_products_table()


