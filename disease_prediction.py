import streamlit as st
import pandas as pd
import joblib

kidney_model = joblib.load("kidney_final_model.pkl")
liver_model = joblib.load("liver_pipeline.pkl")
parkinson_model = joblib.load("parkinson_pipeline.pkl")

st.set_page_config(page_title="Disease Prediction App", layout="wide")
st.title("🩺 Disease Prediction System")

st.sidebar.title("🏥Multiple Disease Prediction System")
page = st.sidebar.radio("Choose a model:", ["Kidney Disease", "Liver Disease", "Parkinson Disease"])

if page == "Kidney Disease":
    st.header("🧪 Kidney Disease Prediction")

    st.markdown(""" <style> .box {
    border: 2px solid #4A90E2;
    padding: 20px;
    border-radius: 12px;
    background-color: #f8faff;
    margin-bottom: 20px;}</style>""", unsafe_allow_html=True)

# ---------------------------
# BOX 1 - Basic Info
# ---------------------------
    with st.container():
        st.markdown("<div class='box'><h4>Basic Information</h4>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Age", 1, 120)
            blood_pressure = st.number_input("Blood Pressure", 50, 200)
        with col2:
            urine_specific_gravity = st.number_input("Urine Specific Gravity", 1.000, 1.050, step=0.001)
            albumin_in_urine = st.number_input("Albumin in Urine", 0, 5)
        with col3:
            blood_glucose_random = st.number_input("Blood Glucose Random", 0, 500)
            blood_urea = st.number_input("Blood Urea", 0, 300)

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------
# BOX 2 - Blood Parameters
# ---------------------------
    with st.container():
        st.markdown("<div class='box'><h4>Blood Parameters</h4>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            serum_creatinine = st.number_input("Serum Creatinine", 0.0, 20.0)
            sodium = st.number_input("Sodium", 100, 170)
        with col2:
             potassium = st.number_input("Potassium", 2.0, 10.0)
             hemoglobin = st.number_input("Hemoglobin", 3.0, 18.0)
        with col3:
             packed_cell_volume = st.number_input("Packed Cell Volume", 10, 60)
             white_blood_cell_count = st.number_input("WBC Count", 3000, 25000)
             red_blood_cell_count = st.number_input("RBC Count", 2.0, 8.0)

        st.markdown("</div>", unsafe_allow_html=True)

    submit = st.button("🔍Predict Kidney Disease")

    if submit:
         input_df = pd.DataFrame({
                   'age': [age],
                   'blood_pressure': [blood_pressure],
                   'urine_specific_gravity':[urine_specific_gravity ],
                   'albumin_in_urine': [albumin_in_urine],
                    'blood_glucose_random': [blood_glucose_random],
                   'blood_urea': [blood_urea],
                   'serum_creatinine': [serum_creatinine],
                  'sodium': [sodium],
                  'potassium': [potassium],
                 'hemoglobin': [hemoglobin],
                  'packed_cell_volume': [packed_cell_volume],
                 'white_blood_cell_count': [white_blood_cell_count],
                 'red_blood_cell_count': [red_blood_cell_count],
         })

         prediction = kidney_model.predict(input_df)[0]
         if prediction == 1:
            st.error("⚠️ Positive: Kidney disease detected")
         else:
            st.success("✅ Negative: No kidney disease")


if page == "Liver Disease":
    st.header("🧬 Liver Disease Prediction")

    col1,col2,col3=st.columns(3)
    with col1:
        Age =st.number_input("Age",1,120) 
        Direct_Bilirubin =st.number_input("Direct Bilirubin",0.0, 20.0)            
        Total_Bilirubin   =st.number_input("Total Bilirubin",0.0, 80.0)         
           
    with col2:
        Alkaline_Phosphotase =st.number_input("Alkaline Phosphotase(IU/L)",100, 3000)
        Alamine_Aminotransferase  =st.number_input("Alamine Aminotransferase",5, 2000)    
        Aspartate_Aminotransferase  =st.number_input("Aspartate Aminotransferase",5, 2000)
       
    with col3:                        
        Total_Protiens  =st.number_input("Total Protiens",3.0, 10.0)          
        Albumin       =st.number_input("Albumin",2.0, 6.5)               
        Albumin_and_Globulin_Ratio =st.number_input("Albumin and Globulin Ratio",0.1, 3.0) 
    

    submit = st.button("🔍Predict Liver Disease")

    if submit:
        input_df = pd.DataFrame({
            'Age': [Age],
            'Total_Bilirubin': [Total_Bilirubin],
            'Direct_Bilirubin': [Direct_Bilirubin],
            'Alkaline_Phosphotase': [Alkaline_Phosphotase],
            'Alamine_Aminotransferase': [Alamine_Aminotransferase],
            'Aspartate_Aminotransferase': [Aspartate_Aminotransferase],
            'Total_Protiens': [Total_Protiens],
            'Albumin': [Albumin],
            'Albumin_and_Globulin_Ratio': [Albumin_and_Globulin_Ratio]
        })
  
        prediction= liver_model.predict(input_df)[0]

        if prediction == 1:
            st.error("⚠️ Positive: Liver disease detected")
        else:
            st.success("✅ Negative: No liver disease")


if page == "Parkinson Disease":
    st.header("🧠 Parkinson Disease Prediction")

    
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            fo = st.number_input("MDVP:Fo(Hz)", 80.0, 300.0)
            jitter_percent = st.number_input("MDVP:Jitter(%)", 0.000, 0.050, step=0.001)
            ppq = st.number_input("MDVP:PPQ", 0.000, 0.050, step=0.001)
            shimmer_db = st.number_input("MDVP:Shimmer(dB)", 0.0, 2.0, step=0.01)

        with col2:
            flo = st.number_input("MDVP:Flo(Hz)", 60.0, 260.0)
            jitter_abs = st.number_input("MDVP:Jitter(Abs)", 0.0, 0.001, step=0.00001)
            shimmer = st.number_input("MDVP:Shimmer", 0.000, 0.200, step=0.001)
            apq3 = st.number_input("Shimmer:APQ3", 0.0, 0.10, step=0.001)

        with col3:
            apq5 = st.number_input("Shimmer:APQ5", 0.0, 0.10, step=0.001)
            mdvp_apq = st.number_input("MDVP:APQ", 0.0, 0.15, step=0.001)
            dda = st.number_input("Shimmer:DDA", 0.0, 0.30, step=0.001)
            hnr = st.number_input("HNR", 0.0, 40.0)

        st.markdown("</div>", unsafe_allow_html=True)


    
    with st.container():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            rpde = st.number_input("RPDE", 0.0, 1.0)

        with col2:
            spread1 = st.number_input("spread1", -10.0, 0.0)
            spread2 = st.number_input("spread2", 0.0, 1.0)
        with col3:
            
            d2 = st.number_input("D2", 0.0, 5.0)
            ppe = st.number_input("PPE", 0.0, 1.0)

    st.markdown("</div>", unsafe_allow_html=True)


    # ---------------------------
    # Predict Button
    # ---------------------------
    submit = st.button("🔍 Predict Parkinson Disease")


# ---------------------------
# DataFrame Conversion
# ---------------------------
if submit:
    input_df = pd.DataFrame({
        'MDVP:Fo(Hz)': [fo],
        'MDVP:Flo(Hz)': [flo],
        'MDVP:Jitter(%)': [jitter_percent],
        'MDVP:Jitter(Abs)': [jitter_abs],
        'MDVP:PPQ': [ppq],
        'MDVP:Shimmer': [shimmer],
        'MDVP:Shimmer(dB)': [shimmer_db],
        'Shimmer:APQ3': [apq3],
        'Shimmer:APQ5': [apq5],
        'MDVP:APQ': [mdvp_apq],
        'Shimmer:DDA': [dda],
        'HNR': [hnr],
        'RPDE': [rpde],
        'spread1': [spread1],
        'spread2': [spread2],
        'D2': [d2],
        'PPE': [ppe]
    })

    # ------------------------------
    # Make Prediction
    # ------------------------------
    proba = parkinson_model.predict_proba(input_df)[0][1]  

    if proba >= 0.51:
        st.error(f"⚠️ Parkinson Symptoms Detected (Probability: {proba:.2f})")
    else:
        st.success(f"✅ No Parkinson Symptoms (Probability: {proba:.2f})")

    
    