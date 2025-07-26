# Main file that runs the Inventory System.
# Users will see a menu and choose what to do.

from features.check_inventory import check_inventory  # to display inventory
from db.fetch_products import get_inventory           # to fetch data from MySQL
from features.record_sale import record_sale
from db.fetch_sales import get_sales

# Main menu function that keeps running until the user exits
def main_menu():

    while True:
        # Display the menu options to the user
        print("\n LOCAL MARKET INVENTORY SYSTEM")
        print(" -----------------------------")
        print("1. Check Inventory")
        print("2. Record a Sale")
        print("3. View Sales Report")
        print("4. View Stock Alerts")
        print("5. Exit")



        # Ask for user input
        choice = input("Choose an option (1-5): ")

        # If user chooses to check inventory
        if choice == "1":
            inventory = get_inventory()  # fetch products from database
            check_inventory(inventory)   # display them in a table format

        elif choice == "2":
            record_sale()

        elif choice == "3":
            sales = get_sales()
            return(sales)

        # If user chooses to exit
        elif choice == "4":
            low_stock = get_low_stock_products()
            if low_stock:
                print("Low stock alerts:")
                for name, quantity in low_stock:
                    print(f" - {name}: only {quantity} left!")
            else:
                print("All products are sufficiently stocked.")

        # If user enters something invalid
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

# Run the main menu function
if __name__ == "__main__":
    main_menu()