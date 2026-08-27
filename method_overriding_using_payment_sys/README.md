# Payment System Using Method Overriding

This Python project demonstrates **method overriding** with a simple payment
processing system.

## Method Overriding

Method overriding happens when a child class defines a method with the same name
as a method in its parent class. The child class provides its own version of the
method while keeping a common interface.

In this project, every payment class overrides `process_payment()` to display
information specific to that payment method.

## Parent Method

The `Payment` class is the parent class. It defines the common
`process_payment(amount)` method:

```python
class Payment:
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using a general payment method")
```

This method provides default behavior that child classes can replace.

## Child Implementation

The following child classes inherit from `Payment`:

- `CreditCardPayment`
- `UPIPayment`
- `NetBankingPayment`
- `WalletPayment`

Each child class provides a different implementation of `process_payment()`.
For example:

```python
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using UPI")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Credit Card")
```

## Runtime Behavior

At runtime, Python selects the overridden method based on the actual object in
the list. This is runtime polymorphism:

```python
payment_methods = [
    UPIPayment(),
    CreditCardPayment(),
    NetBankingPayment(),
    WalletPayment(),
]

for payment_method in payment_methods:
    payment_method.process_payment(5000)
```

Although every object is used through the same `process_payment()` interface,
each one produces payment-specific behavior.

## Run the Program

```bash
python main.py
```

Expected output:

```text
Processing ₹5000 using UPI
Processing ₹5000 using Credit Card
Processing ₹5000 using Net Banking
Processing ₹5000 using Wallet
```
