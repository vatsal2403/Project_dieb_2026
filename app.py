import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score,  precision_score, recall_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

st.title("""DIabetic Prediction App which we design using Machine Learning and for the prediction of the diabetes in the patient""")
# I am going to load my model
rf_mod=pickle.load(open('model_rf.pkl', 'rb'))
I=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']

# create empty dict to take input from user
input_data={}
for i in l:
    input_data[i]=st.number_input(f'Enter the value for {i}', key=i, value=0.0)

# model understand the data in the form of dataframe
# i am converting my dict to dataframe
unknown_data=pd.DataFrame(input_data, index=[0])


if st.button('Predict the health status of the patient'):
    result=rf_mod.predict(unknown_data)
    if result[0]==0:
        st.subheader(f'The predicted health status of the patient isNon-Diabetic)')
    else:
        st.subheader(f'The predicted health status of the patient is: {result[0]} (Diabetic)')

        