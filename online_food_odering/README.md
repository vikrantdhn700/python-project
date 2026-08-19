# Online Food Ordering System Using Python OOP

## Project Overview

This project is a small console-based Online Food Ordering System developed in
Python. It demonstrates how object-oriented programming can model real-world
entities such as restaurants, menu items, customers, and orders.

The program allows a restaurant to maintain a menu, customers to place orders,
multiple food items and quantities to be added to each order, and the total bill
to be calculated and displayed as a formatted order summary.

The demonstration includes:

- One restaurant named **Spice Garden**.
- Five food items belonging to different categories.
- Two customers and two separate orders.
- Multiple items and quantities in each order.
- Automatic line-total and final-total calculations.

The project uses only Python's standard library, so no external packages are
required.

## Project Structure

```text
online_food_odering/
|-- customer.py      # Defines the Customer class
|-- food_item.py     # Defines the FoodItem class
|-- restaurant.py    # Defines the Restaurant class and menu behavior
|-- order.py         # Defines the Order class and billing behavior
|-- main.py          # Creates objects and runs the demonstration
`-- README.md        # Complete project documentation
```

Each main class is stored in a separate module. This makes the project easier to
read, test, maintain, and expand. The classes are imported wherever they are
needed instead of placing the entire application in one large file.

## OOP Design

The application contains four main domain classes:

```text
Restaurant
    |
    +-- maintains a menu of FoodItem objects

Customer
    |
    +-- places an Order

Order
    |-- belongs to one Customer
    |-- belongs to one Restaurant
    +-- contains FoodItem objects and their quantities
```

The classes use composition and association rather than inheritance because a
restaurant, food item, customer, and order are different kinds of objects. For
example, an order is not a type of customer; an order is associated with a
customer. Similarly, a restaurant contains food items on its menu.

This design demonstrates several OOP principles:

- **Encapsulation:** Menu and order collections are stored in attributes that
  begin with an underscore, such as `_menu` and `_items`.
- **Abstraction:** Callers use methods such as `add_item()` and
  `calculate_total()` without knowing the internal implementation.
- **Composition:** An `Order` contains references to a `Customer`, a
  `Restaurant`, and several `FoodItem` objects.
- **Data validation:** Each class checks important values before accepting them.
- **Separation of responsibilities:** Each class manages information and
  behavior related to its own role.

## Detailed File Explanation

### `customer.py`

This file defines the `Customer` class, which represents a person placing an
order.

The file imports `dataclass` from Python's standard `dataclasses` module. A data
class automatically provides useful methods such as an initializer, readable
representation, and equality comparison based on the declared fields.

#### `Customer` attributes

The class contains three attributes:

- `customer_id`: A positive integer used to identify the customer.
- `name`: The customer's full name.
- `phone_number`: The customer's contact number.

The class is declared with `@dataclass(frozen=True)`. The `frozen=True` option
makes a customer object immutable after creation. This prevents accidental
changes to identity information while an order is being processed.

#### `Customer.__post_init__()`

Because the initializer is generated automatically by `@dataclass`, validation
is placed in `__post_init__()`. Python calls this method immediately after the
generated initializer.

It performs the following checks:

- The customer ID must be greater than zero.
- The customer name cannot be empty or contain only spaces.
- The phone number cannot be empty or contain only spaces.

If any check fails, the method raises `ValueError` with an explanatory message.

### `food_item.py`

This file defines the `FoodItem` class, representing one item available on a
restaurant's menu.

It imports both `dataclass` and `Decimal`. The `Decimal` class is used for prices
because decimal arithmetic is safer for currency than binary floating-point
arithmetic. It preserves exact decimal values during bill calculations.

#### `FoodItem` attributes

Each food item contains:

- `name`: The display name, such as `Margherita Pizza`.
- `category`: The type of food, such as `Main Course` or `Beverage`.
- `price`: The unit price stored as a `Decimal` value.

`FoodItem` also uses `@dataclass(frozen=True)`. Immutability prevents the name,
category, or price from changing after the item has been added to a menu or an
order. A frozen data class is also hashable, allowing `FoodItem` objects to be
used as dictionary keys inside `Order`.

#### `FoodItem.__post_init__()`

This validation method ensures that:

- The item name is not empty.
- The category is not empty.
- The price is not negative.

A zero price is allowed, which means the application could support a free item
or promotional product. Invalid data causes `ValueError`.

### `restaurant.py`

This file defines the `Restaurant` class. It imports `FoodItem` because the
restaurant menu stores `FoodItem` objects.

#### `Restaurant.__init__(name)`

The constructor validates that the restaurant name is not empty. It then creates:

- `name`: The public restaurant name.
- `_menu`: An initially empty list of `FoodItem` objects.

The leading underscore in `_menu` indicates that the list is intended for
internal class use. Other parts of the program should interact with the menu
through the provided property and methods.

#### `Restaurant.menu`

This read-only property returns the menu as a tuple:

```python
@property
def menu(self) -> tuple[FoodItem, ...]:
    return tuple(self._menu)
