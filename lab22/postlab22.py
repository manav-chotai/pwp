import pandas as pd
# Example DataFrame
df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 25, 30],
    "marks": [88.5, 92.0, 79.5]
})
# Check data types of each column
print(df.dtypes)


import pandas as pd
# Example DataFrame
df = pd.DataFrame({
    "age": [20, 25, None, 30, None]
})
# Fill missing values with the mean of the column
df["age"] = df["age"].fillna(df["age"].mean())
print(df)
