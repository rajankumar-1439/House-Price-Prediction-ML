import streamlit as st 
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction Model")

st.divider()
st.write("### Enter the details of the house:")

st.divider()
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=0)
living_area = st.number_input("Living Area", min_value=0, value=2000)
condition = st.number_input("Condition", min_value=0, value=3)
numberofschool = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

x = [[bedrooms, bathrooms, living_area, condition, numberofschool]]

predict_button = st.button("Predict Price") 
if predict_button:
    st.balloons()
    x_arr = np.array(x)
    prediction = model.predict(x_arr)[0]
    st.write(f"Price prediction id {prediction:.2f}")

else:
    st.write("Click the Predict Price button to see the estimated house price.")    