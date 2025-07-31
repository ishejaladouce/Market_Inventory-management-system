from db.db_config import connect_db 

def get_sales_data():
    try:
        conn = connect_db()
        if not conn:
            return []

        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                s.product_name, 
                s.quantity, 
                s.unit_price, 
                (s.quantity * s.unit_price) AS total_amount, 
                s.sale_date,
                p.measurement_unit
            FROM sales s
            INNER JOIN products p ON s.product_name = p.product_name
            ORDER BY s.sale_date DESC
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
                "date": row[4].strftime("%Y-%m-%d %H:%M:%S"),
                "measurement_unit": row[5]
            })

        return sales

    except Exception as e:
        print("Failed to fetch sales data:", e)
        return []
