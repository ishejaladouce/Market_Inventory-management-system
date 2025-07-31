"""
Market Inventory Management System

A Python-based inventory management system for local markets and small businesses.
This system allows users to manage product inventory, track sales, and monitor stock levels.

Features:
- Check current inventory levels
- Add new products to inventory
- Record sales transactions
- View low stock alerts
- Generate sales reports

This module serves as the main entry point for the application, providing a user-friendly interface
"""

from features.check_inventory import check_inventory  # Display inventory in table format
from db.fetch_products import get_inventory           # Fetch data from MySQL database
from features.record_sale import record_sale          # Process sales transactions
from features.view_sales import get_sales_data, display_sales_report  # Sales reporting
from features.create_product import add_product       # Add new products
from features.stock_alerts import display_stock_alerts  # Low stock monitoring

def main_menu():
    """
    Main menu function that provides an interactive interface for the inventory system.
    
    Displays a menu with 6 options and handles user input to navigate through
    different features of the system.
    """
    while True:
        # Display the main menu options
        print("\n LOCAL MARKET INVENTORY SYSTEM")
        print(" -----------------------------")
        print("1. Check Inventory")
        print("2. Add Product")
        print("3. Record a Sale")
        print("4. View Stock Alerts")
        print("5. View Sales Report")
        print("6. Exit")

        # Get user input and validate
        choice = input("Choose an option (1-6): ")

        # Handle menu options
        if choice == "1":
            # Fetch and display current inventory
            inventory = get_inventory()
            check_inventory(inventory)

        elif choice == "2":
            # Add a new product to inventory
            add_product()

        elif choice == "3":
            # Record a sales transaction
            record_sale()

        elif choice == "4":
            # Display low stock alerts
            display_stock_alerts()

        elif choice == "5":
            # Display sales report with summary
            try:
                sales = get_sales_data()
                display_sales_report()
            except Exception as e:
                print(f"Error displaying sales report: {e}")
                print("Showing mock data instead...")
                from mock_sales import display_mock_sales_report
                display_mock_sales_report()

        elif choice == "6":
            # Exit the application
            print("Exiting the system. Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    # Start the application
    main_menu()