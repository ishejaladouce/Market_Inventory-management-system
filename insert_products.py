from db.db_config import connect_db

def insert_sample_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        products = [
            ("Soap", 10, 1.50),
            ("Toothpaste", 3, 2.00),
            ("Shampoo", 7, 4.75),
            ("Lotion", 2, 5.00),
        ]

        cursor.executemany(
            "INSERT INTO products (product_name, quantity, unit_price) VALUES (%s, %s, %s)", 
            products
        )
        conn.commit()
        print(f"Inserted {cursor.rowcount} products successfully.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error inserting products:", e)

if __name__ == "__main__":
    insert_sample_products()
