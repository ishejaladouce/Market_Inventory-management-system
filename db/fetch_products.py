from db.db_config import connect_db

def get_inventory():
    try:
        conn = connect_db()
        if not conn:
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT id, name, quantity, unit_price, measurement_unit FROM inventory")

        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        inventory = []
        for row in rows:
            inventory.append({
                "id": row[0],
                "name": row[1],
                "quantity": row[2],
                "unit_price": float(row[3]),
                "measurement_unit": row[4]
            })

        return inventory

    except Exception as e:
        print("Error fetching inventory data:", e)
        return []
