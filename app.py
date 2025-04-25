import streamlit as st 
import time


st.set_page_config(page_title="BMI Calculator", page_icon=":bar_chart:", layout="wide")


st.title("BMI Calculator")
st.markdown("""
Your Body Mass Index (BMI) is a measure of body fat based on your weight and height. It's a simple calculation using a person's height and weight.
""")


col1, col2 = st.columns(2)


with col1:
    weight = st.number_input("Weight (Kg)", min_value=0, max_value=500, value=0, step=1)


with col2:
    height = st.number_input("Height (cm)", min_value=0, max_value=300, value=0, step=1)


if height > 0 and weight > 0:
    bmi = weight / (height / 100) ** 2
    st.subheader(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        st.error("You are underweight")
    elif 18.5 <= bmi <= 24.9:
        st.success("You are normal")
    elif 25 <= bmi <= 29.9:
        st.warning("You are overweight")
    else:
        st.error("You are obese")
else:
    st.info("Please enter valid height and weight values.")
