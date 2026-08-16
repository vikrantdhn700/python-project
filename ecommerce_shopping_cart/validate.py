"""Validate product details before adding them to the product list."""


def validate_product(product_id, name, category, price, available_stock, registered_ids):
    if isinstance(product_id, str):
        product_id = product_id.strip()

    if isinstance(product_id, bool) or not isinstance(product_id, (int, str)):
        raise TypeError(
            "Product ID must be a positive integer or non-empty text.")
    if product_id == "":
        raise ValueError("Product ID cannot be empty.")
    if isinstance(product_id, int) and product_id <= 0:
        raise ValueError("Numeric product ID must be greater than zero.")
    if product_id in registered_ids:
        raise ValueError(f"Product ID {product_id!r} already exists.")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Product name cannot be empty.")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Product category cannot be empty.")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Product price must be a number.")
    if price < 0:
        raise ValueError("Product price cannot be negative.")
    if isinstance(available_stock, bool) or not isinstance(available_stock, int):
        raise TypeError("Available stock must be a whole number.")
    if available_stock < 0:
        raise ValueError("Available stock cannot be negative.")

    return product_id, name.strip(), category.strip(), float(price), available_stock
