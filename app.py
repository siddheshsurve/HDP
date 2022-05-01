from unittest import result
import streamlit as st
import pickle
import pandas as pd


modelhdp = pickle.load(open('model.sav','rb'))


st.markdown("<h1 style='text-align: center'>HEART DISEASE PREDICTION</h1>", unsafe_allow_html=True)
st.markdown(""" <br> <br> """, True)
def report():
    age = st.number_input("Age")
    st.markdown(""" <br>""", True)

    s= st.radio("Sex",('male','female'))
    if s == 'male':
        sex=1
    else:
        sex=0
    st.markdown(""" <br>""", True)

    # cp = st.number_input("Chest Pain")
    c= st.radio("Chest Pain",('0','1','2','3'))
    if c == '0':
        cp = 0
    elif c == '1':
        cp=1
    elif c == '2':
        cp=2
    else :
        cp=3
    st.markdown(""" <br>""", True)

    trestbps = st.number_input("TrestBPS")
    st.markdown(""" <br>""", True)

    chol = st.number_input("Cholesterol")
    st.markdown(""" <br>""", True)

    # fbs = st.number_input("FBS")
    f= st.radio("Fasting Blood Sugar",('Yes','No'))
    if f == 'Yes':
        fbs=1
    else:
        fbs=0
    st.markdown(""" <br>""", True)

    # restecg = st.number_input("restecg")
    recg= st.radio("Resting Electrocardiogram (ECG) Results",('Noraml','having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'showing probable or definite left ventricular hypertrophy by Estes'))
    if recg == 'Normal':
        restecg=0
    elif recg == 'having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
        restecg=1
    else :
        restecg=2
    st.markdown(""" <br>""", True)

    thalach = st.number_input("thalach")
    st.markdown(""" <br>""", True)

    # exang = st.number_input("Exang")
    exg= st.radio("Exercise Induced Angina",('Yes','No'))
    if exg == 'Yes':
        exang=1
    else:
        exang=0
    st.markdown(""" <br>""", True)

    oldpeak = st.number_input("OldPeak")
    st.markdown(""" <br>""", True)

    # slope = st.number_input("Slope") 
    slp= st.radio("Slope of the peak exercise ST Segment",('0','1','2','3'))
    if slp == '0':
        slope = 0
    elif slp == '1':
        slope=1
    elif slp == '2':
        slope=2
    else :
        slope=3
    st.markdown(""" <br>""", True)

    # ca = st.number_input("CA")
    cA= st.radio("CA (Number of major vessels)",('0','1','2','3','4'))
    if cA == '0':
        ca = 0
    elif cA == '1':
        ca=1
    elif cA == '2':
        ca=2
    elif cA =='3' :
        ca=3
    else :
        ca=4
    st.markdown(""" <br>""", True)
    
    # thal = st.number_input("thal")
    thl= st.radio("Thalassemia (thal)",('0','1','2','3'))
    if thl == '0':
        thal = 0
    elif thl == '1':
        thal=1
    elif thl == '2':
        thal=2
    else :
        thal=3
    

    user_report_data={
        'age':age,
        'sex':sex,
        'cp':cp,
        'trestbps':trestbps,
        'chol':chol,
        'fbs':fbs,
        'restecg':restecg,
        'thalach':thalach,
        'exang':exang,
        'oldpeak':oldpeak,
        'slope':slope,
        'ca':ca,
        'thal':thal
     }
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data
    
user_data=report()
st.write(user_data)
final_result=modelhdp.predict(user_data)
if st.button("Predict"):
   
    if final_result==1:
        st.markdown("<h1 style='text-align: center; color: red;'>You Might have Heart disease, Take care</h1>", unsafe_allow_html=True)
    if final_result==0:
        st.markdown("<h1 style='text-align: center; color: green;'>Congratulations you are healthy</h1>", unsafe_allow_html=True)



