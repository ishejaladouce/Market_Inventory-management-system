from datetime import datetime

inventory = {
    "Product" :[10,900]
}


def record_sale():

    product = input("Enter product name: ").strip().title()

    if product not in inventory:
        print("Product not found in inventory")

    else:
        try:
            quantity = int(input("Enter quantity being sold: "))
        except ValueError:
            print("Incorrect input, Quantity must be a number.")

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        if inventory[product][0] < quantity:
            print("Not enough inside the inventory.")
            return

    sale = {
        "Product": product,
        "Quantity":quantity,
        "Price":inventory[product][1],
        "Total Price":quantity * inventory[product][1],
        "Time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }

    print("Sale Record")
    for key, value in sale.items():
        print(f"{key.capitalize()}: {value}")

    inventory[product][0] -= quantity




record_sale()
