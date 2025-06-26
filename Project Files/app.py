# app.py
import streamlit as st
from modules.disease_prediction import predict_disease
from modules.treatment_plans import get_treatment_plan
from modules.patient_chat import chat_with_healthai
from modules.health_analytics import display_analytics

st.set_page_config(page_title="HealthAI Assistant", layout="wide")
st.title("🏥 HealthAI: Intelligent Healthcare Assistant")

menu = ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "Patient Chat":
    st.header("🗣️ Patient Chat")
    query = st.text_area("Ask your medical question below:")
    if st.button("Get Answer") and query:
        response = chat_with_healthai(query)
        st.success(response)

elif choice == "Disease Prediction":
    st.header("🔍 Disease Prediction")
    symptoms = st.text_input("Enter your symptoms (comma-separated):")
    if st.button("Predict Disease") and symptoms:
        result = predict_disease(symptoms)
        st.info(result)

elif choice == "Treatment Plans":
    st.header("💊 Treatment Plans")
    condition = st.text_input("Enter diagnosed condition:")
    if st.button("Get Treatment Plan") and condition:
        treatment = get_treatment_plan(condition)
        st.success(treatment)

elif choice == "Health Analytics":
    st.header("📊 Health Analytics")
    display_analytics()
