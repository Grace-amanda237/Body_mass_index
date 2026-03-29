import streamlit as st 

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg", min_value=1.0)
status = st.radio("Select your height format:", ("cms", "meters", "feet"))

# Initialisation de la variable bmi
bmi = 0.0

try:
    if status == 'cms': # Corrigé 'cas' en 'cms'
        height = st.number_input("Centimeters")
        if height > 0:
            bmi = weight / ((height / 100) ** 2) 
            
    elif status == 'meters':
        height = st.number_input("Meters")
        if height > 0:
            bmi = weight / (height ** 2)
            
    elif status == 'feet':
        height = st.number_input("Feet")
        if height > 0:
            bmi = weight / ((height / 3.281) ** 2)

except ZeroDivisionError:
    st.error("Height cannot be zero")

if st.button("Calculate BMI"):
    if bmi > 0:
        st.write(f'Your BMI index is {round(bmi, 2)}')
        
        if bmi < 18.5:
            st.warning('You are underweight')
        elif 18.5 <= bmi < 24.9:
            st.success('You are Healthy')
        elif 24.9 <= bmi < 29.9:
            st.error('You are overweight')
        elif bmi >= 30:
            st.warning('You are extremely overweight')
    else:
        st.error("Please enter a valid height.")