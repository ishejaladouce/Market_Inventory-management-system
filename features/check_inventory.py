"""
Inventory Display Module
=======================

This module provides functionality to display the current inventory in a formatted table.
It shows product names, quantities, measurement units, and prices in an easy-to-read format.

The display includes a summary with total products, units, and inventory value.
"""

# It should be called after fetching products from the database.

# Function to display the inventory in a table format
def check_inventory(products):
    
    #Displays the current inventory in a formatted table with summary.
    
    if not products:
        print("\n Inventory is currently empty. \n")
        return

    # Print table headers
    print("\n Current Inventory:")
    print(f"{'Product Name':<20} {'Quantity':<10} {'Unit':<15} {'Unit Price (RWF)':<15}")
    print("-" * 60)

    # Display each product row
    for product in products:
        # Handle None measurement_unit by defaulting to "piece"
        measurement_unit = product.get('measurement_unit') or "piece"
        print(f"{product['name']:<20} {product['quantity']:<10} {measurement_unit:<15} {product['unit_price']:<15,.0f}")

    print("-" * 60)
    
    # Calculate and display inventory summary
    total_items = sum(product['quantity'] for product in products)
    total_value = sum(product['quantity'] * product['unit_price'] for product in products)
    
    print(f"\n📊 INVENTORY SUMMARY:")
    print(f"   Total Products: {len(products)} different items")
    print(f"   Total Units: {total_items} units")
    print(f"   Total Value: {total_value:,.0f} RWF")
    print("-" * 60 + "\n")

