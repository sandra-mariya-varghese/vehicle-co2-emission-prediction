import streamlit as st
import pandas as pd
import numpy as np
import base64
# import joblib  # Uncomment when your trained model is ready

# ----- Set Background Image -----
def set_bg_image(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the background image function
set_bg_image("background.jpg")

# ----- Title -----
st.title("🚗 Vehicle CO₂ Emissions Predictor")

# ----- Input Fields -----
make = st.text_input("Make", "Toyota")
model = st.text_input("Model", "Corolla")
vehicle_class = st.selectbox("Vehicle Class", ["COMPACT", "SUV", "MID-SIZE", "SUBCOMPACT"])
engine_size = st.slider("Engine Size (L)", 1.0, 8.0, 2.0)
cylinders = st.selectbox("Cylinders", [3, 4, 6, 8, 10, 12])
transmission = st.selectbox("Transmission", ["AS", "AM", "AV", "M", "A"])
fuel_type = st.selectbox("Fuel Type", ["Z", "X", "E", "D", "N"])
fuel_city = st.slider("Fuel Consumption (City L/100km)", 2.0, 30.0, 10.0)
fuel_hwy = st.slider("Fuel Consumption (Hwy L/100km)", 2.0, 30.0, 7.0)
fuel_comb = st.slider("Fuel Consumption (Comb L/100km)", 2.0, 30.0, 8.5)
fuel_mpg = st.slider("Fuel Consumption (Comb MPG)", 5, 100, 30)

# ----- Predict Button -----
if st.button("Predict CO₂ Emission"):
    # Create DataFrame for model input
    input_data = pd.DataFrame({
        "make": [make],
        "model": [model],
        "vehicle_class": [vehicle_class],
        "engine_size": [engine_size],
        "cylinders": [cylinders],
        "transmission": [transmission],
        "fuel_type": [fuel_type],
        "fuel_consumption_city": [fuel_city],
        "fuel_consumption_hwy": [fuel_hwy],
        "fuel_consumption_comb(l/100km)": [fuel_comb],
        "fuel_consumption_comb(mpg)": [fuel_mpg]
    })

    # Load your trained model here (if available)
    # model = joblib.load("your_model.pkl")
    # prediction = model.predict(input_data)

    # Mock prediction for demonstration
    prediction = 210  # Replace with: prediction[0]

    # Display the result
    st.success(f"🌱 Predicted CO₂ Emissions: {prediction} g/km")
