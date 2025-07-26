import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from stock_alerts import get_low_stock_products

def test_stock_alerts():
    low_stock_items = get_low_stock_products()
    if low_stock_items:
        print("Low stock alerts:")
        for name, quantity in low_stock_items:
            print(f" - {name}: only {quantity} left!")
    else:
        print(" All products are sufficiently stocked.")

if __name__ == "__main__":
    test_stock_alerts()

