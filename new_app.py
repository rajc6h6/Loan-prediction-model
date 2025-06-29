# app.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained model
try:
    model = joblib.load('C:\\Users\\raj\\ml\\laon prediction model\\loan_prediction_model.pkl')
except Exception as e:
    st.error("Failed to load the model.")
    st.exception(e)
    st.stop()

st.title(" Loan Approval Predictor")
st.markdown("Enter the applicant's details to check loan eligibility.")

# Sidebar inputs
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
property_area = st.selectbox("Property Area", ['Urban', 'Rural', 'Semiurban'])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in ₹)", min_value=0)
loan_term = st.number_input("Loan Term (in months)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])

# Convert to DataFrame (order must match training columns)
input_df = pd.DataFrame([{
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_term,
    'Credit_History': credit_history
}])


# Predict button
if st.button("Check Loan Status"):
    try:
        st.write("Input DataFrame:")
        st.dataframe(input_df)

        st.write("Predicting...")
        prediction = model.predict_proba(input_df)

        if prediction[0][1] > 0.5:
            result = 'High chance of being Approved'
        else:
            result = 'low chance of being Approved'
        st.success(f"Probability of Approval: {prediction[0][1]:.2f}")
        st.success(f"Loan Status: {result}")

    except Exception as e:
        st.error("Something went wrong during prediction.")
        st.exception(e)