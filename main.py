# main.py
import auth
import product_management
import inventory
import sales
import reports

def main():
    print("Welcome to Market Inventory Management System")
    if not auth.login():
        return

    while True:
        print("\nMenu:")
        print("1. List Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Record Sale")
        print("6. Sales Summary")
        print("7. Low Stock Alert")
        print("8. Logout and Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            product_management.list_products()
        elif choice == "2":
            product_management.add_product()
        elif choice == "3":
            product_management.update_product()
        elif choice == "4":
            product_management.delete_product()
        elif choice == "5":
            sales.record_sale()
        elif choice == "6":
            reports.sales_summary()
        elif choice == "7":
            inventory.low_stock_alert()
        elif choice == "8":
            auth.logout()
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
