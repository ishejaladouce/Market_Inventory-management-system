from datetime import datetime 
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

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

    try:
        quantity = int(input("Enter quantity sold: "))
    except ValueError:
        print("Invalid input: Quantity must be a number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    # 💡 Prompt for measurement unit
    print("\nSelect measurement unit:")
    print("1. piece")
    print("2. kg")
    print("3. litre")
    measurement_options = {"1": "piece", "2": "kg", "3": "litre"}
    measurement_choice = input("Enter option number: ")
    measurement = measurement_options.get(measurement_choice, "piece")  # default to 'piece'

    conn = connect_db()
    if not conn:
        print("Database connection failed.")
        return

    try:
        cursor = conn.cursor(dictionary=True)

        # Check if product exists in inventory
        cursor.execute("SELECT quantity, unit_price FROM inventory WHERE name = %s", (product,))
        product_row = cursor.fetchone()

        if not product_row:
            print(f"Product '{product}' not found in inventory.")
            return

        available_stock = product_row['quantity']
        unit_price = float(product_row['unit_price'])

        if quantity > available_stock:
            print("Not enough stock in inventory.")
            return

        total_price = quantity * unit_price
        sale_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert sale record (🆕 including measurement)
        insert_sale = """
            INSERT INTO sales (product_name, quantity, unit_price, sale_date, measurement_unit)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_sale, (product, quantity, unit_price, sale_time, measurement))

        # Update inventory quantity
        update_inventory = """
            UPDATE inventory SET quantity = quantity - %s WHERE name = %s
        """
        cursor.execute(update_inventory, (quantity, product))

        conn.commit()

        print("\nSALE RECORDED:")
        print(f"Product: {product}")
        print(f"Quantity: {quantity} {measurement}")
        print(f"Unit Price: {unit_price}")
        print(f"Total Price: {total_price}")
        print(f"Date & Time: {sale_time}")
        print(f"Inventory updated. {available_stock - quantity} units remaining of {product}.\n")

    except mysql.connector.Error as err:
        print(f"Error processing sale: {err}")

    finally:
        cursor.close()
        conn.close()
