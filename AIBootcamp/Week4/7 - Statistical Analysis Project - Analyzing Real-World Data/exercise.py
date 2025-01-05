# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.linear_model import LinearRegression

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# contingency_table = pd.crosstab(df['smoker'], ['time'])

# # Perform Chi-Square Test
# chi2, p, dof, expected = chi2_contingency(contingency_table)
# print("Chi-Square Statistic:", chi2)
# print("P-Value: ", p)

# # Interpret Result
# alpha = 0.05
# if p <= alpha:
#     print("Reject the null hypothesis: variables are dependent")
# else:
#     print("Failed to reject the null hypothesis: variables are independent")

# # Inspect Data
# print(df.info())
# print(df.describe())

# del df["sex"]
# del df["smoker"]
# del df["day"]
# del df["time"]

# # Vizualize Distributions
# sns.histplot(df["total_bill"], kde=True)
# plt.title("Distribution of Total Bill")
# plt.show()

# # Correlation heatmap
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

# Define Variables
X = df['total_bill'].values.reshape(-1, 1)
y = df['tip'].values

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Output coefficients
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared: ", model.score(X, y))

# Plot regression
sns.scatterplot(x=df['total_bill'], y=df['tip'], color="blue")
plt.plot(df['total_bill'], model.predict(X), color="red", label="Regression Line")
plt.title("Total Bill vs Tip")
plt.legend()
plt.show()