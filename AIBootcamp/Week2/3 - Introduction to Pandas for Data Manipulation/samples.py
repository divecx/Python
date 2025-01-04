import pandas as pd

# series in pandas
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)

# dataframe in pandas
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
# print(df)

# Loading data from csv, excel, other sources

# df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")\

# saving data (save to csv | save to excel)
# df.to_csv("data.csv", index=False)
# df.to_excel("data.xlsx", index=False)

# Basic DataFrame Operations
# Viewing Data
print(df.head())
printf(df.tail(3))

print(df.info())
print(df.describe())

# selecting and indexing
print(df[["Name", "Age"]]) # selecting columns
print(df[df["Age"] > 25]) # filtering rows
print(df.iloc[0]) # selecting by position
print(df.iloc[:, 0]) # selecting by position
print(df.loc[0])  # selecting by label
print(df.loc[:, "Name"]) # selecting by label

