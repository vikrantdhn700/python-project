"""Run a demonstration of the online food ordering system."""

from decimal import Decimal

from customer import Customer
from food_item import FoodItem
from order import Order
from restaurant import Restaurant


def main() -> None:
    restaurant = Restaurant("Spice Garden")

    # Create at least five food items.
    pizza = FoodItem("Margherita Pizza", "Main Course", Decimal("249.00"))
    burger = FoodItem("Veg Burger", "Fast Food", Decimal("129.00"))
    biryani = FoodItem("Paneer Biryani", "Main Course", Decimal("219.00"))
    fries = FoodItem("French Fries", "Starter", Decimal("99.00"))
    shake = FoodItem("Chocolate Shake", "Beverage", Decimal("149.00"))

    for item in (pizza, burger, biryani, fries, shake):
        restaurant.add_food_item(item)

    # First customer order.
    customer_one = Customer(101, "Aarav Sharma", "9876543210")
    order_one = Order(1001, restaurant, customer_one)
    order_one.add_item(pizza)
    order_one.add_item(fries, 2)
    order_one.add_item(shake)

    # Second customer order.
    customer_two = Customer(102, "Meera Patel", "9123456780")
    order_two = Order(1002, restaurant, customer_two)
    order_two.add_item(burger, 2)
    order_two.add_item(biryani)
    order_two.add_item(shake, 2)

    order_one.display_summary()
    order_two.display_summary()


if __name__ == "__main__":
    main()
