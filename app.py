import streamlit as st
import pickle
import numpy as np

# load files
model = pickle.load(open("artificats\model.pkl", "rb"))
scaler = pickle.load(open("artificats/scaler.pkl", "rb"))

st.title("🌱 Crop Recommendation System")

# inputs
N = st.number_input("Nitrogen", 0, 200)
P = st.number_input("Phosphorus", 0, 200)
K = st.number_input("Potassium", 0, 200)

temperature = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0)
ph = st.number_input("pH Value", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0.0, 3000.0)

# button
if st.button("Predict Crop"):
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    
    # scaling
    data = scaler.transform(data)
    
    # prediction
    pred = model.predict(data)
    print(pred)
    # decode
    
    
    st.success(f"🌾 Recommended Crop: {pred[0]}")