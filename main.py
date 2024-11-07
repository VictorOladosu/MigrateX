import streamlit as st
import pandas as pd
from database import init_db
from models import Service, Metric
from components.metrics import display_service_metrics
from components.charts import create_dashboard_charts

# Initialize the database
init_db()

# Page configuration
st.set_page_config(
    page_title="Enterprise Service Management",
    page_icon="🏢",
    layout="wide"
)

# Main dashboard
st.title("Enterprise Service Management Dashboard")

# Service Overview
col1, col2, col3, col4 = st.columns(4)
services_df = Service.get_all_services()

with col1:
    st.metric("Total Services", len(services_df))
with col2:
    active_services = len(services_df[services_df['status'] == 'active'])
    st.metric("Active Services", active_services)
with col3:
    st.metric("Service Categories", len(services_df['category'].unique()))
with col4:
    incident_count = len(services_df[services_df['status'] == 'incident'])
    st.metric("Active Incidents", incident_count)

# Service Status Chart
st.subheader("Service Status Overview")
status_chart = create_dashboard_charts(services_df)
st.plotly_chart(status_chart, use_container_width=True)

# Recent Activity
st.subheader("Recent Activity")
recent_services = services_df.sort_values('created_at', ascending=False).head(5)
st.dataframe(recent_services[['name', 'category', 'status', 'created_at']])

# Quick Actions
st.sidebar.title("Quick Actions")
if st.sidebar.button("Request New Service"):
    st.sidebar.success("Service request form opened")

# Service Health Overview
st.subheader("Service Health Overview")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Data Services")
    display_service_metrics("data")
    
with col2:
    st.markdown("### Cloud Services")
    display_service_metrics("cloud")
