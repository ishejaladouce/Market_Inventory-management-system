# sales.py
import datetime
import product_management

sales_history = []

def record_sale():
    product_name = input("Product sold: ").strip()
    if product_name not in product_management.inventory:
        print("Product not found.")
        return
    try:
        qty_sold = int(input("Quantity sold: "))
        current_qty = product_management.inventory[product_name]["quantity"]
        if qty_sold > current_qty:
            print("Not enough stock.")
            return
        price = product_management.inventory[product_name]["price"]
        total_price = qty_sold * price
        product_management.inventory[product_name]["quantity"] -= qty_sold
        sale = {
            "product": product_name,
            "quantity": qty_sold,
            "total": total_price,
            "date": datetime.datetime.now()
        }
        sales_history.append(sale)
        print(f"Sale recorded: {qty_sold} x {product_name} = {total_price}")
    except ValueError:
        print("Invalid quantity.")
