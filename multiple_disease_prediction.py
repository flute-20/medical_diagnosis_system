import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css("style.css")

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heartdisease_model.sav', 'rb'))
hypothyroid_model = pickle.load(open('hypothyroid_model.sav', 'rb'))
lung_cancer_model = pickle.load(open('lung_cancer_model.sav', 'rb'))
parkinson_model = pickle.load(open('parkinson_model.sav', 'rb'))

# Navigation bar
selected = option_menu('Multiple Disease Prediction System',
                       ['Diabetes Prediction', 
                        'Heart Disease Prediction',
                        'Hypothyroid Prediction',
                        'Lung Cancer Prediction',
                        'Parkinson Disease Prediction'],
                       icons=['activity', 'heart', 'clipboard', 'lungs', 'person'],
                       default_index=0,
                       orientation="horizontal")

# ===================== Diabetes Prediction =====================
if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    # Creating input fields
    #columns for input fields

    col1 , col2 , col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies" )
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Level" )
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value"  )
    with col2:
        Insulin = st.text_input("Insulin Level" )
    with col3:
        Bmi = st.text_input("BMI value" )
    with col1:  
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value" )
    with col2:
        Age = st.text_input("Enter your Age")

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        
        scaler = pickle.load(open('diab_scaler.sav' , 'rb'))

        input_data = ([[Pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , Bmi , DiabetesPedigreeFunction , Age]])
        
        std_data = scaler.transform(input_data)

        diab_prediction = diabetes_model.predict(std_data)

        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        
        else:
            diab_diagnosis = 'The person is Non-diabetic'

    st.success(diab_diagnosis)

# ===================== Heart Disease Prediction =====================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1 , col2 , col3 = st.columns(3)
    with col1:
        age = st.text_input("Enter you Age")
    with col2:
        sex = st.text_input("Person's Sex")
    with col3:
        cp = st.text_input("Chest Pain level")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Cholestrol Level")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar value")
    with col1:
        restecg = st.text_input("Resting ECG value")
    with col2:
        thalach = st.text_input("Heart rate value")
    with col3:
        exang = st.text_input("Exer induced angina val")
    with col1:
        oldpeak = st.text_input("St depression value")
    with col2:
        slope = st.text_input("The Se value")
    with col3:
        ca = st.text_input("No.of Major Vessels")
    with col1:
        thal = st.text_input("Thalassemina stage")

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        
        scaler = pickle.load(open('heart_scaler.sav' , 'rb'))

        input_data = ([[age ,sex ,cp , trestbps , chol , fbs , restecg , thalach , exang , oldpeak , slope , ca ,thal]])
        
        std_data = scaler.transform(input_data)

        heart_prediction = heart_disease_model.predict(std_data)

        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having Heart Disease'
        
        else:
            heart_diagnosis = 'The person does not have Heart Disease'

    st.success(heart_diagnosis)

# ===================== Hypothyroid Prediction =====================
if selected == 'Hypothyroid Prediction':

    st.title('Hypothyroid Prediction using ML')

    col1 , col2 , col3 = st.columns(3)

    with col1:
        age = st.text_input("Enter Your age")
    with col2:
        sex = st.text_input("Person's Sex")
    with col3:
        on_thyroxine = st.text_input("Thyroxine value")
    with col1:
        tsh = st.text_input("Enter TSH value")
    with col2:
        t3_measured = st.text_input("Enter T3_measured value")
    with col3:
        t3 = st.text_input("Enter T3 value")
    with col1:
        tt = st.text_input("Enter TT value")

    hypothyroid_diagnosis = ''

    if st.button('Thyroid Test Result'):
        
        scaler = pickle.load(open('hypothy_scaler.sav' , 'rb'))

        input_data = ([[age , sex , on_thyroxine , tsh , t3_measured , t3 , tt ]])
        
        std_data = scaler.transform(input_data)

        thyroid_prediction = hypothyroid_model.predict(std_data)

        if(thyroid_prediction[0] == 1):
            hypothyroid_diagnosis = 'The person is having Hypothyroid'
        
        else:
            hypothyroid_diagnosis = 'The person does not have Hypothyroid'

    st.success(hypothyroid_diagnosis)


