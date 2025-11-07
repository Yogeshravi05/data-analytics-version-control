# data_cleaning.py
import pandas as pd

# Load sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, None, 22],
    "Salary": [50000, 54000, 58000, None]
}

df = pd.DataFrame(data)

# Clean missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Display cleaned data
print("Cleaned DataFrame:")
print(df)
