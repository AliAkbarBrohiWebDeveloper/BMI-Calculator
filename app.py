
import streamlit as st
st.title("BMI Calculator")
st.write("Enter your height and weight to calculate your BMI")

height=st.number_input("Height(in meters)",min_value=0.5,max_value=3.0,value=1.75)
weight=st.number_input("Weight(in Kilograms)",min_value=10,max_value=90,value=70)
if st.button("Calculate BMI"):
    if height>0 and weight>0:
        bmi=weight/(height**2)
        st.success(f"Your Bmi is {bmi:.2f}")
        if bmi<18.5:
            st.warning("You are underWeight")
        elif bmi<24.9:
            st.success("You have a normal weight")
        elif bmi<29.9:
            st.error("You are obese")



    else:
            st.error("Enter a vailed height and weight values")
