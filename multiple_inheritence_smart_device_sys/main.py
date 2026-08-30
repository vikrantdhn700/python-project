""" Multiple inheritence """


class Camera:
    """Provides camera features to a smart device."""

    def take_photo(self):
        print(f"{self.brand} {self.model} is taking a photo.")

    def record_video(self):
        print(f"{self.brand} {self.model} is recording a video.")


class MusicPlayer:
    """Provides music playback features to a smart device."""

    def play_music(self):
        print(f"Playing music on {self.brand} {self.model}.")

    def stop_music(self):
        print(f"Music stopped on {self.brand} {self.model}.")


class GPS:
    """Provides location and navigation features to a smart device."""

    def current_location(self):
        print(f"Getting the current location on {self.brand} {self.model}.")

    def navigate(self):
        print(f"Starting navigation on {self.brand} {self.model}.")


class SmartPhone(Camera, MusicPlayer, GPS):
    """A smartphone that combines camera, music, and GPS functionality."""

    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_details(self):
        print(
            f"Brand: {self.brand}, Model: {self.model}, "
            f"Price: ₹{self.price:,}, Storage: {self.storage}"
        )


def main():
    smartphones = [
        SmartPhone("Samsung", "Galaxy S24", 74999, "256 GB"),
        SmartPhone("Apple", "iPhone 15", 69900, "128 GB"),
        SmartPhone("OnePlus", "12R", 42999, "256 GB"),
    ]

    for smartphone in smartphones:
        smartphone.display_details()
        smartphone.take_photo()
        smartphone.record_video()
        smartphone.play_music()
        smartphone.stop_music()
        smartphone.current_location()
        smartphone.navigate()
        print("-" * 60)


if __name__ == "__main__":
    main()
