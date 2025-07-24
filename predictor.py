import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Features (must match training order)
feature_order = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
    'MonthlyCharges', 'TotalCharges'
]

# Mappings
label_maps = {
    'gender': {"Female": 0, "Male": 1},
    'InternetService': {"DSL": 0, "Fiber optic": 1, "No": 2},
    'Contract': {"Month-to-month": 0, "One year": 1, "Two year": 2},
    'PaymentMethod': {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    },
}

def preprocess_user_input(user_input_dict):
    df = pd.DataFrame([user_input_dict])

    # Apply mapping
    for col, mapping in label_maps.items():
        if col in df.columns:
            df[col] = df[col].map(mapping)

    # Fill any unmapped categorical fields with default value (e.g., 0)
    df.fillna(0, inplace=True)

    # Ensure column order
    df = df[feature_order]

    # Scale numeric features
    df_scaled = scaler.transform(df)

    return df_scaled

def predict_churn(user_input_dict):
    X = preprocess_user_input(user_input_dict)
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]
    return ("Yes" if pred == 1 else "No"), round(proba * 100, 2)
