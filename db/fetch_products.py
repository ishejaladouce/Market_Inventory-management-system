#This file contains the function that connects to the database and retrieves the inventory data.

#Import the database connection function
from db.db_config import connect_db

# Function to get the inventory from the database
def get_inventory():
    
    try:
        # Connect to the database
        conn = connect_db()
        if not conn:
            return [] # If connection fails, return an empty list
        
        cursor = conn.cursor()

        # SQL query to fetch all products (product name, quantity, and price)
        cursor.execute("SELECT name, quantity, price FROM inventory ORDER BY name;")
        rows = cursor.fetchall()

        # close the cursor and connection
        cursor.close()
        conn.close()

        # Format the fetched data into a list of dictionaries
        products = []
        for row in rows:
            products.append({
                'name': row[0],
                'quantity': row[1],
                'price': float(row[2])
            })

        return products 
    
    except Exception as e:
        print("Error fetching inventory data:", e)
        return []