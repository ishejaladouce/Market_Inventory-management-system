from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Mock inventory structure (Product: [Quantity, Price])
inventory = {
    "Product": [10, 900]  # Example: 10 units at 900 RWF each
}

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print("Can't connect to the database.", e)
        return None

def record_sale():
    product = input("Enter product name: ").strip().title()

    if product not in inventory:
        print("Product not found in inventory.")
        return

    try:
        quantity = int(input("Enter quantity being sold: "))
    except ValueError:
        print("Invalid input: Quantity must be a number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    available_stock = inventory[product][0]
    unit_price = inventory[product][1]

    if quantity > available_stock:
        print("Not enough stock in inventory.")
        return

    total_price = quantity * unit_price
    sale_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert sale into database
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            insert_query = """
                INSERT INTO sales (product_name, quantity, unit_price, sale_date)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (product, quantity, unit_price, sale_time))
            conn.commit()
        except Exception as e:
            print("Failed to insert sale into database:", e)
            return
        finally:
            cursor.close()
            conn.close()
    else:
        print("Sale not recorded in database due to connection error.")

    # Update local inventory
    inventory[product][0] -= quantity

    print("\n SALE RECORDED")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: {unit_price}")
    print(f"Total Price: {total_price}")
    print(f"Date & Time: {sale_time}")
    print(f"Inventory updated. {inventory[product][0]} units remaining of {product}.\n")

# Uncomment the below if you want to test running this file directly
# if __name__ == "__main__":
#     record_sale()
