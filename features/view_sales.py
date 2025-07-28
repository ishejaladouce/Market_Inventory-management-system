from tabulate import tabulate
from db.fetch_sales import get_sales_data

def display_sales_report():
    sales = get_sales_data()

    if not sales:
        print("\nNo sales data available.\n")
        return

    table = []
    for sale in sales:
        table.append([
            sale["product"],
            sale["quantity"],
            f"{sale['unit_price']:,.0f} RWF",
            f"{sale['total']:,.0f} RWF",
            sale["date"]
        ])

    headers = ["Product", "Quantity", "Unit Price", "Total", "Date & Time"]
    print("\nSALES REPORT")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
