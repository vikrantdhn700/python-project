"""Customer model for the online food ordering system."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    """A customer who can place an order."""

    customer_id: int
    name: str
    phone_number: str

    def __post_init__(self) -> None:
        if self.customer_id <= 0:
            raise ValueError("Customer ID must be positive.")
        if not self.name.strip() or not self.phone_number.strip():
            raise ValueError("Customer name and phone number cannot be empty.")
