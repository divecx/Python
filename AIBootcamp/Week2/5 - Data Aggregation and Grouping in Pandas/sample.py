# Data aggregation and grouping in pandas
import pandas as pd

# Grouping data by categories
grouped = df.groupby("colomn_name")

# operation
# iterate over group
for name, group in grouped:
    print(name)
    print(group)

# apply aggregation
grouped.mean()
grouped.sum()

# Aggregation function
# using groupby
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean", "max", "min"]})

# using pivot_table
pivot = df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean"
)

# custom aggregation
def range_func(x):
    return x.max() - x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)


# calculating summary statistics for grouped data
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

# multi aggregation
df.groupby("category_column").agg(
    {"numeric_column": ["mean", "max", "min"]}
    )

