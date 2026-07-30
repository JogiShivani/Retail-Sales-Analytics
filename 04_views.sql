CREATE VIEW sales_summary AS
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category;