# ===================== Lung Cancer Prediction =====================
if selected == 'Lung Cancer Prediction':

    st.title('Lung Cancer Prediction using ML')

    col1 , col2 , col3 = st.columns(3)

    with col1:
        gender = st.text_input("Person's gender")
    with col2:
        age = st.text_input("Person's age")
    with col3:
        smoking = st.text_input("Smoking level")
    with col1:
        yellow_fingers = st.text_input("Yellow_fingers Level")
    with col2:
        anxiety = st.text_input("Enter anxiety Level")
    with col3:
        peer_pressure = st.text_input("Enter Peer_Pressure Value")
    with col1:
        chronic_disease = st.text_input("Chronic Disease Value")
    with col2:
        fatigue = st.text_input("Enter Fatigue value")
    with col3:
        allergy = st.text_input("Enter Allergy level")
    with col1:
        wheezing = st.text_input("Enter Wheezing value")
    with col2:
        alcohol_consuming = st.text_input("Enter Alcohol consumption value")
    with col3:
        coughing = st.text_input("Enter Coughing Level")
    with col1:
        shortness_of_breath = st.text_input("Enter Shortness Breath level")
    with col2:
        swallowing_difficulty = st.text_input("Enter Swallowing difficulty value")
    with col3:
        chestpain = st.text_input('Enter chest pain Level')
    
    lungcancer_diagnosis = ''

    if st.button('Lung Cancer Test Result'):
        
        scaler = pickle.load(open('lung_scaler.sav' , 'rb'))

        input_data = ([[gender , age , smoking , yellow_fingers , anxiety , peer_pressure , chronic_disease , fatigue , allergy , wheezing , alcohol_consuming , coughing , shortness_of_breath , swallowing_difficulty , chestpain]])
        
        std_data = scaler.transform(input_data)

        lung_cancer_prediction = lung_cancer_model.predict(std_data)

        if(lung_cancer_prediction[0] == 1):
            lungcancer_diagnosis = 'The person is having Lung Cancer '
        
        else:
            lungcancer_diagnosis = 'The person does not have Lung Cancer'

    st.success(lungcancer_diagnosis)

    

# ===================== Parkinson Prediction =====================
if selected == 'Parkinson Disease Prediction':
    st.title('Parkinson Disease Prediction using ML')

    col1 , col2 , col3 = st.columns(3)

    with col1:
        mdvp_fo = st.text_input('Enter Fo(hz) value')
    with col2:
        mdvp_fhi = st.text_input('Enter Fhi(hz) value')
    with col3:
        mdvp_flo = st.text_input('Enter Flo(hz) value')
    with col1:
        mdvp_jitter = st.text_input('Enter Jitter(%) value')
    with col2:
        mdvp_jitter_abs = st.text_input('Enter Jitter(abs) value')
    with col3:
        mdvp_rap = st.text_input('Enter MDVP_Rap value')
    with col1:
        mdvp_ppq = st.text_input('Enter  MDVP_ppq value')
    with col2:
        jitter_ddp = st.text_input('Enter Jitter:DDP value')
    with col3:
        mdvp_shimmer = st.text_input('Enter MDVP:Shimmer value')
    with col1:
        mdvp_shimmer_db = st.text_input('Enter MDVP:Shimmer(dB) value')
    with col2:
        shimmer_apq3= st.text_input('Enter Shimmer:APQ3 value')
    with col3:
        shimmer_apq5 = st.text_input('Enter Shimmer:APQ5 value')
    with col1:
        mdvp_apq = st.text_input('Enter MDVP:APQ value')
    with col2:
        shimmer_dda = st.text_input('Enter Shimmer:DDA value')
    with col3:
        nhr = st.text_input('Enter NHR value')
    with col1:
        hnr = st.text_input('Enter HNR value')
    with col2:
        rpde = st.text_input('Enter RPDE value')
    with col3:
        dfa = st.text_input('Enter DFA value')
    with col1:
        spread1 = st.text_input('Enter spread1 value')
    with col2:
        spread2 = st.text_input('Enter spread2 value')
    with col3:
        d2 = st.text_input('Enter D2 value')
    with col1:
        ppe = st.text_input('Enter PPE value')

    parkinson_diagnosis = ''

    if st.button('Parkinson disease Test Result'):
        
        scaler = pickle.load(open('parkin_scaler.sav' , 'rb'))

        input_data = ([[gender , age , smoking , yellow_fingers , anxiety , peer_pressure , chronic_disease , fatigue , allergy , wheezing , alcohol_consuming , coughing , shortness_of_breath , swallowing_difficulty , chestpain]])
        
        std_data = scaler.transform(input_data)

        parkinson_prediction = parkinson_model.predict(std_data)

        if(parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'The person is having Parkinson disease '
        
        else:
            parkinson_diagnosis = 'The person does not have Parkinson disease'

    st.success(parkinson_diagnosis)

    