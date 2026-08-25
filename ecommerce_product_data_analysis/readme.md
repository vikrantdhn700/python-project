# E-commerce Product Data Analysis

A Python and Pandas project for exploring and analyzing an e-commerce product dataset. It summarizes product inventory, pricing, ratings, categories, brands, and stock levels, then exports an enriched CSV file.

## Features

The program:

- Loads product data from `products.csv`
- Displays dataset information and summary statistics
- Counts total products, unique categories, and unique brands
- Shows the number of products in each category
- Calculates the overall average product price
- Identifies the highest- and lowest-priced products
- Filters products priced above 50,000
- Filters products with ratings above 4
- Sorts products by price and rating in descending order
- Identifies products with stock below 10
- Calculates a discounted amount and final price
- Calculates average final price by category
- Calculates average rating by brand
- Finds the maximum product price in each category
- Exports the processed data to `output/final_products.csv`

## Project Structure

```text
ecommerce_product_data_analysis/
|-- main.py
|-- products.csv
|-- readme.md
`-- output/
    `-- final_products.csv
```

## Dataset

The source dataset contains 56 products from seven categories: Laptop, Mobile, Headphones, Keyboard, Monitor, Tablet, and Accessories.

| Column | Description |
|---|---|
| `product_id` | Unique product identifier |
| `product_name` | Product name |
| `category` | Product category |
| `brand` | Product brand |
| `price` | Original product price |
| `rating` | Customer rating |
| `stock` | Available inventory quantity |
| `discount` | Discount value included in the source data |

The exported dataset also contains:

| Column | Description |
|---|---|
| `discounted_amount` | 80% of the original price |
| `final_price` | Original price minus `discounted_amount`, leaving 20% of the price |

> **Calculation note:** The current script applies a fixed calculation (`price * 0.8`) and does not use the source dataset's `discount` column. Despite its name, `discounted_amount` represents 80% of the price, while `final_price` represents the remaining 20%.

## Requirements

- Python 3.8 or later
- Pandas

Install Pandas with:

```bash
python -m pip install pandas
```

## Run the Analysis

Open a terminal in the project directory and run:

```bash
python main.py
```

The analysis is printed in the terminal, and the processed dataset is written to:

```text
output/final_products.csv
```

Run the script from the project root because it uses relative file paths. Ensure that the `output` directory exists before execution.

## Current Price Calculations

The script calculates the two output fields as follows:

```text
discounted_amount = price * 0.8
final_price       = price - discounted_amount
```

For example, a product priced at 10,000 gets a `discounted_amount` of 8,000 and a `final_price` of 2,000.

## Files

- `main.py` contains the loading, inspection, filtering, sorting, aggregation, calculation, and export logic.
- `products.csv` is the source dataset containing 56 product records.
- `output/final_products.csv` is the generated dataset with the two calculated price columns.
