# Cab Booking System

A simple command-line cab booking application written in Python. It demonstrates object-oriented programming concepts such as inheritance, method overriding, and polymorphism while allowing a user to select a vehicle and calculate a trip fare.

## Features

- Lists the cars and bikes currently available for booking.
- Shows each vehicle's registration number, brand, driver, and per-kilometre rate.
- Accepts a trip distance from the user.
- Calculates the fare using the selected vehicle's rate.
- Continues accepting bookings until the user selects the quit option.

## Project Structure

```text
cab_booking_system/
|-- main.py       # CLI entry point and booking workflow
|-- vehicle.py    # Base Vehicle class and fare calculation
|-- car.py        # Car subclass
|-- bike.py       # Bike subclass
`-- README.md
```

## Requirements

- Python 3.8 or later
- No third-party packages are required

## Getting Started

1. Open a terminal in the project directory:

   ```powershell
   cd D:\julysuper30\cab_booking_system
   ```

2. Run the application:

   ```powershell
   python main.py
   ```

3. Enter the number of the vehicle you want to book.
4. Enter the travel distance in kilometres.
5. Review the calculated fare, or select the displayed quit option to exit.

## How It Works

The application creates a predefined collection of two cars and two bikes. Every vehicle inherits common data and behavior from `Vehicle`:

```python
fare = price_per_km * distance
```

`Car` and `Bike` inherit this calculation and override `display_info()` to provide a vehicle-specific heading. The main loop in `main.py` displays all vehicles, processes a selection, asks for the distance, and prints the booking details and total fare.

## Class Overview

### `Vehicle`

The base class stores:

- `vehicle_no`
- `brand`
- `driver_name`
- `price_per_km`

It also provides `calculate_fare(distance)` and `display_info()`.

### `Car` and `Bike`

Both classes inherit from `Vehicle`. They reuse its constructor and fare calculation while supplying their own headings when vehicle information is displayed.

## Example

```text
==============================
      CAB BOOKING SYSTEM
==============================

Available Vehicles:
1. Car - JH-10-1234 Toyota (Driver: John Doe, Price per KM: Rs.15)
2. Car - JH-01-5678 Hyundai (Driver: Alice Johnson, Price per KM: Rs.12)
3. Bike - JH-02-5678 Honda (Driver: Jane Smith, Price per KM: Rs.10)
4. Bike - JH-10-1234 Yamaha (Driver: Bob Brown, Price per KM: Rs.8)
```

Selecting a vehicle and entering `10` KM produces a total fare equal to ten times that vehicle's per-kilometre rate.

## Current Limitations

- Vehicle and driver records are defined directly in `main.py` and are not persisted.
- The application calculates fares but does not store booking history.
- The first vehicle-selection conversion expects numeric input; non-numeric input ends the program with a `ValueError`.
- Negative distances are currently accepted and should be prevented in a production system.
- Currency-symbol rendering depends on the terminal and source-file encoding.

## Possible Enhancements

- Validate all menu and distance input before calculating a fare.
- Add pickup and destination details.
- Load vehicles from a database or configuration file.
- Track vehicle availability and booking history.
- Add automated tests for fare calculation and input handling.
- Create a graphical or web-based interface.

## License

No license has been specified for this project.
