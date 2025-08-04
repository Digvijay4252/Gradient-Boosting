<!-- # Gradient-Boosting

<img width="922" height="891" alt="image" src="https://github.com/user-attachments/assets/2fd7c002-09ab-4c78-94e3-a1d8f0769373" /> -->

## Employee Attrition Predictor – Gradient Boosting Classifier

This project leverages the Gradient Boosting Classifier to predict whether an employee is likely to leave the company (attrition). Users input job-related attributes, and the model predicts attrition using a trained ensemble model.

 The web interface is built using Flask and styled for usability, allowing real-time predictions via a simple form.

## Model Used

- Algorithm: Gradient Boosting Classifier (from sklearn.ensemble)

- Goal: Binary Classification (Yes/No for employee attrition)

- Serialization: joblib for saving the trained model and encoders

---

## Project Structure

```
Gradient-Boosting/
│
├── app.py                     # Flask web app
├── train_model.py             # Model training script using Gradient Boosting
├── model.pkl                  # Trained classifier
├── encoders.pkl               # Label encoders for categorical features
├── employee_data.csv          # Dataset for training
│
├── templates/
│   └── index.html             # HTML frontend for input
└── static/
    └── style.css              # (Optional) CSS styling for the form

```

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Gradient-Boosting.git
cd Gradient-Boosting
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000

## Screenshots

<img width="922" height="891" alt="image" src="https://github.com/user-attachments/assets/2fd7c002-09ab-4c78-94e3-a1d8f0769373" />

## Future Improvements

Show prediction confidence/probability

Add data visualizations (e.g., SHAP, feature importance)

Accept CSV file uploads for batch prediction

Deploy on Render, Heroku, or HuggingFace Spaces
