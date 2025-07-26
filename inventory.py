# inventory.py

def low_stock_alert():
    low_stock_items = [name for name, details in product_management.inventory.items() if details["quantity"] < 5]
    if low_stock_items:
        print("Low stock alert for these products:")
        for item in low_stock_items:
            print(f"- {item} (Qty: {product_management.inventory[item]['quantity']})")
    else:
        print("No low stock products.")

def check_stock(product_name):
    if product_name in product_management.inventory:
        details = product_management.inventory[product_name]
        print(f"{product_name}: Quantity = {details['quantity']}, Price = {details['price']}")
    else:
        print("Product not found.")