```

Returning a tuple prevents outside code from directly adding, removing, or
reordering entries in the restaurant's internal list. This is an example of
encapsulation: the class keeps control over how its data is modified.

#### `Restaurant.add_food_item(item)`

This method adds a `FoodItem` object to the internal menu. The main program calls
it once for each of the five demonstration items.

#### `Restaurant.offers(item)`

This method returns `True` when the supplied food item exists on the restaurant's
menu and `False` otherwise. The `Order` class uses it to prevent customers from
ordering items that the selected restaurant does not offer.

### `order.py`

This file contains the main ordering and billing logic. It imports `Decimal`,
`Customer`, `FoodItem`, and `Restaurant` because an order works with objects from
all three domain classes.

#### `Order.__init__(order_id, restaurant, customer)`

The constructor creates an order associated with exactly one restaurant and one
customer. It stores:

- `order_id`: A positive integer identifying the order.
- `restaurant`: The `Restaurant` from which food is being ordered.
- `customer`: The `Customer` who placed the order.
- `_items`: A dictionary mapping each `FoodItem` to its ordered quantity.

The order ID must be greater than zero. An invalid ID raises `ValueError`.

Using a dictionary for `_items` provides two useful behaviors. Each food item is
stored only once, and its value records the total quantity ordered. Adding the
same item again increases its existing quantity instead of creating a duplicate
line.

#### `Order.add_item(item, quantity=1)`

This method adds food to the order. The default quantity is `1`, so callers may
omit the quantity when ordering a single item:

```python
order.add_item(pizza)
```

They can provide a quantity for multiple units:

```python
order.add_item(fries, 2)
```

Before changing the order, the method checks that the restaurant offers the item
and that the quantity is positive. It raises `ValueError` when either condition
is not satisfied.

The dictionary's `get()` method retrieves the existing quantity or returns zero
for a new item. The supplied quantity is then added to that value:

```python
self._items[item] = self._items.get(item, 0) + quantity
```

#### `Order.calculate_total()`

This method calculates the complete bill. For each dictionary entry, it
multiplies the food item's unit price by its quantity and adds all resulting line
amounts together.

The summation begins with `Decimal("0.00")`, ensuring that the result remains a
`Decimal` even when the order has no items. The method returns the total rather
than printing it, so it can be reused in other features such as payment handling
or invoice generation.

```text
Order total = sum of (food item price x ordered quantity)
```

#### `Order.display_summary()`

This method prints a complete, formatted receipt containing:

- Order ID.
- Restaurant name.
- Customer name, ID, and phone number.
- Food item name and category.
- Quantity and line amount for each item.
- Final total bill.

Format specifications such as `<22`, `>5`, and `.2f` align the table columns and
display every currency value with exactly two decimal places. The final total is
obtained by calling `calculate_total()` rather than repeating the billing logic.

### `main.py`

This is the application entry point and demonstration program. It imports all
four domain classes and `Decimal`.

#### Demonstration flow

The `main()` function performs these steps:

1. Creates the `Spice Garden` restaurant.
2. Creates five `FoodItem` objects with names, categories, and prices.
3. Adds all five food items to the restaurant menu.
4. Creates the first customer, Aarav Sharma.
5. Creates order `1001` and adds pizza, two fries, and a shake.
6. Creates the second customer, Meera Patel.
7. Creates order `1002` and adds two burgers, biryani, and two shakes.
8. Displays the formatted summary for both orders.

Prices are created from strings, such as `Decimal("249.00")`. Constructing a
`Decimal` from a string preserves the exact value intended for currency.

The final condition is:

```python
if __name__ == "__main__":
    main()
