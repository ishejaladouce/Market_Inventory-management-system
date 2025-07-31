from tabulate import tabulate
from db.fetch_stock_alerts import get_stock_alerts

def display_stock_alerts():
    alerts = get_stock_alerts()

    if not alerts:
        print("\nAll stock levels are healthy \n")
        return

    table = []
    for item in alerts:
        product_with_unit = f"{item['product']} ({item['measurement_unit']})"
        table.append([product_with_unit, item["quantity"]])

    headers = ["Product (Unit)", "Quantity Left"]
    print("\n LOW STOCK ALERTS ")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
