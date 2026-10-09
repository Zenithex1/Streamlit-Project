import streamlit as st
import pandas as pd
import pickle as pk
with open("Covid_Classification.pickle","rb")as f:
    model =pk.load(f)
st.title("Covid Prediction")

Cough_symptoms = st.selectbox("Cough symptoms= ",[True,False])
Fever = st.selectbox("Fever  ",[True,False])
Sore_throat = st.selectbox("Sore thorat ",[True,False])
Shortness_of_breath = st.selectbox("Shortness of breath",[True,False])
Headache = st.selectbox("Headache  ",[True,False])
known_contact  = st.selectbox("Known contact  ",["Abroad","Contact with confirmed","Other"])
if known_contact == "Abroad":
    known_contact = 0
elif known_contact == "Contact with confirmed":
    known_contact = 1
else:
    known_contact = 2

if st.button("Predict"):
    st.success("The form is submitted succesfully")
    data = {
    "Cough_symptoms": [Cough_symptoms],
    "Fever": [Fever],
    "Sore_throat": [Sore_throat],
    "Shortness_of_breath": [Shortness_of_breath],
    "Headache": [Headache],
    "Known_contact": [known_contact]}
    df = pd.DataFrame(data)
    st.write(df)
    result = model.predict(df)[0]
    st.write(f'Chance of getting Corona Virus:{result}')