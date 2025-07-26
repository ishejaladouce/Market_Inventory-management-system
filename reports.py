# reports.py
import sales
import product_management

def sales_summary():
    if not sales.sales_history:
        print("No sales recorded.")
        return
    print("Sales Summary:")
    total_revenue = 0
    for sale in sales.sales_history:
        date_str = sale["date"].strftime("%Y-%m-%d %H:%M")
        print(f"{date_str}: {sale['product']} x {sale['quantity']} = {sale['total']}")
        total_revenue += sale['total']
    print(f"Total Revenue: {total_revenue}")

def inventory_report():
    product_management.list_products()
