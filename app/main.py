# Main file that runs the Inventory System.
# Users will see a menu and choose what to do.

from features.check_inventory import check_inventory  # to display inventory
from db.fetch_products import get_inventory           # to fetch data from MySQL

# Main menu function that keeps running until the user exits
def main_menu():

    while True:
        # Display the menu options to the user
        print("\n LOCAL MARKET INVENTORY SYSTEM")
        print(" -----------------------------")
        print("1. Check Inventory")
        print("2. Exit")


        # Ask for user input
        choice = input("Choose an option (1-2): ")

        # If user chooses to check inventory
        if choice == "1":
            inventory = get_inventory()  # fetch products from database
            check_inventory(inventory)   # display them in a table format

        # If user chooses to exit
        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break

        # If user enters something invalid
        else:
            print("Invalid input. Please try again.")

# Run the main menu function
if __name__ == "__main__":
    main_menu()