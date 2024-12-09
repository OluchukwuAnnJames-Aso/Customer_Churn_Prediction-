import streamlit as st
import numpy as np
import joblib

model =joblib.load("CustomerChurn_logistic_regression_model.pkl")

st.title("Customer Churn Prediction App")
st.write(""" This app predicts customer churn based on the customer data input. Please provide the following details: """)

age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure", min_value=0, max_value=6000, value=12, step=1)
usuage_frequency = st.number_input("Usuage Frequency", min_value=0, max_value=8000, value=10, step=1)
support_calls = st.number_input("Support Calls", min_value=0, max_value=500, value=5, step=1)
payment_delay = st.number_input("Payment Delay", min_value=0, max_value=250, value=7, step=1)
subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract_length = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
total_spend = st.number_input("Total Spend", min_value=0.0, max_value=100000.0, value=50.0, step=0.1)
last_interaction = st.number_input("Last Interaction", min_value=0, max_value=6000, value=7, step=1)

gender_encoded = 1 if gender == "Male" else 0
subscription_type_encoded = 1 if subscription_type == "Basic" else 2 if subscription_type == "Standard" else 3
contract_length_encoded = 1 if contract_length == "Monthly" else 2 if contract_length == "Quarterly" else 3
inputs = np.array([[age, gender_encoded,tenure, usuage_frequency, support_calls, payment_delay, subscription_type_encoded, contract_length_encoded, total_spend, last_interaction]])

if st.button("Predict"):
    prediction = model.predict(inputs)
    Churn = "Churn" if prediction[0] == 1 else "No Churn"
    st.write(f"Prediction: **{Churn}**")
