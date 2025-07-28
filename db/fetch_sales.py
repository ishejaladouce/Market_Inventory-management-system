# fetch_sales.py
# This function connects to the database and fetches all sales records from the 'sales' table.

from db.db_config import connect_db

def get_sales_data():
    try:
        conn = connect_db()

        if not conn:
            # If connection fails, return empty list
            return []

        cursor = conn.cursor()

        cursor.execute("""
            SELECT product_name, quantity, unit_price, (quantity * unit_price) AS total_amount, sale_date
            FROM sales
            ORDER BY sale_date DESC
        """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        sales = []
        for row in rows:
            sales.append({
                "product": row[0],
                "quantity": row[1],
                "unit_price": float(row[2]),
                "total": float(row[3]),
                "date": row[4].strftime("%Y-%m-%d %H:%M:%S")
            })

        return sales

    except Exception as e:
        print("Failed to fetch sales data:", e)
        return []
