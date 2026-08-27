""" Method Overriding using payment system """


class Payment:
    """Base class for all payment methods."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using a general payment method")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Credit Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using UPI")


class NetBankingPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Net Banking")


class WalletPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Wallet")


def main() -> None:
    amount = 5000
    payment_methods = [
        UPIPayment(),
        CreditCardPayment(),
        NetBankingPayment(),
        WalletPayment(),
    ]

    for payment_method in payment_methods:
        payment_method.process_payment(amount)


if __name__ == "__main__":
    main()
