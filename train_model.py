from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Sample realistic dataset
X = [
    [15, True, 15000, 25, 80, 12, 0.65, True, 70],  # High-Quality Page Example 1
    [12, True, 12000, 20, 60, 10, 0.7, True, 65],   # High-Quality Page Example 2
    [18, True, 20000, 30, 90, 15, 0.68, True, 75],  # High-Quality Page Example 3
    [14, True, 14000, 22, 70, 11, 0.66, True, 60],  # High-Quality Page Example 4
    [3, False, 300, 2, 10, 2, 0.2, False, 10],      # Low-Quality Page Example 1
    [4, False, 400, 3, 15, 3, 0.25, False, 20],     # Low-Quality Page Example 2
    [2, False, 150, 1, 5, 1, 0.1, False, 8],        # Low-Quality Page Example 3
    [5, False, 500, 4, 20, 4, 0.3, False, 25],      # Low-Quality Page Example 4
]
y = [1, 1, 1, 1, 0, 0, 0, 0]  # Labels

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Save the trained model
with open('web_quality_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
