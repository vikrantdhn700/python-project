"""Salary, tax, and bonus calculation functions."""


def calculate_bonus(monthly_salary, bonus_percentage):
    """Calculate employee bonus."""

    bonus = (
        monthly_salary
        * bonus_percentage
        / 100
    )

    return round(bonus, 2)


def calculate_gross_salary(monthly_salary, bonus):
    """Calculate gross salary."""

    gross_salary = monthly_salary + bonus

    return round(gross_salary, 2)


def calculate_tax(gross_salary):
    """
    Calculate tax using a simple progressive
    tax structure.

    """

    remaining_salary = gross_salary

    tax = 0.0

    # First slab: 0%
    first_slab = min(
        remaining_salary,
        25000
    )

    remaining_salary -= first_slab

    # Second slab: 5%
    if remaining_salary > 0:

        second_slab = min(
            remaining_salary,
            25000
        )

        tax += second_slab * 0.05

        remaining_salary -= second_slab

    # Third slab: 10%
    if remaining_salary > 0:

        third_slab = min(
            remaining_salary,
            50000
        )

        tax += third_slab * 0.10

        remaining_salary -= third_slab

    # Fourth slab: 15%
    if remaining_salary > 0:

        tax += remaining_salary * 0.15

    return round(tax, 2)


def calculate_net_salary(
    monthly_salary,
    bonus,
    tax
):
    """Calculate net salary."""

    net_salary = (
        monthly_salary
        + bonus
        - tax
    )

    return round(net_salary, 2)
