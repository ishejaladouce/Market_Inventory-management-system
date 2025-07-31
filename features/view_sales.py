"""
Sales Reporting Module
=====================

This module provides functionality to display sales reports in a formatted table.
It shows sales transactions with product details, quantities, prices, and dates.

The display includes a comprehensive summary with total transactions, items sold, and revenue.
"""

from tabulate import tabulate
from db.fetch_sales import get_sales_data

def display_sales_report():
    """
    Displays a comprehensive sales report with transaction details and summary.
    
    The report shows:
    - Product name with measurement unit
    - Quantity sold
    - Unit price in RWF
    - Total price for each transaction
    - Date and time of sale
    - Summary statistics
    
    Returns:
        None: Prints the report to console
    """
    # Fetch sales data from database
    sales = get_sales_data()

    if not sales:
        print("\nNo sales data available.\n")
        return

    # Prepare table data
    table = []
    total_revenue = 0
    total_items = 0
    
    for sale in sales:
        # Handle None measurement_unit by defaulting to "piece"
        measurement_unit = sale['measurement_unit'] or "piece"
        product_with_unit = f"{sale['product']} ({measurement_unit})"
        
        # Add row to table
        table.append([
            product_with_unit,
            sale["quantity"],
            f"{sale['unit_price']:,.0f} RWF",
            f"{sale['total']:,.0f} RWF",
            sale["date"]
        ])
        
        # Accumulate totals for summary
        total_revenue += sale['total']
        total_items += sale['quantity']

    # Display the sales report table
    headers = ["Product (Unit)", "Quantity", "Unit Price", "Total", "Date & Time"]
    print("\nSALES REPORT")
    print("=" * 80)
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    
    # Display summary statistics
    print(f"\n📊 SUMMARY:")
    print(f"   Total Sales: {len(sales)} transactions")
    print(f"   Total Items Sold: {total_items} units")
    print(f"   Total Revenue: {total_revenue:,.0f} RWF")
    print("=" * 80)
