# 📊 Customer Churn Predictor with Retention Strategies (Streamlit + Gemini AI)

This project is a **Streamlit web app** that predicts whether a customer is likely to churn based on their details, and provides **AI-generated retention strategies** using **Gemini AI**.

---

## 🚀 Features

- 📈 Predicts customer churn using a trained classification model
- 🧠 Integrates **Gemini AI** to suggest actionable retention strategies
- 📊 Easy-to-use UI built with **Streamlit**
- 🔐 Environment-based API key handling
- 📦 Pre-trained model and scaler included

---

## 🗂️ Project Structure
```
├── app.py # Streamlit frontend
├── predictor.py # Prediction logic (model + scaler)
├── gemini_helper.py # Gemini AI integration for retention strategies
├── models/
│ ├── churn_model.pkl # Trained churn prediction model
│ └── scaler.pkl # StandardScaler used during training
├── notebooks/
│ └── churn_eda_and_training.ipynb # Notebook for EDA & model training
├── data/
│ └── sample_churn_data.csv # Sample data 
├── .env # Environment file 
```

---

## 📌 Requirements

### Install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

### Packages Required:
```
streamlit
scikit-learn
pandas
python-dotenv
google-generativeai
```

---

## 🔐 Environment Setup
Create a .env file with your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## 🧠 Model Details
The model was trained on a customer churn dataset using features such as:
```
Tenure
MonthlyCharges
TotalCharges
Contract Type
Internet Service
Payment Method
```
And more...

The trained classifier outputs both a Yes/No churn prediction and a probability score.

---

## 🧪 How to Run the App
```bash
streamlit run app.py
This will launch the app in your browser at http://localhost:your_port.
```

---

## 🤖 How Retention Suggestions Work
If the model predicts churn, a request is sent to Gemini Pro using a prompt built from customer details. Gemini responds with 2–3 realistic, personalized strategies for retaining the customer.

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Developed By Saksham Sharma
