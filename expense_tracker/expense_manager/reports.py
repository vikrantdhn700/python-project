"""Expense reporting functions."""

import os
from pathlib import Path
from .expenses import load_expenses


log_file_path = Path(__file__).resolve().parent.parent


def monthly_summary(month):
    """Calculate total expenses for a month."""

    expenses = load_expenses()

    monthly_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    total = sum(
        float(expense["amount"])
        for expense in monthly_expenses
    )

    return monthly_expenses, total


def category_summary(month=None):
    """Generate category-wise expense summary."""

    expenses = load_expenses()

    if month:
        expenses = [
            expense
            for expense in expenses
            if expense["date"].startswith(month)
        ]

    summary = {}

    for expense in expenses:

        category = expense["category"]
        amount = float(expense["amount"])

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary


def highest_expense(month=None):
    """Find the highest expense."""

    expenses = load_expenses()

    if month:
        expenses = [
            expense
            for expense in expenses
            if expense["date"].startswith(month)
        ]

    if not expenses:
        return None

    highest = max(
        expenses,
        key=lambda expense: float(expense["amount"])
    )

    return highest


def export_report(month, filename=None):
    """Export monthly report to a text file."""

    expenses, total = monthly_summary(month)

    category_data = category_summary(month)

    highest = highest_expense(month)

    if filename is None:

        os.makedirs(log_file_path / "reports", exist_ok=True)

        filename = log_file_path / f"reports/monthly_report_{month}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:

            file.write("=" * 50 + "\n")
            file.write(f"MONTHLY EXPENSE REPORT - {month}\n")
            file.write("=" * 50 + "\n\n")

            file.write("EXPENSE DETAILS\n")
            file.write("-" * 50 + "\n")

            for expense in expenses:

                file.write(
                    f"ID: {expense['id']} | "
                    f"Date: {expense['date']} | "
                    f"Category: {expense['category']} | "
                    f"Description: {expense['description']} | "
                    f"Amount: ₹{float(expense['amount']):.2f}\n"
                )

            file.write("\n")
            file.write(f"TOTAL EXPENSE: ₹{total:.2f}\n")

            file.write("\n")
            file.write("CATEGORY-WISE SUMMARY\n")
            file.write("-" * 50 + "\n")

            for category, amount in category_data.items():

                file.write(
                    f"{category}: ₹{amount:.2f}\n"
                )

            file.write("\n")
            file.write("HIGHEST EXPENSE\n")
            file.write("-" * 50 + "\n")

            if highest:

                file.write(
                    f"Description: {highest['description']}\n"
                )

                file.write(
                    f"Category: {highest['category']}\n"
                )

                file.write(
                    f"Amount: ₹{float(highest['amount']):.2f}\n"
                )

            else:

                file.write("No expenses found.\n")

            file.write("\n")
            file.write("=" * 50 + "\n")

        return filename

    except OSError as e:
        raise OSError(
            f"Unable to export report: {e}"
        ) from e
