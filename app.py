import streamlit as st
import time
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# Load the trained logistic regression model
model_path = "models/logistic_regression_model.pkl"
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# App Title
st.title("💳 Welcome to CC Fraud Detection Platform")

# Subheading
st.subheader("🔍 Enter your transaction details")

# Field names - NOW WITH 15 FEATURES to match the model
field_names = [
    "Amount", "Transaction Time", "Location Score", "Merchant Type", 
    "Card Usage", "Risk Factor", "Account Age", "Spending Pattern", 
    "Alert Count", "Device Score", "IP Risk", "Transaction Frequency",
    "Cross Border", "Merchant Category", "Time Since Last Transaction"
]

# Default values
default_values = {name: 0 for name in field_names}

# Create input fields
user_inputs = {}
cols = st.columns(3)  # Arrange fields in 3 columns for better UI
for idx, name in enumerate(field_names):
    with cols[idx % 3]:  # Distribute fields across columns
        user_inputs[name] = st.text_input(name, value=str(default_values[name]))

# Prediction function
def predict_fraud(inputs):
    # Convert inputs to numpy array
    input_array = np.array([float(inputs[name]) for name in field_names]).reshape(1, -1)
    prediction = model.predict(input_array)
    return "Fraud" if prediction[0] == 1 else "Not Fraud"

# Button Actions
col1, col2 = st.columns([1, 1])  # Buttons side by side

with col1:
    predict_button = st.button("🚀 Predict Transaction")

with col2:
    reset_button = st.button("🔄 Reset Fields")

# Reset Fields
if reset_button:
    st.rerun()

# Prediction with Progress Bar
if predict_button:
    try:
        with st.spinner("Processing transaction..."):
            progress_bar = st.progress(0)
            for i in range(5):  # Simulate loading time
                time.sleep(0.5)
                progress_bar.progress((i + 1) * 20)

            # Get prediction
            result = predict_fraud(user_inputs)

            # Display result
            if result == "Fraud":
                st.error(f"🚨 Prediction: **{result}**")
            else:
                st.success(f"✅ Prediction: **{result}**")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")