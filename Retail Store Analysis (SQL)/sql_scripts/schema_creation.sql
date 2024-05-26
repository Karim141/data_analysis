CREATE SCHEMA Retail_Store;

USE Retail_Store;

-- Table for categories data
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    Category VARCHAR(255),
    SubCategory VARCHAR(255)
);

-- Table for brand data
CREATE TABLE Brand (
    Brand_ID INT AUTO_INCREMENT PRIMARY KEY,
    Brand_Name VARCHAR(255) UNIQUE NOT NULL
);

-- Table for products data
CREATE TABLE Products (
    ProductID VARCHAR(255) PRIMARY KEY,
    ProductName VARCHAR(255),
    ProductStock INT,
    Price DECIMAL(10, 2),
    Discount INT,
    Category_CategoryID INT,
    FOREIGN KEY (Category_CategoryID) REFERENCES Categories(CategoryID)
);

-- Table for cashier data
CREATE TABLE Cashier (
    CashierID INT AUTO_INCREMENT PRIMARY KEY,
    CashierName VARCHAR(255),
    CashierPhoneNo VARCHAR(15),
    CashierAddress VARCHAR(255)
);

-- Table for customer cart data
CREATE TABLE Customer_Cart (
    CustomerName VARCHAR(255) PRIMARY KEY,
    CustomerPhNo VARCHAR(15),
    CustomerAddress VARCHAR(255),
    Password VARCHAR(255)
);

-- Table for mapping between brand and product
CREATE TABLE Brand_has_product (
    Brands_Brand_id INT,
    Products_ProductID VARCHAR(255),
    PRIMARY KEY (Brands_Brand_id, Products_ProductID),
    FOREIGN KEY (Brands_Brand_id) REFERENCES Brand(Brand_ID),
    FOREIGN KEY (Products_ProductID) REFERENCES Products(ProductID)
);

-- Table for transaction data
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
    PRIMARY KEY (Transaction_date, Products_ProductID, CustomerCart_CustomerID),
    FOREIGN KEY (Products_ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerCart_CustomerID) REFERENCES Customer_Cart(CustomerName),
    FOREIGN KEY (Cashier_CashierID) REFERENCES Cashier(CashierID)
);
