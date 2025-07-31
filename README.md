# Market Inventory Management System

A complete Python-based inventory management system designed for local markets and small businesses. This system helps you manage product inventory, track sales, and monitor stock levels with a simple command-line interface.

##  What This System Does

This inventory system was built to solve real business problems:
- **Track your products** - See what you have in stock at any time
- **Record sales** - Keep track of every sale with automatic stock updates
- **Monitor low stock** - Get alerts when products are running low
- **Generate reports** - See your sales performance and revenue
- **Handle different units** - Support for pieces, kilograms, litres, etc.

## Key Features

###  What's Working Right Now
- **Inventory Management**: Add and view products with quantities and prices
- **Sales Tracking**: Record customer purchases with automatic stock reduction
- **Stock Alerts**: Get notified when products have less than 5 units
- **Sales Reports**: Beautiful formatted reports with revenue summaries
- **smart Units**: Products show their measurement units (piece, kg, litre)
- **Real Database**: All data stored in MySQL database (Aiven cloud)

### User Experience
- Clean, easy-to-use menu system
- Beautiful formatted tables for reports
- Automatic calculations and summaries
- Error handling with fallback options
- Measurement units displayed clearly

## Getting Started

### What You Need
- Python 3.7 or higher
- Internet connection (for database access)
- Basic understanding of command line

### Quick Setup (5 minutes)

1. **Install Python packages**:
   ```bash
   pip install pymysql python-dotenv tabulate
   ```

2. **Set up your database credentials**:
   Create a file named `.env` in the project folder with:
   ```env
   DB_HOST= fill in your credentials
   DB_PORT= fill in your credentials
   DB_USER= fill in your credentials
   DB_PASSWORD= fill in your credentials
   DB_NAME= fill in your credentials
   ```

3. **Run the system**:
   ```bash
   python -m app.main
   ```

## How to Use

### Starting the System
```bash
python -m app.main
```

You'll see a menu like this:
```
 LOCAL MARKET INVENTORY SYSTEM
 -----------------------------
1. Check Inventory
2. Add Product
3. Record a Sale
4. View Stock Alerts
5. View Sales Report
6. Exit
```

### Typical Workflow

1. **Add Products** (Option 2):
   - Enter product name (e.g., "Rice")
   - Set quantity (e.g., 50)
   - Set unit price (e.g., 2500)
   - Choose unit (piece, kg, litre)

2. **Record Sales** (Option 3):
   - Select product from list
   - Enter quantity sold
   - System automatically updates stock

3. **Check Stock** (Option 1):
   - View all products with current quantities
   - See total inventory value

4. **Monitor Alerts** (Option 4):
   - See products with low stock (less than 5 units)

5. **View Reports** (Option 5):
   - See all sales with revenue totals
   - Track performance over time

## What's Inside the Project

```
Market_Inventory-management-system/
├── app/
│   └── main.py              #  Main application - starts everything
├── db/
│   ├── db_config.py         #  Database connection setup
│   ├── fetch_products.py    #  Gets inventory data
│   ├── fetch_sales.py       #  Gets sales data
│   └── fetch_stock_alerts.py #  Gets low stock alerts
├── features/
│   ├── check_inventory.py   #  Shows inventory table
│   ├── create_product.py    #  Adds new products
│   ├── record_sale.py       #  Processes sales
│   ├── stock_alerts.py      #  Shows low stock warnings
│   └── view_sales.py        #  Shows sales reports
├── .env                     #  Your database password (keep secret!)
├── requirements.txt         #  Python packages needed
└── README.md               #  This file
```

##  Sample Outputs

### Inventory Display
```
 Current Inventory:
Product Name         Quantity   Unit            Unit Price (RWF)
------------------------------------------------------------
Rice                15         kg              30,000
Sugar               45         kg              1,800
Beans               1          piece           200
Samosa              1          piece           1,000
------------------------------------------------------------

📊 INVENTORY SUMMARY:
   Total Products: 4 different items
   Total Units: 62 units
   Total Value: 1,350,200 RWF
```

### Sales Report
```
SALES REPORT
================================================================================
╒══════════════════╤════════════╤══════════════╤═════════════╤═════════════════════╕
│ Product (Unit)   │   Quantity │ Unit Price   │ Total       │ Date & Time         │
╞══════════════════╪════════════╪══════════════╪═════════════╪═════════════════════╡
│ Sugar (kg)       │          5 │ 1,800 RWF    │ 9,000 RWF   │ 2025-07-31 19:14:13 │
├──────────────────┼────────────┼──────────────┼─────────────┼─────────────────────┤
│ Rice (kg)        │          5 │ 30,000 RWF   │ 150,000 RWF │ 2025-07-31 15:08:53 │
╘══════════════════╧════════════╧══════════════╧═════════════╧═════════════════════╛

📊 SUMMARY:
   Total Sales: 2 transactions
   Total Items Sold: 10 units
   Total Revenue: 159,000 RWF
```

### Stock Alerts
```
 LOW STOCK ALERTS 
╒═══════════════════╤═════════════════╕
│ Product (Unit)    │   Quantity Left │
╞═══════════════════╪═════════════════╡
│ Beans (piece)     │               1 │
├───────────────────┼─────────────────┤
│ Samosa (piece)    │               1 │
├───────────────────┼─────────────────┤
│ Chocolate (piece) │               2 │
╘═══════════════════╧═════════════════╛
```

## 🔧 Technical Details

### Database Setup
The system uses two main tables:

**Inventory Table:**
- Product name, quantity, price, and measurement unit
- Automatically tracks stock levels

**Sales Table:**
- Records every sale with product, quantity, price, date
- Links to inventory for automatic stock updates

### What We Fixed
-  Database connection issues (switched to PyMySQL)
-  Measurement units display (piece, kg, litre)
-  Sales report formatting with summaries
-  Stock alert system working
-  Error handling for database issues
-  Clean code with proper documentation

##  Troubleshooting

### Common Issues

**"Can't connect to database"**
- Check your `.env` file has correct credentials
- Make sure you have internet connection
- Verify the database server is running

**"Module not found"**
- Run: `pip install pymysql python-dotenv tabulate`

**"Invalid option"**
- Make sure you're running: `python -m app.main`
- Choose numbers 1-6 only

### Getting Help
If something's not working:
1. Check the error message carefully
2. Make sure your `.env` file is set up correctly
3. Try running individual features to isolate the problem

## 🎉 What Makes This Special

- **Real Database**: Not just mock data - actual MySQL database
- **Smart Units**: Products show their measurement units clearly
- **Beautiful Reports**: Professional-looking tables and summaries
- **Error Handling**: System keeps working even if database has issues
- **Clean Code**: Well-documented and organized
- **User-Friendly**: Simple menu system anyone can use

##  Future Improvements

- Add user authentication
- Export reports to Excel/PDF
- Add barcode scanning
- Mobile app interface
- Multi-location support
- Advanced analytics

---

**Built with ❤️ for local businesses**  
**Version**: 1.0  
**Last Updated**: 2025  
**Database**: MySQL with PyMySQL connector