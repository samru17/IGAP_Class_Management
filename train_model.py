# train_model.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

np.random.seed(42)

n = 1000

study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(40, 100, n)
previous_marks = np.random.uniform(30, 95, n)
assignment_score = np.random.uniform(30, 100, n)

score = (
    study_hours * 5
    + attendance * 0.35
    + previous_marks * 0.30
    + assignment_score * 0.20
)

result = (score >= 65).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_marks": previous_marks,
    "assignment_score": assignment_score,
    "result": result
})

X = df[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "assignment_score"
    ]
]

y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

joblib.dump(model, "student_performance_model.pkl")

print("Model saved successfully!")