# File: streamlit_app/app.py

import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression

# Load the pre-trained model
MODEL_PATH = "Logistic_regression_model.pkl"  # Assuming the model file is in the same directory
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Streamlit web application
st.title('Linear Regression Model Deployment')

# User Input
user_input = st.number_input("Enter the number:")

# Make Prediction
if st.button('Predict'):
    prediction = model.predict([[user_input]])[0]
    st.write(f"Predicted Output: {prediction:.2f}")  # Limiting to 2 decimal points for better readability
