# Task 1: Perform EDA and Preprocessing

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df_telco = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Drop unnecessary column
df_telco = df_telco.drop(columns=['customerID'])

# Encode target variable
le = LabelEncoder()
df_telco['Churn'] = le.fit_transform(df_telco['Churn'])

# One-hot encode categorical variables
categorical_cols = df_telco.select_dtypes(include=['object']).columns
df_telco = pd.get_dummies(df_telco, columns=categorical_cols, drop_first=True)

# Define features and target
X = df_telco.drop(columns=['Churn'])
y = df_telco['Churn']

# Scale Features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)

# Train k-NN Model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Evaluate models
log_pred = log_model.predict(X_test)
knn_pred = knn_model.predict(X_test)

print("\n Logistic Regression Classification report: ")
print(classification_report(y_test, log_pred))

print("\n k-NN Regression Classification report: ")
print(classification_report(y_test, knn_pred))

# Confusion Matrix for Logistic Regression
print("Confusion Matrix: \n", confusion_matrix(y_test, log_pred))


# # Inspect Data
# print(df_telco.info())
# print(df_telco.describe())

# # Visualize churn distribution
# sns.countplot(x='Churn', data=df_telco)
# plt.title("Churn Distribution")
# plt.show()

# # Handle missing values
# df_telco.fillna(df_telco.mean(), inplace=True)