```

It runs the demonstration only when `main.py` is executed directly. Importing
the file into another program will not automatically display the sample orders.

## Sample Data and Bill Calculations

The restaurant menu contains the following five items:

| Food Item | Category | Unit Price |
|---|---|---:|
| Margherita Pizza | Main Course | Rs. 249.00 |
| Veg Burger | Fast Food | Rs. 129.00 |
| Paneer Biryani | Main Course | Rs. 219.00 |
| French Fries | Starter | Rs. 99.00 |
| Chocolate Shake | Beverage | Rs. 149.00 |

### First customer order

| Food Item | Quantity | Calculation | Amount |
|---|---:|---:|---:|
| Margherita Pizza | 1 | 249.00 x 1 | Rs. 249.00 |
| French Fries | 2 | 99.00 x 2 | Rs. 198.00 |
| Chocolate Shake | 1 | 149.00 x 1 | Rs. 149.00 |
| **Total** | | | **Rs. 596.00** |

### Second customer order

| Food Item | Quantity | Calculation | Amount |
|---|---:|---:|---:|
| Veg Burger | 2 | 129.00 x 2 | Rs. 258.00 |
| Paneer Biryani | 1 | 219.00 x 1 | Rs. 219.00 |
| Chocolate Shake | 2 | 149.00 x 2 | Rs. 298.00 |
| **Total** | | | **Rs. 775.00** |

## Requirements

- Python 3.9 or newer is recommended because the project uses built-in generic
  type hints such as `list[FoodItem]` and `dict[FoodItem, int]`.
- No third-party libraries or package installation are required.

## How to Run

Open PowerShell or another terminal, navigate to the project directory, and run:

```powershell
cd D:\julysuper30\online_food_odering
python main.py
```

On Windows, the Python launcher can also be used:

```powershell
py main.py
```

## Expected Output

The program prints two formatted order summaries. The first summary shows a
total of `Rs. 596.00`, and the second shows a total of `Rs. 775.00`. Each summary
also includes its order ID, restaurant, customer information, item quantities,
categories, and line amounts.

## Validation and Error Handling

The project includes the following safeguards:

- Customer IDs must be positive.
- Customer names and phone numbers cannot be empty.
- Food names and categories cannot be empty.
- Food prices cannot be negative.
- Restaurant names cannot be empty.
- Order IDs and ordered quantities must be positive.
- A food item must be on the restaurant's menu before it can be ordered.

These checks place responsibility inside the appropriate classes. This prevents
invalid objects or operations from silently entering the system and makes the
classes safer to reuse from other programs.

## Possible Future Improvements

The project could later be extended with:

- Delivery addresses and delivery charges.
- Taxes, discounts, and promotional codes.
- Menu item availability and stock quantities.
- Removing items or changing quantities in an order.
- Multiple restaurants and order status tracking.
- Payment methods and payment status.
- Database storage.
- A graphical interface, web interface, or REST API.

Because responsibilities are already separated across classes and modules, these
features can be added without placing all logic in a single file.
