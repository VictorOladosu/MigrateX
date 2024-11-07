import streamlit as st
import pandas as pd
from models import Service, Metric
from components.charts import create_service_timeline

st.title("Cloud Services Management")

# Cloud Service Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Active Cloud Services", "15")
with col2:
    st.metric("Total Resources", "245")
with col3:
    st.metric("Avg Response Time", "125ms")

# Cloud Service Categories
st.header("Cloud Services")

tab1, tab2, tab3 = st.tabs(["Migration", "Security", "Cost Optimization"])

with tab1:
    st.subheader("Migration Services")
    migration_metrics = {
        "Completed Migrations": "45",
        "In Progress": "12",
        "Success Rate": "98%"
    }
    
    for metric, value in migration_metrics.items():
        st.metric(metric, value)

with tab2:
    st.subheader("Security Services")
    security_metrics = {
        "Security Score": "94%",
        "Vulnerabilities": "3",
        "Compliance Rate": "98%"
    }
    
    for metric, value in security_metrics.items():
        st.metric(metric, value)

with tab3:
    st.subheader("Cost Optimization")
    cost_metrics = {
        "Monthly Spend": "$45,000",
        "Savings": "$12,000",
        "Optimization Score": "87%"
    }
    
    for metric, value in cost_metrics.items():
        st.metric(metric, value)

# Resource Monitoring
st.header("Resource Monitoring")
monitoring_data = pd.DataFrame({
    'Resource': ['VM1', 'VM2', 'VM3', 'VM4'],
    'CPU': [45, 78, 32, 91],
    'Memory': [67, 45, 89, 34],
    'Status': ['Healthy', 'Warning', 'Healthy', 'Critical']
})

st.dataframe(monitoring_data)
