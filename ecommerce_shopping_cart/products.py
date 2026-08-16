""" Product module for the e-commerce shopping cart application. It defines the Product class and its associated methods for managing product details and stock availability. """
from validate import validate_product


class Product:
    """Represents a product that can be purchased."""

    _registered_ids = set()

    def __init__(self, product_id, name, category, price, available_stock):
        values = validate_product(
            product_id, name, category, price, available_stock,
            Product._registered_ids,
        )
        (
            self.product_id,
            self.name,
            self.category,
            self.price,
            self.available_stock,
        ) = values
        Product._registered_ids.add(self.product_id)

    def is_available(self, quantity=1):
        """Return True when the requested quantity is in stock."""
        return quantity > 0 and self.available_stock >= quantity

    def reduce_stock(self, quantity):
        if not self.is_available(quantity):
            raise ValueError(f"Not enough stock available for {self.name}.")
        self.available_stock -= quantity

    def restore_stock(self, quantity):
        self.available_stock += quantity

    def __str__(self):
        return (
            f"{self.product_id} - {self.name} ({self.category}) | "
            f"${self.price:.2f} | Stock: {self.available_stock}"
        )
