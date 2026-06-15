import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard"],
    "Price": [1200.00, 25.00, 300.00, 75.00],
    "Quantity": [2, 10, 3, 5]
})

# Scalar Operation: Apply 10% tax to the entire Price column
df["Taxed_Price"] = df["Price"] * 1.10
print(df)

# Series-to-Series Operation: Multiply two columns together simultaneously
df["Total_Value"] = df["Price"] * df["Quantity"]
print(df)

# Convert all product names to uppercase
df["Product_Upper"] = df["Product"].str.upper()
print(df)

# Check for a substring cleanly across the entire dataset
df["Is_Input_Device"] = df["Product"].str.contains("Mouse|Keyboard", regex=True)
print(df)

# If Price is greater than 200, label it "Expensive", otherwise "Affordable"
df["Category"] = np.where(df["Price"] > 200, "Expensive", "Affordable")
print(df)

# Define the conditional thresholds
conditions = [
    df["Price"] >= 500,
    (df["Price"] >= 100) & (df["Price"] < 500),
    df["Price"] < 100
]

# Define the corresponding outputs
outputs = ["High Tier", "Mid Tier", "Low Tier"]

# Apply them all vectorially in one clean sweep
df["Tier"] = np.select(conditions, outputs, default="Unknown")
print(df)

