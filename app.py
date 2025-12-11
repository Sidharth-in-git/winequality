import streamlit as st
import requests

st.set_page_config(page_title="Wine Quality Predictor", layout="centered")

st.title("🍷 Wine Quality Prediction")
st.write("Enter the wine features to predict its quality.")

# Input fields
alcohol = st.number_input("Alcohol", min_value=0.0, max_value=20.0, value=10.0)
density = st.number_input("Density", min_value=0.0, max_value=2.0, value=0.99)
pH = st.number_input("pH", min_value=0.0, max_value=5.0, value=3.2)

# Backend URL
API_URL = "http://127.0.0.1:8000/predict"

if st.button("Predict Quality"):
    # JSON data to send
    data = {
        "alcohol": alcohol,
        "density": density,
        "pH": pH
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Wine Quality: **{result['predicted_quality']}** ⭐")
        else:
            st.error("Error: Could not get prediction")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
