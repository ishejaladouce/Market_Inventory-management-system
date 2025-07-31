from db.db_config import connect_db

def add_product():
    print("\n--- Add New Product ---")
    name = input("Enter product name: ").strip().title()

    # Validate quantity input
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative integer for quantity.")

    # Validate price input
    while True:
        try:
            price = float(input("Enter unit price (RWF): "))
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number for price.")

    # Measurement input
    print("Select measurement unit:")
    print("1. piece")
    print("2. kg")
    print("3. litre")
    measurement_options = {"1": "piece", "2": "kg", "3": "litre"}
    measurement_choice = input("Enter option number: ").strip()
    measurement = measurement_options.get(measurement_choice, "piece")  # Default is 'piece'

    conn = None
    cursor = None
    try:
        conn = connect_db()
        if not conn:
            print("Could not connect to database.")
            return

        cursor = conn.cursor()

        # Check if product already exists
        cursor.execute("SELECT * FROM inventory WHERE name = %s", (name,))
        existing = cursor.fetchone()

        if existing:
            print(f"\nProduct '{name}' already exists. Use the update option instead.\n")
        else:
            cursor.execute(
                "INSERT INTO inventory (name, quantity, unit_price, measurement_unit) VALUES (%s, %s, %s, %s)",
                (name, quantity, price, measurement)
            )
            conn.commit()
            print(f"\nProduct '{name}' added successfully with measurement '{measurement}'!\n")

    except Exception as e:
        print("Error adding product:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    add_product()
