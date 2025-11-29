import streamlit as st

st.set_page_config(
    page_title="Telco Analytics Hub",
    page_icon="📡",
    layout="centered"
)

st.title("📡 Telco Analytics Hub")

st.markdown("""
Welcome to the Customer Retention Portal.

### Workflow:
1. Go to **Predictor** to enter customer details and calculate churn risk.
2. Once a prediction is made, go to **AI Advisor** to discuss retention strategies.

👈 **Select a page from the sidebar to get started.**
""")

st.info("System Status: Connected to Google Cloud Storage Model Registry.")
