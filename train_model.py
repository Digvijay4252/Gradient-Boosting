import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load dataset
data = pd.read_csv('employee_attrition.csv')

# Label encode categorical columns
label_encoders = {}
for col in ['Department', 'OverTime', 'Attrition']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Features and target
X = data[['Age', 'Department', 'YearsAtCompany', 'MonthlyIncome', 'JobSatisfaction', 'OverTime']]
y = data['Attrition']

# Train Gradient Boosting model
model = GradientBoostingClassifier()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Gradient Boosting model and encoders saved successfully.")
