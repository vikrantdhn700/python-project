import csv
import sys
from pathlib import Path

import pandas as pd


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


PROJECT_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = PROJECT_DIR / "products.csv"
SALES_FILE = PROJECT_DIR / "sales.csv"
OUTPUT_DIR = PROJECT_DIR / "output"

PRODUCT_FIELDS = [
    "product_id",
    "name",
    "brand",
    "category",
    "price",
    "stock",
    "warranty",
    "model",
    "size",
    "material",
    "author",
    "publisher",
]

SALES_FIELDS = [
    "transaction_id",
    "product_id",
    "product_name",
    "category",
    "quantity",
    "price",
    "customer_city",
    "payment_method",
]


class Product:
    """Parent class containing properties shared by every product."""

    category = "General"

    def __init__(self, product_id, name, brand, price, stock):
        if price < 0 or stock < 0:
            raise ValueError("Price and stock cannot be negative.")
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = float(price)
        self.stock = int(stock)

    def display_product(self):
        print(
            f"{self.product_id} | {self.name} | {self.brand} | "
            f"₹{self.price:,.2f} | Stock: {self.stock}"
        )

    def update_stock(self, quantity):
        new_stock = self.stock + int(quantity)
        if new_stock < 0:
            raise ValueError(f"Insufficient stock for {self.name}.")
        self.stock = new_stock

    def to_record(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "warranty": "",
            "model": "",
            "size": "",
            "material": "",
            "author": "",
            "publisher": "",
        }


class Electronics(Product):
    category = "Electronics"

    def __init__(self, product_id, name, brand, price, stock, warranty, model):
        super().__init__(product_id, name, brand, price, stock)
        self.warranty = warranty
        self.model = model

    def display_product(self):
        super().display_product()
        print(f"  Warranty: {self.warranty} | Model: {self.model}")

    def to_record(self):
        record = super().to_record()
        record.update({"warranty": self.warranty, "model": self.model})
        return record


class Clothing(Product):
    category = "Clothing"

    def __init__(self, product_id, name, brand, price, stock, size, material):
        super().__init__(product_id, name, brand, price, stock)
        self.size = size
        self.material = material

    def display_product(self):
        super().display_product()
        print(f"  Size: {self.size} | Material: {self.material}")

    def to_record(self):
        record = super().to_record()
        record.update({"size": self.size, "material": self.material})
        return record


class Books(Product):
    category = "Books"

    def __init__(self, product_id, name, brand, price, stock, author, publisher):
        super().__init__(product_id, name, brand, price, stock)
        self.author = author
        self.publisher = publisher

    def display_product(self):
        super().display_product()
        print(f"  Author: {self.author} | Publisher: {self.publisher}")

    def to_record(self):
        record = super().to_record()
        record.update({"author": self.author, "publisher": self.publisher})
        return record


