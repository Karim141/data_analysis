-- Top 10 Selling Products

SELECT Products.ProductName, SUM(Transactions.Quantity) AS TotalSold
FROM Transactions
JOIN Products ON Transactions.Products_ProductID = Products.ProductID
GROUP BY Products.ProductName
ORDER BY TotalSold DESC
LIMIT 10;

-- Revenue by Category

SELECT Categories.Category, SUM(Transactions.TotalAmount) AS TotalRevenue
FROM Transactions
JOIN Products ON Transactions.Products_ProductID = Products.ProductID
JOIN Categories ON Products.Category_CategoryID = Categories.CategoryID
GROUP BY Categories.Category
ORDER BY TotalRevenue DESC;

-- Total Revenue by Brand

SELECT Brand.Brand_Name, SUM(Transactions.TotalAmount) AS TotalRevenue
FROM Transactions
JOIN Products ON Transactions.Products_ProductID = Products.ProductID
JOIN Brand_has_product ON Products.ProductID = Brand_has_product.Products_ProductID
JOIN Brand ON Brand_has_product.Brands_Brand_id = Brand.Brand_ID
GROUP BY Brand.Brand_Name
ORDER BY TotalRevenue DESC;


-- Customer spending

SELECT Customer_Cart.CustomerName, SUM(Transactions.TotalAmount) AS TotalSpent
FROM Transactions
JOIN Customer_Cart ON Transactions.CustomerCart_CustomerID = Customer_Cart.CustomerName
GROUP BY Customer_Cart.CustomerName
ORDER BY TotalSpent DESC
LIMIT 10;


-- Monthly Sales Performance

SELECT DATE_FORMAT(Transaction_date, '%Y-%m') AS Month, SUM(TotalAmount) AS MonthlyRevenue
FROM Transactions
GROUP BY Month
ORDER BY Month;

-- Average Transaction Value by Payment Method

SELECT Payment_Method, AVG(TotalAmount) AS AverageTransactionValue
FROM Transactions
GROUP BY Payment_Method
ORDER BY AverageTransactionValue DESC;



