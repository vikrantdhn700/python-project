"""Order model for the online food ordering system."""

from decimal import Decimal

from customer import Customer
from food_item import FoodItem
from restaurant import Restaurant


class Order:
    """A customer's collection of food items from one restaurant."""

    def __init__(
        self, order_id: int, restaurant: Restaurant, customer: Customer
    ) -> None:
        if order_id <= 0:
            raise ValueError("Order ID must be positive.")
        self.order_id = order_id
        self.restaurant = restaurant
        self.customer = customer
        self._items: dict[FoodItem, int] = {}

    def add_item(self, item: FoodItem, quantity: int = 1) -> None:
        if not self.restaurant.offers(item):
            raise ValueError(f"{item.name} is not on the restaurant's menu.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self._items[item] = self._items.get(item, 0) + quantity

    def calculate_total(self) -> Decimal:
        return sum(
            (item.price * quantity for item, quantity in self._items.items()),
            start=Decimal("0.00"),
        )

    def display_summary(self) -> None:
        print("=" * 62)
        print("ORDER SUMMARY".center(62))
        print("=" * 62)
        print(f"Order ID   : {self.order_id}")
        print(f"Restaurant : {self.restaurant.name}")
        print(f"Customer   : {self.customer.name} (ID: {self.customer.customer_id})")
        print(f"Phone      : {self.customer.phone_number}")
        print("-" * 62)
        print(f"{'Item':<22} {'Category':<14} {'Qty':>5} {'Amount':>15}")
        print("-" * 62)

        for item, quantity in self._items.items():
            amount = item.price * quantity
            print(
                f"{item.name:<22} {item.category:<14} "
                f"{quantity:>5} {'Rs. ' + format(amount, '.2f'):>15}"
            )

        print("-" * 62)
        total = "Rs. " + format(self.calculate_total(), ".2f")
        print(f"{'TOTAL BILL:':<46} {total:>15}")
        print("=" * 62, end="\n\n")
