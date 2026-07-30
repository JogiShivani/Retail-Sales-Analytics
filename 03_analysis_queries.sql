-- TOTAL SALES
SELECT SUM(Sales) AS Total_Sales
FROM orders;

-- TOTAL PROFIT
SELECT SUM(Profit) AS Total_Profit
FROM orders;

-- TOTAL ORDERS
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- TOTAL CUSTOMERS
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- AVERAGE ORDER VALUE
SELECT ROUND(AVG(Sales),2) AS Average_Order_Value
FROM orders;
 
-- TOP 10 CUSTOMERS
SELECT
    CustomerName,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY CustomerName
ORDER BY Total_Sales DESC
LIMIT 10; 

-- TOP SELLING PRODUCTS
SELECT
    Product,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Product
ORDER BY Total_Quantity DESC;

-- HIGHEST REVENUE PRODUCTS
SELECT
    Product,
    SUM(Sales) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;

-- SALES BY CATEGORY
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- PROFIT BY CATEGORY
SELECT
     Category,
     SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales Desc;

-- SALES BY STATE
SELECT
    State,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY State
ORDER BY Total_Sales DESC;

-- MONTHLY SALES TREND
SELECT
    MONTH(OrderDate) AS Month,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY MONTH(OrderDate)
ORDER BY Month;

-- AVERAGE DISCOUNT
SELECT
    ROUND(AVG(Discount),2) AS Average_Discount
FROM orders;

-- TOP 5 MOST PROFITABLE PRODUCTS
SELECT
    Product,
    SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Product
ORDER BY Total_Profit DESC
LIMIT 5;

-- TOP 5 STATES BY PROFIT
SELECT
    State,
    SUM(Profit) AS Total_Profit
FROM orders
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 5;