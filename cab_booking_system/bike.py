""" Bike class that inherits the Vehicle class. """
from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_no, brand, driver_name, price_per_km):
        super().__init__(vehicle_no, brand, driver_name, price_per_km)

    def display_info(self):
        print("\n--- Bike Details ---")
        super().display_info()
