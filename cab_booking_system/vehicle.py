""" Vehicle class representing a cab booking vehicle """


class Vehicle:
    def __init__(self, vehicle_no, brand, driver_name, price_per_km):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km

    def calculate_fare(self, distance):
        return self.price_per_km * distance

    def display_info(self):
        print(f"Vehicle No: {self.vehicle_no}")
        print(f"Brand: {self.brand}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Price per KM: {self.price_per_km}")
