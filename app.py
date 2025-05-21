import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")

st.divider()

st.write("This app predicts the salary of a data scientist based on the years of experience and education level.")

years = st.number_input("Enter the years at company",value = 1, step =1, min_value = 0)
jobrate = st.number_input("Enter the job rates",value=3.5, step = 0.5, min_value = 0.0)

X=[years,jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("press the button for salary prediction")

st.divider()

if predict:

    st.balloons()

    X1=np.array([X])

    prediction = float(model.predict(X1)[0])

    st.write(f"Salary prediction is {prediction:,.2f}")





else:
    "Please press the button to get the prediction"