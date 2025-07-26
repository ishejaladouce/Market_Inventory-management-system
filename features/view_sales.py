def display_sales_report(sales):
    if not sales:
        print("\nNo sales data available.\n")
        return

    print("\nSALES REPORT")
    print("-" * 50)
    for sale in sales:
        print(f"Product      : {sale['product']}")
        print(f"Quantity     : {sale['quantity']}")
        print(f"Unit Price   : {sale['unit_price']} RWF")
        print(f"Total        : {sale['total']} RWF")
        print(f"Date & Time  : {sale['date']}")
        print("-" * 50)
