import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import requests
import json

st.write("""
# Application to predict the time for the new york city taxi trips
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    PU = st.sidebar.text_input('PU Location ID')
    DO = st.sidebar.text_input('DO Location ID')
    trip_distance = st.sidebar.number_inputs("Trip Distance", value=10, min_value=1, max_value=100)

    input_dict = {'PuLocationID':PU,
            'DOLocation':DO,
            'trip_distance': trip_distance,
            }
    
    return input_dict 


input_dict = user_input_features()

if st.button('Predict'):
    response = requests.post(
        url = "http://127.0.0.1:4444.predict",
        data=json.dumps(input_dict)
    )

    st.write(f"El tiempo estimado del viaje es {response.text['prediction']} minutos")

# df = user_input_features()

# st.subheader('User Input parameters')
# st.write(df)

# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target

# clf = RandomForestClassifier()
# clf.fit(X, Y)

# prediction = clf.predict(df)
# prediction_proba = clf.predict_proba(df)

# st.subheader('Class labels and their corresponding index number')
# st.write(iris.target_names)

# st.subheader('Prediction')
# st.write(iris.target_names[prediction])
# #st.write(prediction)

# st.subheader('Prediction Probability')
# st.write(prediction_proba)