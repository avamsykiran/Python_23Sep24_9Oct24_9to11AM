import pandas as pd
import numpy as np

df_sales = pd.DataFrame({
    "Store": ["North", "South", "North", "West", "South", "West"],
    "Category": ["Tech", "Tech", "Office", "Office", "Tech", "Office"],
    "Revenue": [1200, 1500, 300, 450, 1100, 600],
    "Units": [5, 6, 12, 15, 4, 18]
})

# Calculate the total revenue per store
store_revenue = df_sales.groupby("Store")["Revenue"].sum().reset_index()
print(store_revenue)

# Group by multiple columns and run targeted aggregations
summary = df_sales.groupby(["Store", "Category"]).agg({
    "Revenue": ["sum", "mean"],  # Calculate BOTH total and average revenue
    "Units": "max"               # Find the highest number of units sold in a single transaction
})
print(summary)

# Create a matrix layout comparing Stores (rows) against Product Categories (columns)
pivot = df_sales.pivot_table(
    values="Revenue",      # The numeric data to aggregate
    index="Store",         # Rows
    columns="Category",    # Columns
    aggfunc="sum",         # The aggregation function (defaults to 'mean' if omitted)
    fill_value=0           # Replace any resulting missing NaN cells with 0
)
print(pivot)