def build_products():
    """Return 30 objects across the three child classes."""
    return [
        Electronics("P001", "Laptop", "Dell", 65000, 15, "2 Years", "Inspiron 15"),
        Electronics("P002", "Smartphone", "Samsung", 42000, 22, "1 Year", "Galaxy A55"),
        Electronics("P003", "Tablet", "Apple", 55000, 8, "1 Year", "iPad Air"),
        Electronics("P004", "Smart TV", "Sony", 72000, 6, "2 Years", "Bravia X80L"),
        Electronics("P005", "Headphones", "JBL", 6500, 35, "1 Year", "Tune 770NC"),
        Electronics("P006", "Smartwatch", "Noise", 4999, 28, "1 Year", "ColorFit Pro"),
        Electronics("P007", "Camera", "Canon", 58000, 5, "2 Years", "EOS 1500D"),
        Electronics("P008", "Bluetooth Speaker", "Boat", 2999, 40, "1 Year", "Stone 1200"),
        Electronics("P009", "Monitor", "LG", 18500, 12, "3 Years", "UltraGear 24"),
        Electronics("P010", "Keyboard", "Logitech", 2500, 45, "1 Year", "K380"),
        Clothing("P011", "Formal Shirt", "Van Heusen", 2499, 30, "L", "Cotton"),
        Clothing("P012", "Denim Jeans", "Levis", 3499, 25, "32", "Denim"),
        Clothing("P013", "T-Shirt", "Puma", 1499, 50, "M", "Cotton"),
        Clothing("P014", "Jacket", "Adidas", 5999, 9, "XL", "Polyester"),
        Clothing("P015", "Kurta", "Manyavar", 3999, 18, "L", "Silk Blend"),
        Clothing("P016", "Saree", "Biba", 4499, 14, "Free Size", "Cotton Silk"),
        Clothing("P017", "Hoodie", "Nike", 3299, 21, "M", "Fleece"),
        Clothing("P018", "Track Pants", "Reebok", 2199, 27, "L", "Polyester"),
        Clothing("P019", "Sweater", "Allen Solly", 2899, 7, "M", "Wool"),
        Clothing("P020", "Cargo Trousers", "Roadster", 2699, 16, "34", "Cotton"),
        Books("P021", "Python Crash Course", "No Starch Press", 899, 32, "Eric Matthes", "No Starch Press"),
        Books("P022", "Atomic Habits", "Penguin", 599, 48, "James Clear", "Penguin"),
        Books("P023", "The Alchemist", "HarperCollins", 399, 42, "Paulo Coelho", "HarperCollins"),
        Books("P024", "Clean Code", "Pearson", 799, 11, "Robert C. Martin", "Pearson"),
        Books("P025", "Deep Work", "Piatkus", 549, 24, "Cal Newport", "Piatkus"),
        Books("P026", "Ikigai", "Random House", 499, 38, "Hector Garcia", "Random House"),
        Books("P027", "Rich Dad Poor Dad", "Plata", 450, 29, "Robert Kiyosaki", "Plata"),
        Books("P028", "Think Like a Monk", "Simon & Schuster", 650, 8, "Jay Shetty", "Simon & Schuster"),
        Books("P029", "Wings of Fire", "Universities Press", 375, 36, "A. P. J. Abdul Kalam", "Universities Press"),
        Books("P030", "The Psychology of Money", "Jaico", 525, 20, "Morgan Housel", "Jaico"),
    ]


def write_products(products):
    """Create products.csv and write the first 27 products with open/write."""
    with open(PRODUCTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=PRODUCT_FIELDS)
        writer.writeheader()
        writer.writerows(product.to_record() for product in products[:27])


def append_products(products):
    """Append the final three products with open/append."""
    with open(PRODUCTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=PRODUCT_FIELDS)
        writer.writerows(product.to_record() for product in products[27:])


