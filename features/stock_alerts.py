from db.db_config import connect_db

def get_low_stock_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT product_name, quantity FROM products WHERE quantity < 5"
        cursor.execute(query)
        low_stock = cursor.fetchall()

        cursor.close()
        conn.close()
        return low_stock
    except Exception as e:
        print("Error fetching low stock products:", e)
        return []

if __name__ == "__main__":
    low_stock_items = get_low_stock_products()
    if not low_stock_items:
        print("✅ All products have sufficient stock.")
    else:
        print("⚠️ Low stock alerts:")
        for product_name, quantity in low_stock_items:
            print(f"- {product_name}: only {quantity} left!")



