# This file contains a function to display the current inventory in a table format. 
# It should be called after fetching products from the database.


# Function to display the inventory in a table format
def check_inventory(products):
    
    #check if the products list is empty
    if not products:
        print("\n Inventory is currently empty. \n")
        return #End the function early if there's nothing to show
    
    # Print the table headers
    print("\n Current Inventory: ")
    print(f"{'Product Name':<20} {'Quantity':<10} {'Unit Price (RWF)':<15}")
    print("-" * 45)  # Just a line to separate header and data

    #Loop through each product and print its details
    for product in products:
        print(f"{product['name']:<20} {product['quantity']:<10} {product['price']:<15,.0f}")

        print("-" * 45 + "\n")  # Closing line