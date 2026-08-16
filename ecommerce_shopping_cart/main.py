""" main.py is the entry point of the application. It demonstrates the functionality of the Product and ShoppingCart classes by creating a list of products, adding them to a shopping cart, and displaying the selected products."""
from products import Product
from shopping_cart import ShoppingCart


def main() -> None:
    products = [
        Product(101, "Laptop", "Electronics", 899.99, 4),
        Product(102, "Wireless Mouse", "Electronics", 24.50, 10),
        Product(103, "Coffee Mug", "Home", 12.75, 6),
        Product(104, "Python Book", "Books", 39.99, 3),
        Product(105, "Gaming Headset", "Electronics", 79.95, 0),
    ]

    print("Available products:")
    for product in products:
        print(product)

    cart = ShoppingCart()
    print("\nCustomer shopping:")
    cart.add_product(products[0], 1)
    cart.add_product(products[1], 2)
    cart.add_product(products[2], 3)

    # A product with zero stock cannot be purchased.
    cart.add_product(products[4], 1)

    # Removing an item also restores its available stock.
    cart.remove_product(products[2], 1)
    cart.display_selected_products()


if __name__ == "__main__":
    main()
