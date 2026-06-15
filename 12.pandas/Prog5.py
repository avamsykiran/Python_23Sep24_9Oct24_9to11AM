import pandas as pd

# Dataset A: Employee profiles
df_employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Dept_ID": [1, 2, 1, 9]  # David is in Dept 9 (which doesn't exist in our depts table)
})

# Dataset B: Department details
df_departments = pd.DataFrame({
    "Dept_ID": [1, 2, 3],
    "Dept_Name": ["Engineering", "HR", "Marketing"]
})

#inner join
inner_result = pd.merge(df_employees, df_departments, on="Dept_ID", how="inner")
print(inner_result)

#left outer join
left_result = pd.merge(df_employees, df_departments, on="Dept_ID", how="left")
print(left_result)

#right outer join
right_result = pd.merge(df_employees, df_departments, on="Dept_ID", how="right")
print(right_result)


