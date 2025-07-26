Market_Inventory-management-system

## Project Structure

The codebase is organized to follow clean modular design principles. Each feature is separated for clarity and scalability.

market_inventory-management-system/
├── features/                  # All core application features
│   ├── check_inventory.py     # Feature 1: View all products
│   ├── modify_quantity.py     # Feature 2: Update product quantities
│   ├── record_sale.py         # Feature 3: Record a sale
│   ├── stock_alerts.py        # Feature 4: Show low-stock alerts
│   └── sales_report.py        # Feature 5: Show performance and revenue
│
├── db/                        # Database connection logic
│   ├── db_config.py           # PostgreSQL connection setup (Aiven)
│   └── queries.py             # (Optional) SQL query functions
│
├── main.py                    # Entry point with interactive menu
├── README.md                  # Project documentation
├── .env                       # Environment file for DB credentials (not committed)
├── .gitignore                 # Specifies untracked files like `.env`
└── requirements.txt           # Python dependencies

### Feature: Check Inventory
This feature allows users to view all products in stock with their quantity and price. It simulates database interaction using mock data and includes empty-checks and clean formatting for ease of use.
