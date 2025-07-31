from db.db_config import connect_db

ALERT_THRESHOLD = 5

def get_stock_alerts():
    try:
        conn = connect_db()

        if not conn:
            return []

        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, quantity, measurement_unit
            FROM inventory
            WHERE quantity <= %s  
            ORDER BY quantity ASC
        """, (ALERT_THRESHOLD,))

        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        alerts = []
        for row in rows:
            alerts.append({
                "product": row[0],
                "quantity": row[1],
                "measurement_unit": row[2] or "piece"  # Default to "piece" if NULL
            })

        return alerts

    except Exception as e:
        print("Failed to fetch stock alerts:", e)
        return []