import streamlit as st
import pandas as pd
from models import Service, Metric
from components.charts import create_service_timeline

st.title("Data Management Services")

# Service Categories
st.header("Data Service Categories")

tab1, tab2, tab3 = st.tabs(["Data Governance", "Data Quality", "Master Data Management"])

with tab1:
    st.subheader("Data Governance")
    governance_metrics = {
        "Data Classifications": "85%",
        "Policy Compliance": "92%",
        "Data Catalog Coverage": "78%"
    }
    
    for metric, value in governance_metrics.items():
        st.metric(metric, value)

with tab2:
    st.subheader("Data Quality")
    quality_metrics = {
        "Data Accuracy": "94%",
        "Completeness": "88%",
        "Consistency": "91%"
    }
    
    for metric, value in quality_metrics.items():
        st.metric(metric, value)

with tab3:
    st.subheader("Master Data Management")
    mdm_metrics = {
        "Golden Records": "250K",
        "Match Rate": "95%",
        "Data Sources": "12"
    }
    
    for metric, value in mdm_metrics.items():
        st.metric(metric, value)

# Service Request Form
st.sidebar.header("Request Data Service")
service_type = st.sidebar.selectbox(
    "Service Type",
    ["Data Governance", "Data Quality", "MDM"]
)
description = st.sidebar.text_area("Description")
if st.sidebar.button("Submit Request"):
    # Add service request logic here
    st.sidebar.success("Service request submitted successfully!")
