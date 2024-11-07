import streamlit as st
import pandas as pd
import plotly.express as px
from models import Service, Metric
from components.charts import create_cost_breakdown

st.title("Cost Management")

# Cost Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Monthly Cost", "$125,000")
with col2:
    st.metric("Cost Variance", "-5%")
with col3:
    st.metric("Savings Opportunity", "$15,000")

# Cost Categories
st.header("Cost by Service Category")

cost_data = pd.DataFrame({
    'category': ['Data', 'Cloud', 'IoT', 'Security'],
    'name': ['Storage', 'Compute', 'Devices', 'Tools'],
    'cost': [45000, 35000, 25000, 20000]
})

cost_breakdown = create_cost_breakdown(cost_data)
st.plotly_chart(cost_breakdown, use_container_width=True)

# Cost Optimization Recommendations
st.header("Cost Optimization Recommendations")

recommendations = pd.DataFrame({
    'Resource': ['Unused VMs', 'Over-provisioned Storage', 'Idle Services'],
    'Potential Savings': ['$5,000', '$3,000', '$7,000'],
    'Impact': ['Medium', 'Low', 'High'],
    'Implementation': ['Easy', 'Medium', 'Complex']
})

st.dataframe(recommendations)

# Cost Trends
st.header("Cost Trends")
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
cost_trends = pd.DataFrame({
    'Date': dates,
    'Cost': [100000, 98000, 115000, 125000, 120000, 118000, 
             122000, 125000, 123000, 121000, 124000, 125000]
})

fig = px.line(cost_trends, x='Date', y='Cost', title='Monthly Cost Trend')
st.plotly_chart(fig, use_container_width=True)
