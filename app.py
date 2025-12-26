import streamlit as st
import requests

# --- CUSTOM CSS ---
st.markdown(
    """
    <style>
    /* Change the font for all headers */
    h1, h2, h3, h4, h5, h6, .css-1d391kg { 
        font-family: 'Times New Roman', serif !important;
    }
    /* Optional: change sidebar font too */
    .css-1d391kg, .css-qbe2hs {
        font-family: 'Times New Roman', serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- COLOR SETTINGS ---
st.sidebar.header("Customize Colors")d:

# Background and text
bg_color = st.sidebar.color_picker("Background Color", "#420505")
text_color = st.sidebar.color_picker("Text Color", "#000000")

# Button
button_color = st.sidebar.color_picker("Button Color", "#4CAF50")
button_text_color = st.sidebar.color_picker("Button Text Color", "#FFFFFF")

# Input boxes
input_bg_color = st.sidebar.color_picker("Input Box Background", "#FFFFFF")
input_text_color = st.sidebar.color_picker("Input Text Color", "#000000")

# Result boxes
success_bg_color = st.sidebar.color_picker("Success Box Background", "#D4EDDA")
success_text_color = st.sidebar.color_picker("Success Text Color", "#155724")

error_bg_color = st.sidebar.color_picker("Error Box Background", "#F8D7DA")
error_text_color = st.sidebar.color_picker("Error Text Color", "#721C24")

# --- APPLY CUSTOM CSS ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .stButton>button {{
        background-color: {button_color};
        color: {button_text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Wine Quality Predictor", layout="centered")

st.title(" Wine Quality Prediction")
st.write("Enter the wine features to predict its quality.")

# Input fields
alcohol = st.number_input("Alcohol Level", min_value=0.0, max_value=20.0, value=10.0)
density = st.number_input("Density Level", min_value=0.0, max_value=2.0, value=0.99)
pH = st.number_input("pH Level", min_value=0.0, max_value=5.0, value=3.2)

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
            st.success(f"Wine Quality: **{result['predicted_quality']}**")
        else:
            st.error("Error: Could not get prediction")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
