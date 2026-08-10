"""Custom payroll package."""

from .calculations import (
    calculate_bonus,
    calculate_tax,
    calculate_gross_salary,
    calculate_net_salary,
)

from .employees import (
    add_employee,
    find_employee,
    generate_payslip,
)


__all__ = [
    "calculate_bonus",
    "calculate_tax",
    "calculate_gross_salary",
    "calculate_net_salary",
    "add_employee",
    "find_employee",
    "generate_payslip",
]
