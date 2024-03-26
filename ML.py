import streamlit as st
import pickle

from sklearn.linear_model import LinearRegression

# Load the pre-trained model
with open("C:/Users/harsh/OneDrive/Pictures/Desktop/ADCET_WORKSHOP/Logistic_regression_model.pkl", 'rb') as file:
    model = pickle.load(file)

# Streamlit web application
st.title('Linear Regression Model Deployment')

# User Input
user_input = st.number_input("Enter the number:")

# Make Prediction
prediction = model.predict([[user_input]])  # Corrected user_input without quotes
prediction = (prediction)  # Extracting the single prediction value from the array

# Display The Prediction
st.write(f"Salary for {user_input} Years Experienced person is : {prediction}")