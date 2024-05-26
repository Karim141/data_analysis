# Retail Store Database Analysis

This project contains SQL scripts to analyze a retail store database. The database schema, initial data, and various analysis scripts are provided to extract insights from the data.

## Database Schema

The database schema is visualized in the following diagram:

![EER Diagram](eer_diagram/EER_diagram.png)

The schema includes the following tables:
- `Customer_Cart`
- `Cashier`
- `Transactions`
- `Brand`
- `Brand_has_product`
- `Products`
- `Categories`

## Schema Creation

The schema can be created using the provided [schema_creation.sql](sql_scripts/schema_creation.sql) script:

```sql
-- schema_creation.sql
CREATE TABLE Customer_Cart (
    CustomerName VARCHAR(255),
    CustomerPhNo VARCHAR(15),
    CustomerAddress VARCHAR(255),
    Password VARCHAR(255),
    PRIMARY KEY (CustomerName)
);

CREATE TABLE Cashier (
    CashierID INT,
    CashierName VARCHAR(255),
    CashierPhoneNo VARCHAR(15),
    CashierAddress VARCHAR(255),
    PRIMARY KEY (CashierID)
);

CREATE TABLE Categories (
    CategoryID INT,
    Category VARCHAR(255),
    SubCategory VARCHAR(255),
    PRIMARY KEY (CategoryID)
);

CREATE TABLE Products (
    ProductID VARCHAR(255),
    ProductName VARCHAR(255),
    ProductStock INT,
    Price DECIMAL(10, 2),
    Discount INT,
    Category_CategoryID INT,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (Category_CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Brand (
    Brand_ID INT,
    Brand_Name VARCHAR(255),
    PRIMARY KEY (Brand_ID)
);

CREATE TABLE Brand_has_product (
    Brands_Brand_id INT,
    Products_ProductID VARCHAR(255),
    PRIMARY KEY (Brands_Brand_id, Products_ProductID),
    FOREIGN KEY (Brands_Brand_id) REFERENCES Brand(Brand_ID),
    FOREIGN KEY (Products_ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Transactions (
    Transaction_date DATE,
    Quantity INT,
    Subtotal DECIMAL(10, 2),
    Taxes DECIMAL(10, 2),
    DiscountPrice DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    Payment_Method VARCHAR(50),
    Products_ProductID VARCHAR(255),
    CustomerCart_CustomerID VARCHAR(255),
    Cashier_CashierID INT,
    PRIMARY KEY (Transaction_date, Products_ProductID, CustomerCart_CustomerID, Cashier_CashierID),
    FOREIGN KEY (Products_ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerCart_CustomerID) REFERENCES Customer_Cart(CustomerName),
    FOREIGN KEY (Cashier_CashierID) REFERENCES Cashier(CashierID)
);

## Data Import

The initial data can be imported using the following CSV files in the data directory:

brand_has_product.csv
brand.csv
cashier.csv
categories.csv
customer_cart.csv
products.csv
transactions.csv