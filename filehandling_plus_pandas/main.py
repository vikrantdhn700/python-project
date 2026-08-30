import csv
import pandas as pd

FILENAME = 'sales.txt'


FIELDS = ("order_id", "product", "quantity", "price", "city")

INITIAL_SALES = [
    (101, "Laptop", 1, 65000, "Bangalore"),
    (102, "Mouse", 2, 1200, "Delhi"),
    (103, "Keyboard", 1, 2500, "Mumbai"),
    (104, "Monitor", 2, 18000, "Chennai"),
    (105, "Printer", 1, 14500, "Hyderabad"),
    (106, "Webcam", 3, 3200, "Pune"),
    (107, "Headphones", 2, 4500, "Kolkata"),
    (108, "Tablet", 1, 28000, "Ahmedabad"),
    (109, "USB Drive", 5, 900, "Jaipur"),
    (110, "External HDD", 2, 6200, "Lucknow"),
    (111, "Laptop", 3, 1800, "Bangalore"),
    (112, "Router", 1, 3500, "Delhi"),
    (113, "Smartphone", 2, 32000, "Mumbai"),
    (114, "Speakers", 4, 2200, "Chennai"),
    (115, "SSD", 2, 7500, "Hyderabad"),
    (116, "Microphone", 1, 5800, "Pune"),
    (117, "Speakers", 2, 6800, "Kolkata"),
    (118, "Projector", 1, 42000, "Ahmedabad"),
    (119, "HDMI Cable", 6, 700, "Jaipur"),
    (120, "Graphics Card", 1, 48000, "Lucknow"),
    (121, "RAM", 4, 4200, "Bangalore"),
    (122, "Smartwatch", 2, 12500, "Delhi"),
    (123, "Scanner", 1, 16000, "Mumbai"),
    (124, "Cooling Pad", 3, 2100, "Chennai"),
    (125, "Mouse", 5, 1500, "Hyderabad"),
    (126, "Mechanical Keyboard", 2, 6200, "Pune"),
    (127, "WiFi Adapter", 4, 1300, "Kolkata"),
    (128, "Docking Station", 1, 9800, "Ahmedabad"),
    (129, "Ink Cartridge", 6, 1900, "Jaipur"),
    (130, "Headphones", 1, 18500, "Lucknow"),
]

"""Create/write the text file with sales transaction data"""
with open(FILENAME, 'w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(FIELDS)
    writer.writerows(INITIAL_SALES)

"""Read file using normal file handling"""
with open(FILENAME, 'r', encoding='utf-8') as file:
    print("Sales transaction data: ")
    print("--------------------")
    read_sale = file.read()
    print(read_sale)

df = pd.read_csv(FILENAME)
df['revenue'] = df['quantity'] * df['price']
print(df)

# # Total revenue column added
total_revenue = sum(df["revenue"])
print(f"Total Revenue: {total_revenue}")

# # Average order value
avg_order_value = df['revenue'].mean()
print(f"Average order value: {avg_order_value}")

# # Highest order value and lowest order value
highest_value_order = df.loc[df["revenue"].idxmax()]
lowest_value_order = df.loc[df["revenue"].idxmin()]
print(f"Highest value order:\n {highest_value_order}")
print(f"Lowest value order: \n {lowest_value_order}")

# # Revenue product wise
revenue_product_wise = df.groupby(
    'product')['revenue'].sum().sort_values(ascending=True)
print(revenue_product_wise)

# # Revenue city wise
revenue_city_wise = df.groupby(
    'city')['revenue'].sum().sort_values(ascending=False)
print("Revenue city wise: \n")
print(revenue_city_wise)

# # save proccessed data as sales.csv
df.to_csv('sales.csv', index=False)
