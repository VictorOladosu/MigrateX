import streamlit as st
import pandas as pd
import plotly.express as px
from models import Service, Metric
from components.charts import create_service_timeline

st.title("IoT Services Platform")

# IoT Platform Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Connected Devices", "1,234")
with col2:
    st.metric("Active Gateways", "45")
with col3:
    st.metric("Data Points/sec", "5,678")

# IoT Service Categories
st.header("IoT Services")

tab1, tab2, tab3 = st.tabs(["Platform Services", "Monitoring", "Analytics"])

with tab1:
    st.subheader("Platform Services")
    platform_metrics = {
        "Device Uptime": "99.9%",
        "Message Success Rate": "99.7%",
        "Active Connections": "1,234"
    }
    
    for metric, value in platform_metrics.items():
        st.metric(metric, value)

with tab2:
    st.subheader("Monitoring Services")
    monitoring_metrics = {
        "Alert Count": "23",
        "Response Time": "45ms",
        "Device Health": "98%"
    }
    
    for metric, value in monitoring_metrics.items():
        st.metric(metric, value)

with tab3:
    st.subheader("Analytics Services")
    analytics_metrics = {
        "Processed Data": "45 GB",
        "Active Models": "12",
        "Accuracy": "95%"
    }
    
    for metric, value in analytics_metrics.items():
        st.metric(metric, value)

# Device Management
st.header("Device Management")
device_data = pd.DataFrame({
    'Device': [f'Device-{i}' for i in range(1, 6)],
    'Type': ['Sensor', 'Gateway', 'Sensor', 'Controller', 'Sensor'],
    'Status': ['Online', 'Online', 'Offline', 'Online', 'Online'],
    'Last Seen': ['2 min ago', '1 min ago', '15 min ago', '1 min ago', '5 min ago']
})

st.dataframe(device_data)
