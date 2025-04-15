import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix 
import matplotlib.pyplot as plt 
import seaborn as sns 
data = pd.DataFrame({ 
'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Feature1': [0, 1, 1, 0, 1, 0, 0, 1, 0, 1], 
'Target': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1] 
}) 
X = data.drop('Target', axis=1) 
y = data['Target'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
logistic_model = LogisticRegression() 
logistic_model.fit(X_train, y_train) 
y_pred_logistic = logistic_model.predict(X_test) 
accuracy_logistic = accuracy_score(y_test, y_pred_logistic) 
precision_logistic = precision_score(y_test, y_pred_logistic) 
recall_logistic = recall_score(y_test, y_pred_logistic) 
f1_logistic = f1_score(y_test, y_pred_logistic) 
conf_matrix_logistic = confusion_matrix(y_test, y_pred_logistic) 
print("Logistic Regression Metrics:") 
print("Accuracy:", accuracy_logistic) 
print("Precision:", precision_logistic) 
print("Recall:", recall_logistic) 
print("F1 Score:", f1_logistic) 
print("Confusion Matrix:") 
print(conf_matrix_logistic) 
decision_tree_model = DecisionTreeClassifier() 
decision_tree_model.fit(X_train, y_train)
y_pred_dt = decision_tree_model.predict(X_test) 
accuracy_dt = accuracy_score(y_test, y_pred_dt) 
precision_dt = precision_score(y_test, y_pred_dt) 
recall_dt = recall_score(y_test, y_pred_dt) 
f1_dt = f1_score(y_test, y_pred_dt) 
conf_matrix_dt = confusion_matrix(y_test, y_pred_dt) 
print("\nDecision Tree Metrics:") 
print("Accuracy:", accuracy_dt) 
print("Precision:", precision_dt) 
print("Recall:", recall_dt) 
print("F1 Score:", f1_dt) 
print("Confusion Matrix:") 
print(conf_matrix_dt) 
plt.figure(figsize=(8, 6)) 
sns.heatmap(conf_matrix_logistic, annot=True, cmap='Blues', fmt='g') 
plt.xlabel('Predicted labels') 
plt.ylabel('True labels') 
plt.title('Confusion Matrix - Logistic Regression') 
plt.show() 
plt.figure(figsize=(8, 6)) 
sns.heatmap(conf_matrix_dt, annot=True, cmap='Blues', fmt='g') 
plt.xlabel('Predicted labels') 
plt.ylabel('True labels') 
plt.title('Confusion Matrix - Decision Tree') 
plt.show()





