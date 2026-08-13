""" Car class that inherits the Vehicle class """
from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, vehicle_no, brand, driver_name, price_per_km):
        super().__init__(vehicle_no, brand, driver_name, price_per_km)

    def display_info(self):
        print("\n--- Car Details ---")
        super().display_info()
