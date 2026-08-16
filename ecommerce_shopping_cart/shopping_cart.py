"""Shopping cart module for the e-commerce application."""


class ShoppingCart:
    def __init__(self):
        self.items = {}

    @staticmethod
    def is_product_available(product, quantity=1):
        return product.is_available(quantity)

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        if not self.is_product_available(product, quantity):
            print(
                f"Cannot add {quantity} x {product.name}: "
                f"only {product.available_stock} in stock."
            )
            return False

        product.reduce_stock(quantity)
        self.items[product] = self.items.get(product, 0) + quantity
        print(f"Added {quantity} x {product.name} to the cart.")
        return True

    def remove_product(self, product, quantity=None):
        if product not in self.items:
            print(f"{product.name} is not in the cart.")
            return False

        cart_quantity = self.items[product]
        quantity = cart_quantity if quantity is None else quantity

        if quantity <= 0 or quantity > cart_quantity:
            print(f"Invalid quantity for {product.name}.")
            return False

        product.restore_stock(quantity)
        remaining = cart_quantity - quantity
        if remaining == 0:
            del self.items[product]
        else:
            self.items[product] = remaining

        print(f"Removed {quantity} x {product.name} from the cart.")
        return True

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_selected_products(self):
        print("\nSelected products:")
        if not self.items:
            print("The cart is empty.")
            return

        for product, quantity in self.items.items():
            subtotal = product.price * quantity
            print(
                f"- {product.name}: {quantity} x ${product.price:.2f} "
                f"= ${subtotal:.2f}"
            )
        print(f"Total amount: ${self.calculate_total():.2f}")
