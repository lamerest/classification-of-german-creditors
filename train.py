import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, recall_score, precision_score
from transform import transform


# Load the dataset from CSV
data = pd.read_csv('./dataset/dataset.csv')

# Split the data into features and target variable
data = transform(data)

X = data.drop('Result', axis=1)
X = data.drop('Id', axis=1)
print(X)
y = data['Result']
print(y)

# Transform Housing labels to binary

# Save transformed data to CSV
data.to_csv('transformed.csv', index=False)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model

# This dataset requires use of a cost matrix (see below)
#       1        2
# -----------------------
#   1   0        1
# -----------------------
#   2   5        0

# (1 = Good,  2 = Bad)

cost_matrix = [
	[0, 1],
	[5, 0]
]

# Calculate class weights from the cost matrix and class distributions
class_weights = {
	1: cost_matrix[1][0] * sum(y_train == 1), 
	2: cost_matrix[0][1] * sum(y_train == 2)
}

print(cost_matrix[1][0])
print(cost_matrix[0][1])
print(class_weights)

total_cost = sum(class_weights.values())
print('Total cost', total_cost)

class_weights = {
	class_label: weight / total_cost for class_label, 
	weight in class_weights.items()
}
print(class_weights)


# Create a logistic regression model with cost matrix
model = LogisticRegression(class_weight=class_weights)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
# Calculate ROC AUC for the model

y_pred = model.predict_proba(X_test)[:, 1]
rocauc = roc_auc_score(y_test, y_pred)
print(f"ROC AUC: {rocauc}")

# Calculate recall and precision for the model

y_pred = model.predict(X_test)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print(f"Recall: {recall}")
print(f"Precision: {precision}")

# Save the model to a file using joblib
from joblib import dump
dump(model, 'model.joblib')