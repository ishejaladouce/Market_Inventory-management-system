# Main file that runs the Inventory System.
# Users will see a menu and choose what to do.

from features.check_inventory import check_inventory  # to display inventory
from db.fetch_products import get_inventory           # to fetch data from MySQL
from features.record_sale import record_sale
from features.view_sales import get_sales_data, display_sales_report
from features.create_product import add_product
from features.stock_alerts import display_stock_alerts

# Main menu function that keeps running until the user exits
def main_menu():

    while True:
        # Display the menu options to the user
        print("\n LOCAL MARKET INVENTORY SYSTEM")
        print(" -----------------------------")
        print("1. Check Inventory")
        print("2. Add Product")
        print("3. Record a Sale")
        print("4. View Stock Alerts")
        print("5. View Sales Report")
        print("6. Exit")

        # Ask for user input
        choice = input("Choose an option (1-6): ")

        # If user chooses to check inventory
        if choice == "1":
            inventory = get_inventory()  # fetch products from database
            check_inventory(inventory)   # display them in a table format

        # If user chooses to add a new product
        elif choice == "2":
            add_product()

        # If user chooses to record a sale
        elif choice == "3":
            record_sale()

        # If user chooses to view stock alerts
        elif choice == "4":
            display_stock_alerts()

        # If user chooses to view sales report
        elif choice == "5":
            sales = get_sales_data()
            display_sales_report()

        # If user chooses to exit the program
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        # If user enters an invalid option
        else:
            print("Invalid input. Please try again.")

# Run the main menu function
if __name__ == "__main__":
    main_menu()