def read_product_records():
    """Read product records using normal Python file handling."""
    with open(PRODUCTS_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_sales(products):
    """Create 62 rows: 60 transactions plus two deliberate duplicates."""
    cities = [" Bangalore ", "DELHI", "mumbai", "Chennai", "HYDERABAD", "Pune"]
    payments = ["UPI", "Credit Card", "debit card", "Cash", "Net Banking"]
    transactions = []

    for index in range(60):
        product = products[(index * 7) % len(products)]
        category = product.category.lower() if index % 9 == 0 else product.category
        product_name = f" {product.name} " if index % 8 == 0 else product.name
        transactions.append(
            {
                "transaction_id": f"TXN{index + 1:03d}",
                "product_id": product.product_id,
                "product_name": product_name,
                "category": category,
                "quantity": 1 + (index * 3) % 5,
                "price": product.price,
                "customer_city": cities[index % len(cities)],
                "payment_method": payments[index % len(payments)],
            }
        )

    transactions.extend([transactions[10].copy(), transactions[35].copy()])
    with open(SALES_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=SALES_FIELDS)
        writer.writeheader()
        writer.writerows(transactions)


def analyze_and_generate_reports():
    """Clean both CSV datasets, analyze them, and generate all reports."""
    sales_df = pd.read_csv(SALES_FILE)
    products_df = pd.read_csv(PRODUCTS_FILE)
    raw_sales_shape = sales_df.shape

    # Data cleaning: remove duplicates, trim text, standardize capitalization,
    # convert numeric values, and remove unusable rows.
    sales_df = sales_df.drop_duplicates().copy()
    text_columns = [
        "transaction_id",
        "product_id",
        "product_name",
        "category",
        "customer_city",
        "payment_method",
    ]
    for column in text_columns:
        sales_df[column] = sales_df[column].astype("string").str.strip()

    sales_df["transaction_id"] = sales_df["transaction_id"].str.upper()
    sales_df["product_id"] = sales_df["product_id"].str.upper()
    sales_df["product_name"] = sales_df["product_name"].str.title()
    sales_df["category"] = sales_df["category"].str.title()
    sales_df["customer_city"] = sales_df["customer_city"].str.title()
    sales_df["payment_method"] = sales_df["payment_method"].str.title().replace(
        {"Upi": "UPI"}
    )
    sales_df["quantity"] = pd.to_numeric(sales_df["quantity"], errors="coerce")
    sales_df["price"] = pd.to_numeric(sales_df["price"], errors="coerce")
    sales_df = sales_df.dropna(subset=["product_id", "quantity", "price"])
    sales_df["quantity"] = sales_df["quantity"].astype("int64")
    sales_df["price"] = sales_df["price"].astype("float64")

    # A DataFrame column is a Series. This Series stores transaction revenue.
    revenue_series = sales_df["quantity"] * sales_df["price"]
    sales_df["revenue"] = revenue_series

    total_transactions = len(sales_df)
    total_quantity = int(sales_df["quantity"].sum())
    total_revenue = float(sales_df["revenue"].sum())
    average_transaction = float(sales_df["revenue"].mean())
    highest_transaction = sales_df.loc[sales_df["revenue"].idxmax()]
    lowest_transaction = sales_df.loc[sales_df["revenue"].idxmin()]

    product_sales = sales_df.groupby("product_name").agg(
        quantity_sold=("quantity", "sum"),
        revenue=("revenue", "sum"),
    ).sort_values(["quantity_sold", "revenue"], ascending=False)
    best_selling = product_sales.iloc[0]
    lowest_selling = product_sales.sort_values(
        ["quantity_sold", "revenue"], ascending=True
    ).iloc[0]

    category_sales = sales_df.groupby("category")["quantity"].sum().sort_values(ascending=False)
    category_revenue = sales_df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    product_revenue = sales_df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)
    city_revenue = sales_df.groupby("customer_city")["revenue"].sum().sort_values(ascending=False)
    payment_distribution = sales_df["payment_method"].value_counts()
    top_five = product_sales.head(5)
    bottom_five = product_sales.sort_values(
        ["quantity_sold", "revenue"], ascending=True
    ).head(5)

    average_price = float(products_df["price"].mean())
    maximum_price = float(products_df["price"].max())
    minimum_price = float(products_df["price"].min())
    low_stock = products_df[products_df["stock"] < 10].sort_values("stock")
    above_average = products_df[products_df["price"] > average_price].sort_values(
        "price", ascending=False
    )

    product_report = products_df.merge(
        product_sales.reset_index(),
        left_on="name",
        right_on="product_name",
        how="left",
    ).drop(columns="product_name")
    product_report[["quantity_sold", "revenue"]] = product_report[
        ["quantity_sold", "revenue"]
    ].fillna(0)
    product_report["quantity_sold"] = product_report["quantity_sold"].astype(int)
    product_report = product_report.sort_values("revenue", ascending=False)

    city_report = sales_df.groupby("customer_city").agg(
        total_transactions=("transaction_id", "count"),
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
    ).sort_values("total_revenue", ascending=False)

    category_report = sales_df.groupby("category").agg(
        total_transactions=("transaction_id", "count"),
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
        average_transaction_value=("revenue", "mean"),
    ).sort_values("total_revenue", ascending=False)

    OUTPUT_DIR.mkdir(exist_ok=True)
    sales_df.to_csv(OUTPUT_DIR / "cleaned_sales.csv", index=False)
    product_report.to_csv(OUTPUT_DIR / "product_report.csv", index=False)
    city_report.to_csv(OUTPUT_DIR / "city_sales_report.csv")
    category_report.to_csv(OUTPUT_DIR / "category_report.csv")

    summary_lines = [
        "RETAIL STORE SALES REPORT",
        "=" * 50,
        f"Raw Sales Shape: {raw_sales_shape}",
        f"Cleaned Sales Shape: {sales_df.shape}",
        f"Total Transactions: {total_transactions}",
        f"Total Quantity Sold: {total_quantity}",
        f"Total Revenue: ₹{total_revenue:,.2f}",
        f"Average Transaction Value: ₹{average_transaction:,.2f}",
        f"Highest-Value Transaction: {highest_transaction['transaction_id']} "
        f"(₹{highest_transaction['revenue']:,.2f})",
        f"Lowest-Value Transaction: {lowest_transaction['transaction_id']} "
        f"(₹{lowest_transaction['revenue']:,.2f})",
        f"Best-Selling Product: {product_sales.index[0]} "
        f"({int(best_selling['quantity_sold'])} units)",
        f"Lowest-Selling Product: {product_sales.sort_values(['quantity_sold', 'revenue']).index[0]} "
        f"({int(lowest_selling['quantity_sold'])} units)",
        f"Highest Revenue Category: {category_revenue.index[0]}",
        f"Highest Revenue City: {city_revenue.index[0]}",
        f"Average Product Price: ₹{average_price:,.2f}",
        f"Maximum Product Price: ₹{maximum_price:,.2f}",
        f"Minimum Product Price: ₹{minimum_price:,.2f}",
        "",
        "SALES CATEGORY-WISE",
        category_sales.to_string(),
        "",
        "REVENUE CATEGORY-WISE",
        category_revenue.to_string(float_format=lambda value: f"₹{value:,.2f}"),
        "",
        "REVENUE PRODUCT-WISE",
        product_revenue.to_string(float_format=lambda value: f"₹{value:,.2f}"),
        "",
        "REVENUE CITY-WISE",
        city_revenue.to_string(float_format=lambda value: f"₹{value:,.2f}"),
        "",
        "PAYMENT-METHOD DISTRIBUTION",
        payment_distribution.to_string(),
        "",
        "TOP 5 PRODUCTS",
        top_five.to_string(float_format=lambda value: f"{value:,.2f}"),
        "",
        "BOTTOM 5 PRODUCTS",
        bottom_five.to_string(float_format=lambda value: f"{value:,.2f}"),
        "",
        "PRODUCTS WITH STOCK BELOW 10",
        low_stock[["product_id", "name", "stock"]].to_string(index=False),
        "",
        "PRODUCTS PRICED ABOVE AVERAGE",
        above_average[["product_id", "name", "price"]].to_string(index=False),
    ]
    with open(OUTPUT_DIR / "sales_summary.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(summary_lines))

    print("\n".join(summary_lines[:18]))
    print("\nGenerated reports:")
    for report in sorted(OUTPUT_DIR.iterdir()):
        print(f"- {report.name}")


def main():
    products = build_products()

    print("PRODUCT CLASS AND INHERITANCE DEMONSTRATION")
    print("=" * 50)
    for product in (products[0], products[10], products[20]):
        product.display_product()
    products[0].update_stock(5)
    print(f"\nUpdated {products[0].name} stock: {products[0].stock}")

    write_products(products)
    append_products(products)
    records = read_product_records()
    print(f"Product records read with file handling: {len(records)}")

    write_sales(products)
    analyze_and_generate_reports()


if __name__ == "__main__":
    main()
