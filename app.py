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
    if fever == 'Yes':
        fever = 1
    elif fever == 'No':
        fever = 0
    breathingProblem = st.selectbox("Breathing Problem:", ["Yes", "No"])
    if breathingProblem == 'Yes':
        breathingProblem = 1
    elif breathingProblem == 'No':
        breathingProblem = 0
    runningNone = st.selectbox("Running Nose:", ["Yes", "No"])
    if runningNone == 'Yes':
        runningNone = 1
    elif runningNone == 'No':
        runningNone = 0
    dryCough = st.selectbox("Dry Cough:", ["Yes", "No"])
    if dryCough == 'Yes':
        dryCough = 1
    elif dryCough == 'No':
        dryCough = 0
    asthma = st.selectbox("Asthma:", ["Yes", "No"])
    if asthma == 'Yes':
        asthma = 1
    elif asthma == 'No':
        asthma = 0
    headache = st.selectbox("Headache:", ["Yes", "No"])
    if headache == 'Yes':
        headache = 1
    elif headache == 'No':
        headache = 0
    soreThroat = st.selectbox("Sore throat:", ["Yes", "No"])
    if soreThroat == 'Yes':
        soreThroat = 1
    elif soreThroat == 'No':
        soreThroat = 0
    chronicLungDisease = st.selectbox("Chronic Lung Disease:", ["Yes", "No"])
    if chronicLungDisease == 'Yes':
        chronicLungDisease = 1
    elif chronicLungDisease == 'No':
        chronicLungDisease = 0
    hyperTension = st.selectbox("Hyper Tension:", ["Yes", "No"])
    if hyperTension == 'Yes':
        hyperTension = 1
    elif hyperTension == 'No':
        hyperTension = 0
    diabetes = st.selectbox("Diabetes:", ["Yes", "No"])
    if diabetes == 'Yes':
        diabetes = 1
    elif diabetes == 'No':
        diabetes = 0
    heartDisease = st.selectbox("Heart Disease:", ["Yes", "No"])
    if heartDisease == 'Yes':
        heartDisease = 1
    elif heartDisease == 'No':
        heartDisease = 0
    abroadTravel = st.selectbox("Abroad travel:", ["Yes", "No"])
    if abroadTravel == 'Yes':
        abroadTravel = 1
    elif abroadTravel == 'No':
        abroadTravel = 0
    fatigue = st.selectbox("Fatigue:", ["Yes", "No"])
    if fatigue == 'Yes':
        fatigue = 1
    elif fatigue == 'No':
        fatigue = 0
    contactWithPatient = st.selectbox("Contact with COVID Patient:", ["Yes", "No"])
    if contactWithPatient == 'Yes':
        contactWithPatient = 1
    elif contactWithPatient == 'No':
        contactWithPatient = 0
    familyWorkingInPublicExposedPlaces = st.selectbox("Family working in Public Exposed Places:", ["Yes", "No"])
    if familyWorkingInPublicExposedPlaces == 'Yes':
        familyWorkingInPublicExposedPlaces = 1
    elif familyWorkingInPublicExposedPlaces == 'No':
        familyWorkingInPublicExposedPlaces = 0
    gastrointestinal = st.selectbox("Gastrointestinal:", ["Yes", "No"])
    if gastrointestinal == 'Yes':
        gastrointestinal = 1
    elif gastrointestinal == 'No':
        gastrointestinal = 0
    visitedPublicExposedPlaces = st.selectbox("Visited Public Exposed Places:", ["Yes", "No"])
    if visitedPublicExposedPlaces == 'Yes':
        visitedPublicExposedPlaces = 1
    elif visitedPublicExposedPlaces == 'No':
        visitedPublicExposedPlaces = 0
    attendedLargeGathering = st.selectbox("Attended Large Gathering:", ["Yes", "No"])
    if attendedLargeGathering == 'Yes':
        attendedLargeGathering = 1
    elif attendedLargeGathering == 'No':
        attendedLargeGathering = 0
    wearingMasks = st.selectbox("Wearing Masks:", ["Yes", "No"])
    if wearingMasks == 'Yes':
        wearingMasks = 1
    elif wearingMasks == 'No':
        wearingMasks = 0
    sanitizationFromMarket = st.selectbox("Sanitization from Market:", ["Yes", "No"])
    if sanitizationFromMarket == 'Yes':
        sanitizationFromMarket = 1
    elif sanitizationFromMarket == 'No':
        sanitizationFromMarket = 0

    # Button to start predictions
    if st.button("Predict"):
        # Store user inputs in a dictionary
        input_data = {
            'Fever': int(fever),
            'Breathing Problem': int(breathingProblem),
            'Running Nose': int(runningNone),
            'Dry Cough': int(dryCough),
            'Asthma': int(asthma),
            'Headache': int(headache),
            'Sore throat': int(soreThroat),
            'Chronic Lung Disease': int(chronicLungDisease),
            'Hyper Tension': int(hyperTension),
            'Diabetes': int(diabetes),
            'Heart Disease': int(heartDisease),
            'Abroad travel': float(abroadTravel),
            'Fatigue': int(fatigue),
            'Contact with COVID Patient': int(contactWithPatient),
            'Family working in Public Exposed Places': int(familyWorkingInPublicExposedPlaces),
            'Gastrointestinal': int(gastrointestinal),
            'Visited Public Exposed Places': int(visitedPublicExposedPlaces),
            'Attended Large Gathering': int(attendedLargeGathering),
            'Wearing Masks': int(wearingMasks),
            'Sanitization from Market': float(sanitizationFromMarket)
        }
        print(input_data)

        # Getting the predictions
        response = get_prediction(input_data)
        response = json.loads(response)
        print(response)
        response = json.loads(response['body'])
        prediction = response['predicted_label']
        if prediction == 'Absence':
            st.subheader('No trace of having Covid-19.')
        elif prediction == 'Presence':
            st.subheader('Have traces of having Covid-19.')
