CREATE TABLE customers (
     CustomerID VARCHAR(20) PRIMARY KEY,
     CustomerName VARCHAR(100),
     City VARCHAR(50),
     State VARCHAR(50)
);     

CREATE TABLE products(
     ProductID VARCHAR(20) PRIMARY KEY,
     Category VARCHAR(50),
     SubCategory VARCHAR(50),
     ProductName VARCHAR(100),
     Price DECIMAL(10,2)
);     

CREATE TABLE orders (
    OrderID VARCHAR(20) PRIMARY KEY,
    CustomerID VARCHAR(20),
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2),
    Discount INT,
    Sales DECIMAL(10,2),
    Profit DECIMAL(10,2),
    OrderDate DATE
);