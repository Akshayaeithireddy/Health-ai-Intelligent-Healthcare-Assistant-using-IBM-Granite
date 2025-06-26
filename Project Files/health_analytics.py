# modules/health_analytics.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

def display_analytics():
    st.write("Visualize health data trends.")
    
    # Dummy health data
    data = {
        'Date': pd.date_range(start='2025-06-01', periods=10),
        'Heart Rate': [72, 75, 78, 70, 76, 74, 73, 77, 71, 75],
        'Blood Pressure': [120, 122, 125, 118, 121, 123, 119, 124, 117, 122]
    }
    df = pd.DataFrame(data)
    
    st.line_chart(df.set_index('Date'))
