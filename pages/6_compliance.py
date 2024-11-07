import streamlit as st
import pandas as pd
import plotly.express as px
from models import Service, Metric

st.title("Compliance Monitoring")

# Compliance Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Overall Compliance", "94%")
with col2:
    st.metric("Policy Violations", "23")
with col3:
    st.metric("Critical Findings", "2")

# Compliance Categories
st.header("Compliance by Category")

compliance_data = pd.DataFrame({
    'Category': ['Data Privacy', 'Security', 'Operational', 'Regulatory'],
    'Compliance_Rate': [95, 92, 88, 97],
    'Violations': [5, 8, 7, 3]
})

fig = px.bar(compliance_data, x='Category', y='Compliance_Rate',
             title='Compliance Rate by Category')
st.plotly_chart(fig, use_container_width=True)

# Active Violations
st.header("Active Policy Violations")

violations = pd.DataFrame({
    'Policy': ['Data Retention', 'Access Control', 'Encryption', 'Audit Logging'],
    'Severity': ['High', 'Medium', 'Low', 'Medium'],
    'Status': ['Open', 'In Progress', 'Open', 'Resolved'],
    'Due Date': ['2024-02-01', '2024-01-25', '2024-02-15', '2024-01-20']
})

st.dataframe(violations)

# Compliance Tasks
st.header("Upcoming Compliance Tasks")

tasks = pd.DataFrame({
    'Task': ['Security Audit', 'Policy Review', 'Training', 'Risk Assessment'],
    'Due Date': ['2024-02-01', '2024-01-25', '2024-02-15', '2024-01-20'],
    'Owner': ['Security Team', 'Compliance', 'HR', 'Risk'],
    'Status': ['Pending', 'In Progress', 'Not Started', 'In Progress']
})

st.dataframe(tasks)

# Compliance Reports
st.header("Compliance Reports")
report_types = st.multiselect(
    "Select Report Type",
    ["Security Compliance", "Data Privacy", "Operational", "Regulatory"]
)

if report_types:
    st.info("Selected reports will be generated and displayed here")
