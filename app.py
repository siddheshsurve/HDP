from unittest import result
import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('model.sav','rb'))

st.title("Heart disease predication")

def report():
    age = st.number_input("Age")
    s= st.radio("Sex",('male','female'))
    if s == 'male':
        sex=1
    else:
        sex=0
    cp = st.number_input("Chest Pain")
    trestbps = st.number_input("TrestBPS")
    chol = st.number_input("Cholesterol")
    fbs = st.number_input("FBS")
    restecg = st.number_input("restecg")
    thalach = st.number_input("thalach")
    exang = st.number_input("Exang")
    oldpeak = st.number_input("OldPeak")
    slope = st.number_input("Slope")
    ca = st.number_input("CA")
    thal = st.number_input("thal")
    

    user_report_data={
        'age':age,
        'jersy':sex,
        'cp':cp,
        'tresbps':trestbps,
        'chol':chol,
        'fbs':fbs,
        'restecg':restecg,
        'thalach':thalach,
        'exang':exang,
        'oldpeak':oldpeak,
        'slope':slope,
        'ca':ca,
        'tghal':thal
     }
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data
    
user_data=report()
st.write(user_data)
final_result=model.predict(user_data)
if st.button("Predict"):
   
    if final_result==1:
        st.subheader('yes you might have heart disease')
    if final_result==0:
        st.subheader('congratulation you are healthy')



