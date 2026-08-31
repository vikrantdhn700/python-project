# Retail Store Management and Analytics System

A complete Python assignment combining object-oriented programming, inheritance,
method overriding, file handling, CSV datasets, pandas analysis, data cleaning,
and automated report generation.

## Folder Structure

```text
retail-store-management-analytic-sys/
|-- main.py
|-- products.csv
|-- sales.csv
|-- requirements.txt
|-- README.md
`-- output/
    |-- cleaned_sales.csv
    |-- product_report.csv
    |-- city_sales_report.csv
    |-- category_report.csv
    `-- sales_summary.txt
```

`products.csv`, `sales.csv`, and everything under `output/` are regenerated each
time the program runs.

## Requirements and Execution

- Python 3.8 or newer
- pandas

Install and run:

```bash
python -m pip install -r requirements.txt
python main.py
```

## OOP Design

`Product` is the parent class. It stores `product_id`, `name`, `brand`, `price`,
and `stock`, and provides `display_product()` and `update_stock()`.

```text
                         Product
                            |
          +-----------------+-----------------+
          |                 |                 |
     Electronics         Clothing           Books
  warranty, model    size, material   author, publisher
```

The three child classes use `super()` to initialize their inherited properties.
They override `display_product()` and `to_record()` to add category-specific
behavior while reusing the parent implementation. This demonstrates inheritance
and method overriding.

The project creates:

- 10 electronics
- 10 clothing products
- 10 books
- 30 products in total

## File Handling and Dataset Creation

The project uses `open()` with context managers (`with open(...)`) so files close
automatically, even if an error occurs.

- Write mode (`"w"`) creates `products.csv` and writes the first 27 products.
- Append mode (`"a"`) appends the final three products.
- Read mode (`"r"`) reads all product records with `csv.DictReader`.
- Write mode creates `sales.csv` with 62 raw rows: 60 transactions and two
  deliberate duplicates used to demonstrate cleaning.
- Write mode creates the human-readable `sales_summary.txt` report.

The CSV work uses Python's built-in `csv.DictWriter` and `csv.DictReader`.

## Pandas Concepts Demonstrated

### Series and DataFrame

`pd.read_csv()` loads both CSV files as pandas DataFrames. Selecting a single
column produces a Series. The program creates a revenue Series using:

```python
revenue_series = sales_df["quantity"] * sales_df["price"]
```

### Data Cleaning

The raw sales dataset intentionally contains duplicate rows, extra spaces, and
inconsistent capitalization. Cleaning includes:

- `drop_duplicates()` for duplicate removal
- `str.strip()` for whitespace removal
- `str.upper()` and `str.title()` for consistent text
- `replace()` for standardizing UPI
- `pd.to_numeric()` and `astype()` for numeric types
- `dropna()` for unusable rows

The raw shape is `(62, 8)`, and the cleaned shape is `(60, 9)`. The ninth column
is calculated revenue.

### Filtering and Sorting

Boolean filtering identifies:

- Products with stock below 10
- Products priced above the average price

`sort_values()` orders products, cities, and categories by quantities or revenue.

### Aggregation and groupby()

The program uses `sum()`, `mean()`, `max()`, `min()`, `value_counts()`,
`groupby()`, and `agg()` to calculate all requested measurements.

## Analyses Performed

- Total sales transactions
- Total quantity sold
- Total and average transaction revenue
- Highest- and lowest-value transactions
- Best- and lowest-selling products
- Sales and revenue by category
- Revenue by product and city
- Payment-method distribution
- Top five and bottom five products
- Average, maximum, and minimum product price
- Products with stock below 10
- Products priced above average

## Generated Reports

- `cleaned_sales.csv` — standardized transactions with calculated revenue
- `product_report.csv` — product details, quantity sold, and revenue
- `city_sales_report.csv` — transactions, quantity, and revenue by city
- `category_report.csv` — sales and revenue statistics by category
- `sales_summary.txt` — human-readable results and key insights

## Current Key Insights

With the included deterministic dataset:

- Total cleaned transactions: 60
- Total quantity sold: 180
- Total revenue: ₹2,407,748.00
- Average transaction value: ₹40,129.13
- Best-selling product: Camera (10 units)
- Highest-revenue category: Electronics
- Highest-revenue city: Bangalore

## Suggested Video Walkthrough

1. Explain the retail store problem and show the folder structure.
2. Open `main.py` and explain the parent and child classes.
3. Show inheritance, `super()`, overriding, objects, and stock updates.
4. Explain `open()`, read/write/append modes, and context managers.
5. Run the program and open the generated product and sales CSV files.
6. Explain pandas Series, DataFrames, and `pd.read_csv()`.
7. Walk through cleaning, type conversion, filtering, and sorting.
8. Explain aggregation, `groupby()`, and each requested calculation.
9. Open all five generated reports.
10. Finish with the key insights shown in `sales_summary.txt`.
