import pandas as pd
import random

first_names = [
    "Aarav","Vivaan","Aditya","Vihaan","Arjun",
    "Sai","Rahul","Rohan","Ananya","Diya",
    "Priya","Sneha","Meera","Kiran","Shivani"
]

last_names = [
    "Sharma","Reddy","Patel","Kumar","Singh",
    "Verma","Gupta","Naidu","Yadav","Jogi"
]

cities = [
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad"
]

states = {
    "Hyderabad":"Telangana",
    "Bangalore":"Karnataka",
    "Mumbai":"Maharashtra",
    "Delhi":"Delhi",
    "Chennai":"Tamil Nadu",
    "Pune":"Maharashtra",
    "Kolkata":"West Bengal",
    "Ahmedabad":"Gujarat"
}

customers = []

for i in range(1,1001):

    city = random.choice(cities)

    customers.append({
        "CustomerID":f"CUST{i:04}",
        "CustomerName":random.choice(first_names)+" "+random.choice(last_names),
        "City":city,
        "State":states[city]
    })

df = pd.DataFrame(customers)

from pathlib import Path

output_path = Path(__file__).parent.parent / "Dataset" / "customers.csv"
df.to_csv(output_path, index=False)

print("customers.csv created successfully!")