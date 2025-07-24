# app.py

import streamlit as st
from predictor import predict_churn  
from gemini_helper import get_retention_suggestion
import os
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("Customer Churn Predictor")
st.write("Enter customer details to predict churn and get suggestions.")

# ---- Form ----
with st.form("churn_form"):
    tenure = st.number_input("Tenure (months)", min_value=0)
    monthly = st.number_input("Monthly Charges", min_value=0.0)
    total = st.number_input("Total Charges", min_value=0.0)
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Has Partner", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents", ["No", "Yes"])
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", 
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

    # Additional services (hardcoded or customizable)
    online_security = st.selectbox("Online Security", ["No", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])

    submitted = st.form_submit_button("Predict")

# ---- Process ----
if submitted:
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
    payment_map = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    }

    # Create input dict
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "PhoneService": 1 if phone == "Yes" else 0,
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "gender": gender,
        "Contract": contract_map[contract],
        "InternetService": internet_map[internet],
        "PaymentMethod": payment_map[payment],
        "OnlineSecurity": 1 if online_security == "Yes" else 0,
        "OnlineBackup": 1 if online_backup == "Yes" else 0,
        "TechSupport": 1 if tech_support == "Yes" else 0,
        "StreamingTV": 1 if streaming_tv == "Yes" else 0,
        "StreamingMovies": 1 if streaming_movies == "Yes" else 0,
        "DeviceProtection": 1 if device_protection == "Yes" else 0,
        "MultipleLines": 1 if multiple_lines == "Yes" else 0
    }

    # Predict churn
    prediction, probability = predict_churn(input_dict)
    st.subheader("Prediction Result")
    st.write(f"**Churn Prediction:** {prediction}")
    st.write(f"**Churn Probability:** {probability}%")

    if prediction == "Yes":
        with st.spinner("Generating retention suggestion..."):
            suggestion = get_retention_suggestion(input_dict)
        if suggestion:
            st.subheader("Retention Strategy Suggestion (AI)")
            st.write(suggestion)
        else:
            st.warning("Could not generate suggestion. Try again later.")
