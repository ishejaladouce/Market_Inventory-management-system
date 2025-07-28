print("Starting fetch_all_products...")

from db.db_config import connect_db

def fetch_all_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        if rows:
            print("Existing products in your database:")
            for row in rows:
                print(row)
        else:
            print("No products found in the database.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error fetching products:", e)

fetch_all_products()
