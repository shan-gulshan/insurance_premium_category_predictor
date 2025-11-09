import streamlit as st
import requests

API_URl = "https://insurance-premium-category-predictor-jajs.onrender.com/health"

st.title("Insurance premium category predictor")
st.markdown("enter your details below: ")

# input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value = "mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)


if st.button("predict_premium_category"):
    input_data  = {
        "age" : age,
        "weight":weight,
        "height":height,
        "income_lpa": income_lpa,
        "smoker" : smoker,
        "city":city,
        "occupation":occupation
    }

    try:
        response  = requests.post(API_URl, json=input_data)
        result = response.json()
        if response.status_code==200:
            result = response.json()
            st.success(f"predicted insurance premium category: **{result['predicted_category']}**")
        else:
            st.error(f"API ERROR : {response.status_code}-{response.text}")
    
    except requests.exceptions.ConnectionError:
        st.error("could not connect to fast api server. make sure it is running on the 800 portf")
