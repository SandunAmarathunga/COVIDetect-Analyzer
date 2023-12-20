import streamlit as st
import pandas as pd
import requests
import json


# call the predictions through endpoint
def get_prediction(data):
    url = 'https://askai.aiclub.world/d06b8d42-3088-4b12-95a6-c929f9c95aae'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r, '_content').decode("utf-8")
    print(response)
    return response


# web app
# title
st.title("Covid Symptom Analyzer")

# setting the image
st.image("banner-coronavirus_0.jpg", caption="covid")

# expander to say about the project
with st.expander("About the Project 📑"):
    st.subheader("The Project")
    st.markdown(
        "- This project is mainly focused on analysing symptoms and confirm whether the patient has Covid-19")

# tabs to navigate
tab1, tab2 = st.tabs(["Introduction 📊", "Predictions 💻"])

with tab1:
    st.subheader("Dataset")
    # reading the dataset
    data1 = pd.read_csv("CovidDataset.csv")
    st.dataframe(data1)

    # feature importance
    st.subheader("Main Variables which impact Covid-19")
    st.image("featureimportance.png", caption="Feature Importance")

with tab2:
    st.header("Prediction Dashboard")
    st.markdown("- User can fill the form.")
    st.markdown("- The predictions can be seen after completing the form")

    # prediction dashboard
    # get the link
    st.subheader("Predict the Possibility of having Covid-19")
    st.subheader("Please fill the form below")

    # Get inputs from the user
    fever = st.selectbox("Fever:", ["Yes", "No"])
    breathingProblem = st.selectbox("Breathing Problem:", ["Yes", "No"])
    runningNone = st.selectbox("Running Nose:", ["Yes", "No"])
    dryCough = st.selectbox("Dry Cough:", ["Yes", "No"])
    asthma = st.selectbox("Asthma:", ["Yes", "No"])
    headache = st.selectbox("Headache:", ["Yes", "No"])
    soreThroat = st.selectbox("Sore throat:", ["Yes", "No"])
    chronicLungDisease = st.selectbox("Chronic Lung Disease:", ["Yes", "No"])
    hyperTension = st.selectbox("Hyper Tension:", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes:", ["Yes", "No"])
    heartDisease = st.selectbox("Heart Disease:", ["Yes", "No"])
    abroadTravel = st.selectbox("Abroad travel:", ["Yes", "No"])
    fatigue = st.selectbox("Fatigue:", ["Yes", "No"])
    contactWithPatient = st.selectbox("Contact with COVID Patient:", ["Yes", "No"])
    familyWorkingInPublicExposedPlaces = st.selectbox("Family working in Public Exposed Places:", ["Yes", "No"])
    gastrointestinal = st.selectbox("Gastrointestinal:", ["Yes", "No"])
    visitedPublicExposedPlaces = st.selectbox("Visited Public Exposed Places:", ["Yes", "No"])
    attendedLargeGathering = st.selectbox("Attended Large Gathering:", ["Yes", "No"])
    wearingMasks = st.selectbox("Wearing Masks:", ["Yes", "No"])
    sanitizationFromMarket = st.selectbox("Sanitization from Market:", ["Yes", "No"])

    # Button to start predictions
    if st.button("Predict"):
        # Store user inputs in a dictionary
        input_data = {
            'Fever': fever,
            'Breathing Problem': breathingProblem,
            'Running Nose': runningNone,
            'Dry Cough': dryCough,
            'Asthma': asthma,
            'Headache': headache,
            'Sore throat': soreThroat,
            'Chronic Lung Disease': chronicLungDisease,
            'Hyper Tension': hyperTension,
            'Diabetes': diabetes,
            'Heart Disease': heartDisease,
            'Abroad travel': abroadTravel,
            'Fatigue': fatigue,
            'Contact with COVID Patient': contactWithPatient,
            'Family working in Public Exposed Places': familyWorkingInPublicExposedPlaces,
            'Gastrointestinal': gastrointestinal,
            'Visited Public Exposed Places': visitedPublicExposedPlaces,
            'Attended Large Gathering': attendedLargeGathering,
            'Wearing Masks': wearingMasks,
            'Sanitization from Market': sanitizationFromMarket
        }
        print(input_data)

        # Getting the predictions
        response = get_prediction(input_data)
        response = json.loads(response)
        response = json.loads(response['body'])
        prediction = response['predicted_label']
        print(prediction)
        if prediction == 'No':
            st.subheader('No trace of having Covid-19.')
        elif prediction == 'Yes':
            st.subheader('Have traces of having Covid-19.')
