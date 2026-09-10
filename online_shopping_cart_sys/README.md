# Online Shopping Cart System

A simple command-line shopping cart application written in Python. Customers can choose products from a predefined catalog, add quantities to their cart, and receive an itemized invoice with a discount and final payable amount.

## Requirements

- Python 3
- No external libraries are required

## Run the Application

Open a terminal in this folder and run:

```powershell
python main.py
```

## Product Catalog

The available products and their prices are stored in the `products` dictionary inside `main.py`.

| Product | Price |
| --- | ---: |
| Laptop | Rs. 65,000 |
| Phone | Rs. 25,000 |
| Mouse | Rs. 800 |
| Keyboard | Rs. 1,200 |
| Monitor | Rs. 9,000 |
| Speaker | Rs. 2,500 |

## How to Use

1. Start the program; it displays the available products and their prices.
2. Enter a product name, such as `Laptop` or `Mouse`.
3. Enter the quantity you want to purchase.
4. Continue adding products, or enter `done` when your cart is complete.
5. Review the generated invoice, including the subtotal, discount, and final amount.

Product names are converted to title case, so entries such as `laptop` and `LAPTOP` are accepted. If the same product is added again, the application adds the new quantity to the quantity already in the cart.

## Data Structure

The application uses two dictionaries:

```python
products = {"Laptop": 65000, "Mouse": 800}
cart = {"Laptop": 1, "Mouse": 2}
```

- `products` maps each product name to its unit price.
- `cart` maps each selected product name to its chosen quantity.

## Invoice Calculation

For every item in the cart, the application calculates:

```text
Item total = unit price x quantity
```

It adds all item totals to produce the subtotal. A discount is then calculated and deducted to obtain the final amount.

```text
Final amount = subtotal - discount
```

The invoice displays the item name, quantity, unit price, each item total, subtotal, discount percentage and amount, and final amount.

## Project File

| File | Purpose |
| --- | --- |
| `main.py` | Contains the product catalog, cart input loop, and invoice calculation. |
