#This file contains the function that connects to the database and retrieves the inventory data.

#Import the database connection function
from db.db_config import connect_db

# Function to get the inventory from the database
def get_inventory():
    try:
        conn = connect_db()
        if not conn:
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT id, name, quantity, unit_price FROM inventory")  # use unit_price, not price

        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        inventory = []
        for row in rows:
            inventory.append({
                "id": row[0],
                "name": row[1],
                "quantity": row[2],
                "unit_price": float(row[3])
            })

        return inventory

    except Exception as e:
        print("Error fetching inventory data:", e)
        return []
