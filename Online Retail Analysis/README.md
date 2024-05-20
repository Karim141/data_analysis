# Exploratory Data Analysis of the Online Retail Dataset

## Overview

This README documents the exploratory data analysis (EDA) of a dataset that includes transactions from an online store. The aim of the analysis is to gain insights into sales patterns, customer trends, and pricing structures.

## Dataset

The dataset used in this analysis, `online_retail.csv`, is sourced from Kaggle. It can be accessed at the following URL: [Online Retail Dataset on Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset).

The `online_retail.csv` dataset contains the following key columns:
- `InvoiceNo`: Invoice number
- `StockCode`: Product code
- `Description`: Product description
- `Quantity`: Quantity sold
- `InvoiceDate`: Date of the invoice
- `UnitPrice`: Price per unit
- `CustomerID`: Customer identification number
- `Country`: Country of the customer

## Data Preparation

### Data Cleaning

Data was first checked for missing values and cleaned accordingly. Transactions without a `CustomerID` and canceled transactions (those where `InvoiceNo` starts with 'C') were removed to ensure data quality.

### Conversion

The `InvoiceDate` column was converted to datetime format to facilitate time series analysis.

## Descriptive Statistics

Basic descriptive statistics were generated to provide an overview of the data, including mean, median, and standard deviation, which help identify general trends and outliers in the dataset.

## Data Visualization and Analysis

### Distribution of Product Quantities

The histogram of product quantities shows most products are purchased in small quantities, indicating typical consumer buying behavior.

![Distribution of Product Quantities](distribution_of_product_quantities.png)

### Distribution of Unit Prices

The histogram of unit prices reveals that most items are priced below £50, with a high concentration of products in the lower price range.

![Distribution of Unit Prices](distribution_of_unit_prices.png)

### Revenue Development Over Time

The time series plot of total revenue shows fluctuations that might correlate with specific seasons or promotional events, indicating important sales periods.

![Revenue Development Over Time](revenue_development_over_time.png)

### Top 10 Best-Selling Products

This bar chart highlights the products with the highest quantities sold, showcasing which items are most popular among customers.

![Top 10 Best-Selling Products](top_10_best_selling_products.png)

### Sales by Country

The sales by country analysis indicates the geographical distribution of sales, highlighting which countries generate the most revenue.

![Sales by Country](sales_by_country.png)

### Top 10 Customers by Total Sales

Identifying top customers by total sales helps in recognizing valuable customers who contribute significantly to revenue.

![Top 10 Customers by Total Sales](top_10_customers_by_total_sales.png)

### Sales Frequency by Day of the Week

This bar chart shows the number of sales transactions for each day of the week, indicating peak sales days and helping in planning for demand.

![Sales Frequency by Day of the Week](sales_frequency_by_day_of_the_week.png)

### Relationship Between Unit Price and Sold Quantity

The scatter plot examines the relationship between unit price and quantity sold, helping to understand pricing strategies' impact on sales volume.

![Relationship Between Unit Price and Sold Quantity](relationship_between_unit_price_and_sold_quantity.png)

## Conclusions

- The data shows a wide variety in product types and sales patterns.
- Seasonal trends and customer segments provide valuable insights for strategic decision-making.
- Sales volume varies significantly by days and countries, highlighting market potentials.
- Analysis of price elasticity could aid in developing optimal pricing strategies.

## Outliers Detection

A boxplot for quantities was used to identify outliers in the data, which could be due to bulk purchases or data entry errors.

![Boxplot for Detecting Outliers in Quantities](boxplot_for_detecting_outliers_in_quantities.png)

This comprehensive analysis provides critical insights into the operations of the online store, guiding future business strategies and customer engagement plans.

## Conclusions from the exploratory data analysis:

1. The data show a wide variety in product types and sales patterns.
2. Seasonal trends and customer segments provide valuable insights for strategic decisions.
3. Sales volume varies significantly by days and countries, indicating market potentials.
4. The analysis of price elasticity could help develop optimal pricing strategies.