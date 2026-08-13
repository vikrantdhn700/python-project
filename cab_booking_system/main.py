""" Main module for the cab booking system """
from bike import Bike
from car import Car


def main() -> None:
    car1 = Car("JH-10-1234", "Toyota", "John Doe", 15)
    car2 = Car("JH-01-5678", "Hyundai", "Alice Johnson", 12)

    bike1 = Bike("JH-02-5678", "Honda", "Jane Smith", 10)
    bike2 = Bike("JH-10-1234", "Yamaha", "Bob Brown", 8)

    vehicles = [car1, car2, bike1, bike2]

    while True:
        print("\n==============================")
        print("      CAB BOOKING SYSTEM")
        print("==============================")

        print("\nAvailable Vehicles:")

        for index, vehicle in enumerate(vehicles, start=1):
            print(f"{index}. {vehicle.__class__.__name__} - {vehicle.vehicle_no} {vehicle.brand} (Driver: {vehicle.driver_name}, Price per KM: ₹{vehicle.price_per_km})")

        print("==============================")

        length_vehicles = len(vehicles)

        choice = int(
            input(f"Select a vehicle by number (or '{length_vehicles + 1}' to quit): "))

        if choice == length_vehicles + 1:
            break

        try:
            if not 1 <= choice <= len(vehicles) + 1:
                raise ValueError(
                    f"Invalid choice. Please select a number between 1 and {len(vehicles) + 1}.")

            selected_vehicle = vehicles[choice - 1]
            distance = float(
                input(f"Enter distance traveled for {selected_vehicle.vehicle_no} (in KM): "))
            fare = selected_vehicle.calculate_fare(distance)
            print("\n--- Fare Details ---")
            print(f"Driver: {selected_vehicle.driver_name}\n")
            print(
                f"Vehicle: {selected_vehicle.vehicle_no} ({selected_vehicle.brand})\n")
            print(f"Distance traveled: {distance} KM\n")
            print(f"Price per KM: ₹{selected_vehicle.price_per_km}\n")
            print(f"Total fare for {distance} KM: ₹{fare}\n")
        except (ValueError, IndexError) as e:
            print(f"Error - {e}")


if __name__ == "__main__":
    main()
