import streamlit as st
from datetime import datetime
from components.monitoring import monitoring_system

def display_alerts():
    alerts = monitoring_system.get_active_alerts()
    
    if alerts:
        st.error(f"🚨 Active Alerts ({len(alerts)})")
        for alert in alerts:
            with st.expander(f"Alert: {alert['service_name']} - {alert['metric_name']}", expanded=True):
                st.markdown(f"""
                    - **Service:** {alert['service_name']}
                    - **Metric:** {alert['metric_name']}
                    - **Current Value:** {alert['value']:.2f}
                    - **Threshold:** {alert['threshold']:.2f}
                    - **Since:** {alert['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
                """)
    else:
        st.success("✅ No active alerts")

def display_service_alerts(service_name):
    alerts = [a for a in monitoring_system.get_active_alerts() if a['service_name'] == service_name]
    
    if alerts:
        st.warning(f"⚠️ Active Alerts for {service_name}")
        for alert in alerts:
            st.info(f"""
                {alert['metric_name']}: {alert['value']:.2f} (Threshold: {alert['threshold']:.2f})
                Since: {alert['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
            """)
