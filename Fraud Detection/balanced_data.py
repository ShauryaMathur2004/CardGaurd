import pandas as pd
df = pd.read_csv("Fraud Detection/cleaned_data.csv")
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

#Separate features and target
X = df.drop('IsFraud', axis=1)
y = df['IsFraud']

#Split into train and test before resampling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#Using SMOTE (Over-sampling)
smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X_train, y_train)

print("SMOTE applied:")
print("Before:", y_train.value_counts().to_dict())
print("After:", y_smote.value_counts().to_dict())


# === Logistic Regression ===
lr = LogisticRegression(max_iter=1000)
lr.fit(X_smote, y_smote)
y_pred_lr = lr.predict(X_test)

print("\n=== Logistic Regression Report ===")
print(classification_report(y_test, y_pred_lr, digits=4))

# Save the logistic regression model
joblib.dump(lr, "logistic_model.pkl")

# === Random Forest Classifier ===
rf = RandomForestClassifier(random_state=42)
rf.fit(X_smote, y_smote)
y_pred_rf = rf.predict(X_test)

print("\n=== Random Forest Report ===")
print(classification_report(y_test, y_pred_rf, digits=4))

# Save the random forest model
joblib.dump(rf, "random_forest_model.pkl")
