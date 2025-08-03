from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('label_encoders.pkl')

# Reverse map for prediction output
attrition_map_rev = {i: label for i, label in enumerate(encoders['Attrition'].classes_)}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            department = request.form['department']
            years = int(request.form['years_at_company'])
            income = float(request.form['monthly_income'])
            satisfaction = int(request.form['job_satisfaction'])
            overtime = request.form['overtime']

            # Encode inputs
            dept_encoded = encoders['Department'].transform([department])[0]
            overtime_encoded = encoders['OverTime'].transform([overtime])[0]

            features = [[age, dept_encoded, years, income, satisfaction, overtime_encoded]]
            pred = model.predict(features)[0]
            prediction = attrition_map_rev[pred]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
