# product_management.py

inventory = {}

def add_product():
    name = input("Product name: ").strip()
    if name in inventory:
        print("Product already exists.")
        return
    try:
        qty = int(input("Quantity: "))
        price = float(input("Price per unit: "))
        inventory[name] = {"quantity": qty, "price": price}
        print(f"{name} added.")
    except ValueError:
        print("Please enter valid numbers for quantity and price.")

def update_product():
    name = input("Product to update: ").strip()
    if name not in inventory:
        print("Product not found.")
        return
    try:
        qty = int(input("New quantity: "))
        price_input = input("New price (leave blank to keep current): ").strip()
        price = float(price_input) if price_input else inventory[name]["price"]
        inventory[name]["quantity"] = qty
        inventory[name]["price"] = price
        print(f"{name} updated.")
    except ValueError:
        print("Invalid input.")

def delete_product():
    name = input("Product to delete: ").strip()
    if name in inventory:
        del inventory[name]
        print(f"{name} deleted.")
    else:
        print("Product not found.")

def list_products():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for name, details in inventory.items():
        print(f"{name} - Qty: {details['quantity']}, Price: {details['price']}")
