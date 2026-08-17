"""Restaurant model for the online food ordering system."""

from food_item import FoodItem


class Restaurant:
    """A restaurant and its available menu."""

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Restaurant name cannot be empty.")
        self.name = name
        self._menu: list[FoodItem] = []

    @property
    def menu(self) -> tuple[FoodItem, ...]:
        return tuple(self._menu)

    def add_food_item(self, item: FoodItem) -> None:
        self._menu.append(item)

    def offers(self, item: FoodItem) -> bool:
        return item in self._menu
