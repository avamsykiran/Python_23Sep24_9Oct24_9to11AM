import pandas as pd
import numpy as np

data = {
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, np.nan, 42, 19, 35],
    "City": ["New York", "Chicago", "London", "Chicago", np.nan],
    "Spend": [150.50, 42.00, np.nan, 300.00, 85.20]
}

df = pd.DataFrame(data)
print(df)

# Basic Filtering: Find customers who spent more than $100
high_spenders = df[df["Spend"] > 100]
print(high_spenders)

# Multiple Conditions: Find customers from Chicago OR younger than 25
# CRITICAL: In Pandas, we MUST use bitwise operators (&, |) and wrap conditions in parentheses ()
filtered_df = df[(df["City"] == "Chicago") | (df["Age"] < 25)]
print(filtered_df)

# Drop any row that contains AT LEAST ONE missing value
clean_df = df.dropna()
print(clean_df)

# Drop rows ONLY if the missing value occurs in a specific column
clean_spend = df.dropna(subset=["Spend"])
print(clean_spend)

# Fill missing City entries with a constant string
df["City"] = df["City"].fillna("Unknown")
print(df)

# Fill missing Spend entries dynamically with the overall average (mean) spend
df["Spend"] = df["Spend"].fillna(df["Spend"].mean())
print(df)

# Sort by Spend in descending order
sorted_df = df.sort_values(by="Spend", ascending=False)
print(sorted_df)

# Complex Sorting: Primary sort by City (A-Z), Secondary sort by Spend (High to Low)
complex_sort = df.sort_values(by=["City", "Spend"], ascending=[True, False])
print(complex_sort)

# Create a new column based on values from an existing column
df["Customer_Tier"] = df["Spend"].apply(lambda s: "Premium" if s >= 150 else "Standard")
print(df)


