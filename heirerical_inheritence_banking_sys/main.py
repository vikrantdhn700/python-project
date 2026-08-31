""" Hirerical Inheritence """


class BankAccount:
    """Parent class containing behavior shared by every bank account."""

    def __init__(self, account_number, holder_name, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(
            f"₹{amount:,.2f} deposited into account {self.account_number}."
        )

    def display_balance(self):
        print(f"Available balance: ₹{self.balance:,.2f}")

    def account_details(self):
        print(f"Account number: {self.account_number}")
        print(f"Holder name: {self.holder_name}")
        self.display_balance()


class SavingsAccount(BankAccount):
    """Bank account that earns interest on its balance."""

    def __init__(
        self, account_number, holder_name, balance, interest_rate
    ):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def account_details(self):
        super().account_details()
        print(f"Account type: Savings Account")
        print(f"Interest rate: {self.interest_rate}%")


class CurrentAccount(BankAccount):
    """Bank account with an approved overdraft facility."""

    def __init__(
        self, account_number, holder_name, balance, overdraft_limit
    ):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def account_details(self):
        super().account_details()
        print(f"Account type: Current Account")
        print(f"Overdraft limit: ₹{self.overdraft_limit:,.2f}")


class SalaryAccount(BankAccount):
    """Bank account linked to an employer and a monthly salary."""

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        employer,
        monthly_salary,
    ):
        super().__init__(account_number, holder_name, balance)
        self.employer = employer
        self.monthly_salary = monthly_salary

    def account_details(self):
        super().account_details()
        print(f"Account type: Salary Account")
        print(f"Employer: {self.employer}")
        print(f"Monthly salary: ₹{self.monthly_salary:,.2f}")


def main() -> None:
    accounts = [
        SavingsAccount("SAV101", "Aarav Sharma", 50000, 4.5),
        SavingsAccount("SAV102", "Meera Iyer", 72500, 4.0),
        CurrentAccount("CUR201", "Bright Traders", 125000, 50000),
        CurrentAccount("CUR202", "Nova Solutions", 90000, 35000),
        SalaryAccount(
            "SAL301", "Rohan Verma", 45000, "TechNova Pvt Ltd", 80000
        ),
        SalaryAccount(
            "SAL302", "Ananya Singh", 60000, "CloudWorks Ltd", 95000
        ),
    ]

    for account in accounts:
        account.account_details()
        account.deposit(5000)
        account.display_balance()
        print("-" * 60)


if __name__ == "__main__":
    main()
