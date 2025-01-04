# Select Specific columns and filter rows

import pandas as pd

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

selected_columns = df[["species", "sepal_length"]]
print("Selected columns: ", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filteres rows: \n", filtered_rows)