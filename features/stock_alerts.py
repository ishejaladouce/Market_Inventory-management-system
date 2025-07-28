from tabulate import tabulate
from db.fetch_stock_alerts import get_stock_alerts

def display_stock_alerts():
    alerts = get_stock_alerts()

    if not alerts:
        print("\nAll stock levels are healthy \n")
        return

    table = []
    for item in alerts:
        table.append([item["product"], item["quantity"]])

    headers = ["Product", "Quantity Left"]
    print("\n LOW STOCK ALERTS ")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
