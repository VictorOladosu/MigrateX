import streamlit as st
import pandas as pd
from models import Service, Metric
from components.charts import create_service_timeline

st.title("Security Services")

# Security Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Security Score", "94%")
with col2:
    st.metric("Active Threats", "3")
with col3:
    st.metric("Incidents Today", "12")

# Security Service Categories
st.header("Security Services")

tab1, tab2, tab3 = st.tabs(["Threat Detection", "Incident Response", "Compliance"])

with tab1:
    st.subheader("Threat Detection")
    threat_metrics = {
        "Detected Threats": "45",
        "False Positives": "3",
        "Detection Rate": "99.7%"
    }
    
    for metric, value in threat_metrics.items():
        st.metric(metric, value)

with tab2:
    st.subheader("Incident Response")
    response_metrics = {
        "Open Incidents": "5",
        "Avg Response Time": "15min",
        "Resolution Rate": "95%"
    }
    
    for metric, value in response_metrics.items():
        st.metric(metric, value)

with tab3:
    st.subheader("Compliance Status")
    compliance_metrics = {
        "Compliance Score": "98%",
        "Policy Violations": "2",
        "Audit Status": "Passed"
    }
    
    for metric, value in compliance_metrics.items():
        st.metric(metric, value)

# Security Incidents
st.header("Recent Security Incidents")
incidents_data = pd.DataFrame({
    'Incident': [f'INC-{i}' for i in range(1, 6)],
    'Type': ['Malware', 'Phishing', 'Access Violation', 'DDoS', 'Data Leak'],
    'Severity': ['High', 'Medium', 'Low', 'High', 'Medium'],
    'Status': ['Open', 'Closed', 'Open', 'In Progress', 'Closed']
})

st.dataframe(incidents_data)
