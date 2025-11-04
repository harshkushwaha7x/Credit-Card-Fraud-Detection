import streamlit as st
import time
import pickle
import numpy as np

# Load the trained logistic regression model
model_path = "models/logistic_regression_model.pkl"
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

st.title("💳 Welcome to CC Fraud Detection Platform")
st.subheader("🔍 Enter your transaction details")

# The 9 key fields you actually want user input for
ui_fields = [
    "Amount", "Transaction Time", "Location Score", "Merchant Type", 
    "Card Usage", "Risk Factor", "Account Age", "Spending Pattern", "Alert Count"
]

# The 15 total features the model expects
model_features = [
    "Amount", "Transaction Time", "Location Score", "Merchant Type", 
    "Card Usage", "Risk Factor", "Account Age", "Spending Pattern", "Alert Count",
    "Device Score", "IP Risk", "Transaction Frequency",
    "Cross Border", "Merchant Category", "Time Since Last Transaction"
]

# Default placeholder values for missing ones
default_fill_values = {
    "Device Score": 0.0,
    "IP Risk": 0.0,
    "Transaction Frequency": 0.0,
    "Cross Border": 0.0,
    "Merchant Category": 0.0,
    "Time Since Last Transaction": 0.0
}

# Create input fields for 9 important features
user_inputs = {}
cols = st.columns(3)
for idx, name in enumerate(ui_fields):
    with cols[idx % 3]:
        user_inputs[name] = st.text_input(name, value="0")

# Prediction function
def predict_fraud(inputs):
    # Merge user inputs + default filler features
    complete_input = []
    for feature in model_features:
        if feature in inputs:
            complete_input.append(float(inputs[feature]))
        else:
            complete_input.append(default_fill_values.get(feature, 0.0))

    input_array = np.array(complete_input).reshape(1, -1)
    prediction = model.predict(input_array)
    return "Fraud" if prediction[0] == 1 else "Not Fraud"

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    predict_button = st.button("🚀 Predict Transaction")
with col2:
    reset_button = st.button("🔄 Reset Fields")

if reset_button:
    st.rerun()

if predict_button:
    with st.spinner("Processing transaction..."):
        progress_bar = st.progress(0)
        for i in range(5):
            time.sleep(0.3)
            progress_bar.progress((i + 1) * 20)

        try:
            result = predict_fraud(user_inputs)
            if result == "Fraud":
                st.error(f"🚨 Prediction: **{result}**")
            else:
                st.success(f"✅ Prediction: **{result}**")
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
