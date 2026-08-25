"""
This script performs various data analysis tasks on a CSV file containing student information.
"""

import pandas as pd

# Read CSV
df = pd.read_csv('students.csv')
# print(df)

# Display the first 5 rows
print("First 5 rows:\n", df.head(5))

# Display the last 5 rows
print("Last 5 rows:\n", df.tail(5))

# Display the shape of the DataFrame
print("Shape of DataFrame:", df.shape)

# Display the no of columns
print("No of columns:", df.shape[1])

# Display the no of rows
print("No of rows:", df.shape[0])

# Display the column names
print("Column names:", list(df.columns))

# Display the data types of each column
print("Data types:\n", df.dtypes)

# Get basic information
print(df.info())

# Get statistical summary
print(df.describe())

# Find the average python marks of students
avg_python_marks = df['python_marks'].mean()
print("Average Python Marks:", avg_python_marks)

# Find the average sql marks of students
avg_sql_marks = df['sql_marks'].mean()
print("Average SQL Marks:", avg_sql_marks)

# Find the average pandas marks of students
avg_pandas_marks = df['pandas_marks'].mean()
print("Average Pandas Marks:", avg_pandas_marks)

# Find Maximum marks
max_python_marks = df['python_marks'].max()
print("Maximum Python Marks:", max_python_marks)

max_sql_marks = df['sql_marks'].max()
print("Maximum SQL Marks:", max_sql_marks)

max_pandas_marks = df['pandas_marks'].max()
print("Maximum Pandas Marks:", max_pandas_marks)

# Find Minimum marks
min_python_marks = df['python_marks'].min()
print("Minimum Python Marks:", min_python_marks)

min_sql_marks = df['sql_marks'].min()
print("Minimum SQL Marks:", min_sql_marks)

min_pandas_marks = df['pandas_marks'].min()
print("Minimum Pandas Marks:", min_pandas_marks)

# Sort student by python marks in descending order
sorted_by_python = df.sort_values(by='python_marks', ascending=False)
print("Students sorted by Python Marks (Descending):\n", sorted_by_python)

# Sort student by attendance in descending order
sorted_by_attendance = df.sort_values(by='attendance', ascending=False)
print("Students sorted by Attendance (Descending):\n", sorted_by_attendance)

# Filter students whose marks more than 80 in python
filtered_students = df[df['python_marks'] > 80]
print("Students with Python Marks > 80:\n", filtered_students)

# Filter students having attendance more than 75
filtered_attendance = df[df['attendance'] > 75]
print("Students with Attendance > 75:\n", filtered_attendance)

# selecting specific columns
selected_columns = df[['name', 'python_marks', 'pandas_marks']]
print("Selected Columns (Name, Python Marks, Pandas Marks):\n", selected_columns)

# Add a new column 'total_marks'
df['total_marks'] = df['python_marks'] + df['sql_marks'] + df['pandas_marks']
print("Total Marks:\n", df)

# Add a new column 'avg_marks'
df['avg_marks'] = df['total_marks'] / 3
print("Average Marks:\n", df)

# save the processed dataset in a new CSV file
df.to_csv('output/processed_students.csv', index=False)
