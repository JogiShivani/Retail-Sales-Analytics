import pandas as pd
from pathlib import Path

products = [
    ["PROD0001", "Electronics", "Laptop", "Dell Inspiron", 55000],
    ["PROD0002", "Electronics", "Mobile", "Samsung Galaxy", 28000],
    ["PROD0003", "Electronics", "Headphones", "Boat Rockerz", 1500],
    ["PROD0004", "Furniture", "Chair", "Office Chair", 4500],
    ["PROD0005", "Furniture", "Table", "Study Table", 6500],
    ["PROD0006", "Furniture", "Sofa", "3 Seater Sofa", 22000],
    ["PROD0007", "Grocery", "Rice", "Basmati Rice 5kg", 750],
    ["PROD0008", "Grocery", "Oil", "Sunflower Oil 5L", 950],
    ["PROD0009", "Grocery", "Tea", "Tata Tea Gold", 420],
    ["PROD0010", "Clothing", "Shirt", "Formal Shirt", 1200],
    ["PROD0011", "Clothing", "Jeans", "Blue Jeans", 1800],
    ["PROD0012", "Clothing", "Shoes", "Running Shoes", 3500]
]

df = pd.DataFrame(
    products,
    columns=[
        "ProductID",
        "Category",
        "SubCategory",
        "ProductName",
        "Price"
    ]
)

output_path = Path(__file__).parent.parent / "Dataset" / "products.csv"

df.to_csv(output_path, index=False)

print("products.csv created successfully!")