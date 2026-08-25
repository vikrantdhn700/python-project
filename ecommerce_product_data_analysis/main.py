"""
This script performs various data analysis tasks on a CSV file containing e-commerce product information.
"""

import pandas as pd

df = pd.read_csv('products.csv')

# Inspect dataset
print("Dataset Overview:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Find total number of products
total_products = df.shape[0]
print("Total Products:", total_products)

# Find unique categories
unique_categories = df['category'].nunique()
print("Unique Categories:", unique_categories)

# Find unique brands
unique_brands = df['brand'].nunique()
print("Unique Brands:", unique_brands)

# Count products category-wise
category_counts = df['category'].value_counts()
print("Category Counts:\n", category_counts)

# Find average price of products
average_price = df['price'].mean()
print("Average Price:", average_price)

# Find the highest priced product
highest_priced_product = df.loc[df['price'].idxmax()]
print("Highest Priced Product:\n", highest_priced_product)

# Find the lowest priced product
lowest_priced_product = df.loc[df['price'].idxmin()]
print("Lowest Priced Product:\n", lowest_priced_product)

# Find product price above 50000
products_above_50000 = df[df['price'] > 50000]
print("Products Priced Above 50000:\n", products_above_50000)

# Find product with rating above 4
highly_rated_products = df[df['rating'] > 4]
print("Highly Rated Products (Rating > 4):\n", highly_rated_products)

# Sort products by price in descending order
sorted_products = df.sort_values(by='price', ascending=False)
print("Products Sorted by Price (Descending):\n", sorted_products)

# Sort products by rating in descending order
sorted_by_rating = df.sort_values(by='rating', ascending=False)
print("Products Sorted by Rating (Descending):\n", sorted_by_rating)

# Find products with stock less than 10
low_stock_products = df[df['stock'] < 10]
print("Low Stock Products (Stock < 10):\n", low_stock_products)

# Create discount amount
df['discounted_amount'] = df['price'] * 0.8
print("Products with Discounted Amount:\n",
      df[['product_name', 'price', 'discounted_amount']])

# Create final price
df['final_price'] = df['price'] - df['discounted_amount']
print("Products with Final Price:\n",
      df[['product_name', 'price', 'discounted_amount', 'final_price']])

# Find avg price by category
average_price_by_category = df.groupby('category')['final_price'].mean()
print("Average Final Price by Category:\n", average_price_by_category)

# Find avg rating by brand
average_rating_by_brand = df.groupby('brand')['rating'].mean()
print("Average Rating by Brand:\n", average_rating_by_brand)

# Find maximum product price by category-wise
max_price_by_category = df.groupby('category')['price'].max()
print("Maximum Product Price by Category:\n", max_price_by_category)

# Export Final dataframe to CSV
df.to_csv('output/final_products.csv', index=False)
