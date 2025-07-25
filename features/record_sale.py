# record_sale.py
# This function handles recording a sale.
# It:
# 1. Asks for the product name
# 2. Validates availability
# 3. Asks for quantity
# 4. Checks stock
# 5. Records the sale
# 6. Updates the inventory

from datetime import datetime

# Mock inventory structure (Product: [Quantity, Price])
inventory = {
    "Product": [10, 900]  # Example: 10 units at 900 RWF each
}

def record_sale():
    # Ask the user for the product name
    product = input("Enter product name: ").strip().title()

    # Check if product is in inventory
    if product not in inventory:
        print("Product not found in inventory.")
        return  # Early exit to avoid using undefined variables

    try:
        # Ask for quantity being sold
        quantity = int(input("Enter quantity being sold: "))
    except ValueError:
        print("Invalid input: Quantity must be a number.")
        return

    # Check for valid quantity
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    # Check if there's enough stock
    available_stock = inventory[product][0]
    unit_price = inventory[product][1]

    if quantity > available_stock:
        print("Not enough stock in inventory.")
        return

    # Calculate total and prepare the sale record
    sale = {
        "Product": product,
        "Quantity": quantity,
        "Price": unit_price,
        "Total Price": quantity * unit_price,
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Print the sale record nicely
    print("\n SALE RECORDED")
    for key, value in sale.items():
        print(f"{key}: {value}")

    # Update inventory
    inventory[product][0] -= quantity
    print(f"\n Inventory updated. {inventory[product][0]} units remaining of {product}.\n")

# Run the function
record_sale()
