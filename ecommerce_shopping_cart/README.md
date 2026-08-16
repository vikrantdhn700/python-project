# E-Commerce Shopping Cart System

A basic command-line shopping cart application built with Python and object-oriented programming (OOP).

## Features

- Create products with an ID, name, category, price, and available stock
- Validate product information before creating a product
- Reject duplicate product IDs
- Add one or more units of a product to the cart
- Remove some or all units of a product from the cart
- Display selected products, quantities, subtotals, and the total amount
- Check product availability before adding it to the cart
- Reduce stock when products are added and restore stock when they are removed
- Prevent a product from being purchased when its stock is zero

## Project Structure

```text
ecommerce_shopping_cart/
|-- main.py            # Creates products and demonstrates a purchase
|-- products.py        # Contains the Product class
|-- shopping_cart.py   # Contains the ShoppingCart class
|-- validate.py        # Contains product validation rules
`-- README.md
```

## Validation Rules

Product data is validated by `validate_product()` in `validate.py`.

- Product ID must be a positive integer or non-empty string.
- Product ID must be unique.
- Product name cannot be empty.
- Product category cannot be empty.
- Price must be numeric and cannot be negative.
- Available stock must be a whole number and cannot be negative.
- Leading and trailing spaces are removed from text fields.

Invalid data raises a `ValueError` or `TypeError` with an explanatory message.

## Requirements

- Python 3.8 or later
- No third-party packages are required

## Running the Program

Open a terminal in the project folder and run:

```powershell
python main.py
```

The demonstration creates five products and adds multiple products to a customer's cart. It also removes one selected item and attempts to purchase a gaming headset with zero stock.

## Example Output

```text
Customer shopping:
Added 1 x Laptop to the cart.
Added 2 x Wireless Mouse to the cart.
Added 3 x Coffee Mug to the cart.
Cannot add 1 x Gaming Headset: only 0 in stock.
Removed 1 x Coffee Mug from the cart.

Selected products:
- Laptop: 1 x $899.99 = $899.99
- Wireless Mouse: 2 x $24.50 = $49.00
- Coffee Mug: 2 x $12.75 = $25.50
Total amount: $974.49
```

## OOP Classes

### `Product`

Stores product details and provides methods to check availability, reduce stock, and restore stock.

### `ShoppingCart`

Stores products and quantities selected by the customer. It provides methods to add products, remove products, check availability, display cart contents, and calculate the total amount.
