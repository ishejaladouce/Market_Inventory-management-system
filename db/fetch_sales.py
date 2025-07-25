# This function will connect to the Database and fetches all sales records from the 'sales' table.

#This gives us access to out DB connection function
from db.db_config import connect_db

def get_sales():
    try:
        #connect to the database
        conn = connect_db()

        if not conn:
            #If the connection fails, return an empty list
            return []

        cursor = conn.cursor() #create a cursor object to run SQL queries

        cursor.execute("""
            SELECT product_name, quantity, unit_price, total_amount, sale_time
            FROM sales
            ORDER BY sale_time DESC
        """)

        #Fetch all the results from the query
        rows = cursor.fetchall()

        #Close the cursor and DB connection 
        cursor.close()
        conn.close()

        # Format the data in a list of dictionaries
        sales = []
        for row in rows:
            sales.append({
                "product": row[0],
                "quantity": row[1],
                "unit_price": float(row[2]),
                "total": float(row[3]),
                "date": row[4].strftime("%Y-%m-%d %H:%M:%S")
            })

            #return the final list of formatted sales
        return sales

    except Exception as e:
        # If anything goes Wrong, print the error and return an empty list
        print("Failed to fetch sales data:", e)
        return []