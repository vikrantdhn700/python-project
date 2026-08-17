"""Base user model for the e-learning platform."""


class User:
    """Parent class containing information shared by all platform users."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        if user_id <= 0:
            raise ValueError("User ID must be positive.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if "@" not in email:
            raise ValueError("A valid email address is required.")

        self.user_id = user_id
        self.name = name
        self.email = email

    def display_profile(self) -> None:
        print(f"ID: {self.user_id} | Name: {self.name} | Email: {self.email}")
