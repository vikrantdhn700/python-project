"""Food item model for the online food ordering system."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class FoodItem:
    """A food item offered by a restaurant."""

    name: str
    category: str
    price: Decimal

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.category.strip():
            raise ValueError("Food name and category cannot be empty.")
        if self.price < 0:
            raise ValueError("Food price cannot be negative.")
