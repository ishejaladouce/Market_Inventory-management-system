# It should be called after fetching products from the database.

# Function to display the inventory in a table format
def check_inventory(products):
    if not products:
        print("\n Inventory is currently empty. \n")
        return

    # Print headers
    print("\n Current Inventory:")
    print(f"{'Product Name':<20} {'Quantity':<10} {'Unit':<15} {'Unit Price (RWF)':<15}")
    print("-" * 60)

    # Print each product row
    for product in products:
        print(f"{product['name']:<20} {product['quantity']:<10} {product['measurement_unit']:<15} {product['unit_price']:<15,.0f}")

    print("-" * 60 + "\n")

