import random
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

def generate_sample_metrics():
    return {
        'cpu_usage': round(random.uniform(0, 100), 2),
        'memory_usage': round(random.uniform(0, 100), 2),
        'response_time': round(random.uniform(10, 1000), 2),
        'error_rate': round(random.uniform(0, 5), 2)
    }

def create_service_status_chart(df):
    fig = px.pie(df, names='status', title='Service Status Distribution')
    return fig

def create_metric_timeline(df, metric_name):
    fig = px.line(df, x='timestamp', y='value',
                  title=f'{metric_name} Over Time')
    return fig

def format_number(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    return str(num)
