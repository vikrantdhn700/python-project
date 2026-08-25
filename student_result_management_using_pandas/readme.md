# Student Result Management Using Pandas

A beginner-friendly Python project that uses Pandas to load, explore, analyze, filter, sort, and enrich student result data stored in a CSV file.

## Features

The program:

- Loads student records from `students.csv`
- Displays the first and last five records
- Reports the dataset shape, row and column counts, column names, and data types
- Prints DataFrame information and descriptive statistics
- Calculates average, maximum, and minimum marks for Python, SQL, and Pandas
- Sorts students by Python marks and attendance
- Filters students with Python marks above 80
- Filters students with attendance above 75
- Selects student names with Python and Pandas marks
- Calculates each student's total and average marks
- Saves the enriched dataset to `output/processed_students.csv`

## Project Structure

```text
student_result_management_using_pandas/
|-- main.py
|-- students.csv
|-- readme.md
`-- output/
    `-- processed_students.csv
```

## Dataset

The source dataset contains 30 student records with these columns:

| Column | Description |
|---|---|
| `student_id` | Unique student identifier |
| `name` | Student's full name |
| `age` | Student's age |
| `city` | Student's city |
| `python_marks` | Marks obtained in Python |
| `sql_marks` | Marks obtained in SQL |
| `pandas_marks` | Marks obtained in Pandas |
| `attendance` | Attendance percentage |

The processed output adds:

| Column | Description |
|---|---|
| `total_marks` | Sum of Python, SQL, and Pandas marks |
| `avg_marks` | Average of the three subject marks |

## Requirements

- Python 3.8 or later
- Pandas

Install Pandas with:

```bash
python -m pip install pandas
```

## Running the Project

Open a terminal in the project directory and run:

```bash
python main.py
```

The analysis results will be printed in the terminal. The script will also create or overwrite `output/processed_students.csv` with the calculated `total_marks` and `avg_marks` columns.

> Run the script from the project root because it uses relative paths to access the input and output CSV files. Make sure the `output` directory exists before running it.

## Example Calculations

For each student, the additional fields are calculated as:

```text
total_marks = python_marks + sql_marks + pandas_marks
avg_marks   = total_marks / 3
```

## Files

- `main.py` contains all data loading, inspection, analysis, filtering, sorting, calculation, and export logic.
- `students.csv` is the source dataset.
- `output/processed_students.csv` is the generated dataset containing the original fields plus total and average marks.
