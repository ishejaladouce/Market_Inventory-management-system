import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db')))

from db_config import connect_db

def get_low_stock_products():
    conn = connect_db()
    if not conn:
        print("[ERROR] Could not connect to DB.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, quantity FROM products WHERE quantity < 5")
        return cursor.fetchall()
    finally:
        conn.close()

if __name__ == "__main__":
    low_stock = get_low_stock_products()
    if low_stock:
        print("🚨 Low stock alerts:")
        for name, quantity in low_stock:
            print(f" - {name}: only {quantity} left!")
    else:
        print("All products are sufficiently stocked.")


