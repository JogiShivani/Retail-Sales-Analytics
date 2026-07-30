import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

# Load customers
customer_path = Path(__file__).parent.parent / "Dataset" / "customers.csv"
customers = pd.read_csv(customer_path)

products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headphones",
    "Printer",
    "USB Cable",
    "Webcam",
    "Tablet",
    "Speaker"
]

categories = {
    "Laptop":"Electronics",
    "Keyboard":"Accessories",
    "Mouse":"Accessories",
    "Monitor":"Electronics",
    "Headphones":"Accessories",
    "Printer":"Office",
    "USB Cable":"Accessories",
    "Webcam":"Accessories",
    "Tablet":"Electronics",
    "Speaker":"Electronics"
}

orders = []

for i in range(1,5001):

    customer = customers.sample(1).iloc[0]

    product = random.choice(products)

    quantity = random.randint(1,5)

    price = random.randint(500,50000)

    discount = random.choice([0,5,10,15,20])

    sales = quantity * price

    profit = sales * random.uniform(0.08,0.30)

    order_date = datetime(2025,1,1) + timedelta(days=random.randint(0,364))

    orders.append({
        "OrderID":f"ORD{i:05}",
        "CustomerID":customer["CustomerID"],
        "CustomerName":customer["CustomerName"],
        "City":customer["City"],
        "State":customer["State"],
        "Product":product,
        "Category":categories[product],
        "Quantity":quantity,
        "Price":price,
        "Discount":discount,
        "Sales":round(sales,2),
        "Profit":round(profit,2),
        "OrderDate":order_date.strftime("%Y-%m-%d")
    })

df = pd.DataFrame(orders)

output_path = Path(__file__).parent.parent / "Dataset" / "orders.csv"

df.to_csv(output_path,index=False)

print("orders.csv created successfully!")