# Data Cleaning and Preparation with Pandas

# handling missing values
# drop missing values

df = df.dropna()
df = df.dropna(axis=1)

# fill missing values
df["column_name"] = df["column_name"].fillna(0)
df.fillna(method="ffill") #forwardfill
df.fillna(method="bfill") #backwardfill

# interpolation
df["column_name"] = df["column_name"].interpolate()

#===================================================
# Data Transformation
# renaming column 
df = df.rename(columns={"old_name": "new_name"})

# Changing Data Types 
df["column_name"] = df["columns_name"].astype("float")
df["column_name"] = pd.to_datetime(df["column_name"])

# Creating or Modifying Column
df["new_column"] = df["existing_column"] * 2

#===================================================
# Combining and Merging DataFrame
# Concatenation
combined = pd.concat([df1, df2], axis=0) # rows
combined = pd.concat([df1, df2], axis=1) # column

# Merging
merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")

# Joining
joined = df1.join(df2, how="inner")