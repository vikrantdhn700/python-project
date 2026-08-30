import sys
from pathlib import Path

import pandas as pd


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


PROJECT_DIR = Path(__file__).resolve().parent
DIRTY_FILE = PROJECT_DIR / "dirty_customer_data.csv"
CLEANED_FILE = PROJECT_DIR / "cleaned_customer_data.csv"


def create_messy_dataset():
    """Create 120 deliberately messy customer records."""
    names = [
        "aarav sharma",
        "MEERA IYER",
        "Rohan Verma",
        "ananya singh",
        "VIKRAM PATEL",
        "sneha reddy",
        "Arjun Nair",
        "PRIYA DAS",
        "kabir khan",
        "Neha Joshi",
    ]
    cities = [
        "bangalore",
        "DELHI",
        "Mumbai",
        " chennai ",
        "HYDERABAD",
        "pune",
        " Kolkata",
        "ahmedabad ",
        "JAIPUR",
        "lucknow",
    ]

    records = []
    for index in range(1, 111):
        name = names[(index - 1) % len(names)]
        city = cities[(index - 1) % len(cities)]
        email_name = name.strip().lower().replace(" ", ".")

        if index % 29 == 0:
            name = ""
        elif index % 4 == 0:
            name = f"  {name}  "

        if index % 14 == 0:
            city = ""
        elif index % 9 == 0:
            city = f"  {city.strip()}  "

        if index % 13 == 0:
            age = ""
        elif index % 17 == 0:
            age = "unknown"
        elif index % 19 == 0:
            age = "twenty five"
        else:
            age = str(20 + index % 45)

        if index % 12 == 0:
            email = ""
        elif index % 8 == 0:
            email = f"  {email_name.upper()}@EXAMPLE.COM  "
        else:
            email = f"{email_name}{index}@example.com"

        if index % 11 == 0:
            purchase_amount = ""
        elif index % 23 == 0:
            purchase_amount = "not available"
        elif index % 7 == 0:
            purchase_amount = "₹1,250.50"
        else:
            purchase_amount = str(500 + index * 37.5)

        if index % 10 == 0:
            rating = ""
        elif index % 16 == 0:
            rating = "five"
        else:
            rating = str(1 + index % 5)

        records.append(
            {
                "customer_id": f" c{index:03d} " if index % 6 == 0 else f"C{index:03d}",
                "name": name,
                "age": age,
                "city": city,
                "email": email,
                "purchase_amount": purchase_amount,
                "rating": rating,
            }
        )

    # Add ten exact duplicate rows.
    records.extend(record.copy() for record in records[20:30])
    pd.DataFrame(records).to_csv(DIRTY_FILE, index=False)


def clean_customer_data():
    df = pd.read_csv(DIRTY_FILE)
    original_shape = df.shape

    print("\nDIRTY DATASET BEFORE CLEANING")
    print("=" * 80)
    print(df.to_string(index=False))
    print(f"\nOriginal shape: {original_shape}")

    # Detect missing data and count missing values.
    missing_data = df.isnull()
    print("\nMissing-value detection using isnull():")
    print(missing_data.head(10).to_string(index=False))
    print("\nMissing values in each column using isnull().sum():")
    print(df.isnull().sum())

    # Demonstrate the rows retained if every missing value were dropped.
    complete_rows = df.dropna()
    print(f"\nShape returned by dropna(): {complete_rows.shape}")

    # Detect and remove exact duplicate rows.
    print(f"Duplicate rows detected: {df.duplicated().sum()}")
    df = df.drop_duplicates().copy()

    # Remove rows missing essential identifying information.
    df = df.dropna(subset=["customer_id", "name"])

    # Clean string columns with strip, lower, upper, and title.
    df["customer_id"] = df["customer_id"].astype(str).str.strip().str.upper()
    df["name"] = df["name"].astype(str).str.strip().str.title()
    df["city"] = df["city"].astype("string").str.strip().str.title()
    df["email"] = df["email"].astype("string").str.strip().str.lower()

    # Standardize values using replace().
    df["city"] = df["city"].replace(
        {"Bengaluru": "Bangalore", "Unknown City": "Unknown"}
    )
    df["age"] = df["age"].replace(
        {"twenty five": "25", "unknown": pd.NA}
    )
    df["rating"] = df["rating"].replace({"five": "5"})
    df["purchase_amount"] = df["purchase_amount"].replace(
        {"not available": pd.NA}
    )

    # Convert invalid numeric text to missing values before filling it.
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["purchase_amount"] = pd.to_numeric(
        df["purchase_amount"]
        .astype("string")
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Handle remaining missing values using fillna().
    df["age"] = df["age"].fillna(df["age"].median())
    df["city"] = df["city"].fillna("Unknown")
    df["email"] = df["email"].fillna("not-provided@example.com")
    df["purchase_amount"] = df["purchase_amount"].fillna(
        df["purchase_amount"].median()
    )
    df["rating"] = df["rating"].fillna(df["rating"].median())

    # Assign appropriate final data types using astype().
    df["customer_id"] = df["customer_id"].astype("string")
    df["name"] = df["name"].astype("string")
    df["age"] = df["age"].round().astype("int64")
    df["city"] = df["city"].astype("string")
    df["email"] = df["email"].astype("string")
    df["purchase_amount"] = df["purchase_amount"].astype("float64")
    df["rating"] = df["rating"].astype("float64")

    cleaned_shape = df.shape
    df.to_csv(CLEANED_FILE, index=False)

    print("\nCLEAN DATASET AFTER CLEANING")
    print("=" * 80)
    print(df.to_string(index=False))
    print(f"\nShape before cleaning: {original_shape}")
    print(f"Shape after cleaning:  {cleaned_shape}")
    print("\nFinal data types:")
    print(df.dtypes)
    print("\nRemaining missing values:")
    print(df.isnull().sum())
    print(f"\nCleaned data saved to: {CLEANED_FILE}")


def main():
    create_messy_dataset()
    clean_customer_data()


if __name__ == "__main__":
    main()
