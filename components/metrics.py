import streamlit as st
import pandas as pd
from models import Service, Metric

def display_service_metrics(category):
    services = Service.get_all_services()
    category_services = services[services['category'] == category]
    
    for _, service in category_services.iterrows():
        metrics = Metric.get_service_metrics(service['id'])
        if not metrics.empty:
            latest_metrics = metrics.sort_values('timestamp').iloc[-1]
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    f"{service['name']} - CPU",
                    f"{latest_metrics['value']}%"
                )
            with col2:
                st.metric(
                    f"{service['name']} - Memory",
                    f"{latest_metrics['value']}%"
                )
