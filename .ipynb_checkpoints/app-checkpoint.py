import streamlit as st
import pickle
import numpy as np

# Load crop model
crop_model = pickle.load(open("artificats/crop_model.pkl", "rb"))

# Title
st.title("🌱 Crop Recommendation System")

st.write("Enter soil and environmental details:")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temp = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Value")
rainfall = st.number_input("Rainfall (mm)")

# Button
if st.button("Predict Crop 🚀"):

    # Prepare input
    input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])

    # Prediction
    crop = crop_model.predict(input_data)[0]

    # Output
    st.success(f"🌾 Recommended Crop: {crop}")