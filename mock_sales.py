from tabulate import tabulate

def display_mock_sales_report():
    """Display mock sales data for demonstration purposes"""
    
    # Mock sales data
    mock_sales = [
        {
            "product": "Rice",
            "quantity": 5,
            "unit_price": 2500,
            "total": 12500,
            "date": "2024-01-15 14:30:00",
            "measurement_unit": "kg"
        },
        {
            "product": "Tomatoes",
            "quantity": 10,
            "unit_price": 800,
            "total": 8000,
            "date": "2024-01-15 13:45:00",
            "measurement_unit": "kg"
        },
        {
            "product": "Milk",
            "quantity": 3,
            "unit_price": 1200,
            "total": 3600,
            "date": "2024-01-15 12:20:00",
            "measurement_unit": "litre"
        },
        {
            "product": "Bread",
            "quantity": 8,
            "unit_price": 500,
            "total": 4000,
            "date": "2024-01-15 11:15:00",
            "measurement_unit": "piece"
        },
        {
            "product": "Potatoes",
            "quantity": 7,
            "unit_price": 600,
            "total": 4200,
            "date": "2024-01-15 10:30:00",
            "measurement_unit": "kg"
        }
    ]
    
    if not mock_sales:
        print("\nNo sales data available.\n")
        return

    table = []
    for sale in mock_sales:
        product_with_unit = f"{sale['product']} ({sale['measurement_unit']})"
        table.append([
            product_with_unit,
            sale["quantity"],
            f"{sale['unit_price']:,.0f} RWF",
            f"{sale['total']:,.0f} RWF",
            sale["date"]
        ])

    headers = ["Product (Unit)", "Quantity", "Unit Price", "Total", "Date & Time"]
    print("\nSALES REPORT (Mock Data)")
    print("=" * 50)
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    
    # Calculate totals
    total_revenue = sum(sale['total'] for sale in mock_sales)
    total_items = sum(sale['quantity'] for sale in mock_sales)
    print(f"\n📊 SUMMARY:")
    print(f"   Total Sales: {len(mock_sales)} transactions")
    print(f"   Total Items Sold: {total_items} units")
    print(f"   Total Revenue: {total_revenue:,.0f} RWF")

if __name__ == "__main__":
    display_mock_sales_report() 