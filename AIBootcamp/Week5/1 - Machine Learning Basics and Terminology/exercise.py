# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns 
import matplotlib.pyplot as plt

# Define features and target variables

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Define feature and target
features = df[['total_bill', 'size']]
target = df['tip']

print("Features: \n", features.head())
print("Target: \n", target.head())

# Split Data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
print("Training Dataset: ", X_train.shape)
print("Testing Dataset: ", X_test.shape)

# Visualize relationships
sns.pairplot(df, x_vars=["total_bill", "size"], y_vars="tip", height=5, aspect=0.8, kind="scatter")
plt.title("Feature vs Target Relationships")
plt.show()