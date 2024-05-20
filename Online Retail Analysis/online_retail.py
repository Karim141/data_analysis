import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data
df = pd.read_csv('online_retail.csv')
print("First lines of the dataset:")
print(df.head())

# Data cleaning
print("\nMissing values in each attribute:")
print(df.isnull().sum())
df.dropna(subset=['CustomerID'], inplace=True)  # Remove rows without CustomerID
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])  # Convert date

# Remove canceled transactions
cancelled_orders = df[df['InvoiceNo'].str.contains('C', na=False)]
non_cancelled_orders = df[~df['InvoiceNo'].str.contains('C', na=False)]
non_cancelled_orders['TotalPrice'] = non_cancelled_orders['Quantity'] * non_cancelled_orders['UnitPrice']

# Basic statistics
print("\nDescriptive statistics of the data:")
print(non_cancelled_orders.describe())

# Data visualization
plt.figure(figsize=(10, 6))
sns.histplot(non_cancelled_orders['Quantity'][non_cancelled_orders['Quantity'] < 50], bins=50)
plt.title('Distribution of Product Quantities')
plt.savefig('distribution_of_product_quantities.png')  # Save the figure
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(non_cancelled_orders['UnitPrice'][non_cancelled_orders['UnitPrice'] < 50], bins=100)
plt.title('Distribution of Unit Prices')
plt.savefig('distribution_of_unit_prices.png')  # Save the figure
plt.show()

# Sales development over time
non_cancelled_orders.set_index('InvoiceDate', inplace=True)
df_resampled = non_cancelled_orders.resample('M').sum()
plt.figure(figsize=(12, 6))
df_resampled['TotalPrice'].plot()
plt.title('Revenue Development Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.savefig('revenue_development_over_time.png')  # Save the figure
plt.show()

# Best-selling products
top_products = non_cancelled_orders.groupby('Description').sum().sort_values(by='Quantity', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products['Quantity'], y=top_products.index)
plt.title('Top 10 Best-Selling Products')
plt.savefig('top_10_best_selling_products.png')  # Save the figure
plt.show()

# Sales by country
sales_by_country = non_cancelled_orders.groupby('Country').sum().sort_values(by='TotalPrice', ascending=False)
plt.figure(figsize=(10, 8))
sns.barplot(x=sales_by_country['TotalPrice'], y=sales_by_country.index)
plt.title('Sales by Country')
plt.savefig('sales_by_country.png')  # Save the figure
plt.show()

# Customer analysis by total sales
customer_spending = non_cancelled_orders.groupby('CustomerID').sum()['TotalPrice'].sort_values(ascending=False)
top_customers = customer_spending.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.values, y=top_customers.index.astype(str))
plt.title('Top 10 Customers by Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Customer ID')
plt.savefig('top_10_customers_by_total_sales.png')  # Save the figure
plt.show()

# Sales frequency by day of the week
non_cancelled_orders['Weekday'] = non_cancelled_orders.index.day_name()
weekday_sales = non_cancelled_orders.groupby('Weekday').count()['InvoiceNo']
plt.figure(figsize=(10, 6))
weekday_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).plot(kind='bar')
plt.title('Sales Frequency by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Sales')
plt.savefig('sales_frequency_by_day_of_the_week.png')  # Save the figure
plt.show()

# Relationship between unit price and sold quantity
plt.figure(figsize=(10, 6))
sns.scatterplot(x='UnitPrice', y='Quantity', data=non_cancelled_orders[non_cancelled_orders['Quantity'] < 50])
plt.title('Relationship Between Unit Price and Sold Quantity')
plt.xlabel('Unit Price (£)')
plt.ylabel('Sold Quantity')
plt.savefig('relationship_between_unit_price_and_sold_quantity.png')  # Save the figure
plt.show()

# Detection of outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=non_cancelled_orders['Quantity'])
plt.title('Boxplot for Detecting Outliers in Quantities')
plt.savefig('boxplot_for_detecting_outliers_in_quantities.png')  # Save the figure
plt.show()