# Sales Data Analysis with Python and Pandas

This project demonstrates Python file handling, CSV operations, and basic sales
analysis using pandas. It contains 30 sample sales transactions from different
Indian cities.

## Features

- Writes transaction data to `sales.txt` in CSV format
- Reads and displays the data using standard Python file handling
- Loads the data into a pandas DataFrame
- Calculates revenue for every transaction
- Calculates total revenue and average order value
- Finds the highest- and lowest-value orders
- Groups revenue by product and city
- Saves the processed data to `sales.csv`

## Data Format

Each transaction contains the following fields:

```text
order_id,product,quantity,price,city
101,Laptop,1,65000,Bangalore
102,Mouse,2,1200,Delhi
```

The generated `sales.csv` file also includes a `revenue` column, calculated as:

```text
revenue = quantity * price
```

## Requirements

- Python 3.8 or newer
- pandas

Install pandas with:

```bash
python -m pip install pandas
```

## Run the Project

Open a terminal in the project directory and run:

```bash
python main.py
```

The program prints the source transactions and analysis results to the terminal.
It creates or replaces these files in the project directory:

- `sales.txt` — original transaction data
- `sales.csv` — processed transaction data with revenue

## Project Structure

```text
filehandling_plus_pandas/
|-- main.py       # Data creation and analysis script
|-- README.md     # Project documentation
|-- sales.txt     # Generated when the script runs
`-- sales.csv     # Generated when the script runs
```

## Notes

Running `main.py` recreates `sales.txt` and `sales.csv`. Prices and calculated
revenue values use Indian rupees (INR).
