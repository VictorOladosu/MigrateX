import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_dashboard_charts(df):
    status_counts = df['status'].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=status_counts.index,
        values=status_counts.values,
        hole=.3
    )])
    
    fig.update_layout(
        title="Service Status Distribution",
        showlegend=True,
        height=400
    )
    
    return fig

def create_service_timeline(df, metric_name):
    fig = px.line(
        df,
        x='timestamp',
        y='value',
        title=f'{metric_name} Timeline'
    )
    
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Value",
        height=400
    )
    
    return fig

def create_cost_breakdown(df):
    fig = px.treemap(
        df,
        path=['category', 'name'],
        values='cost',
        title='Service Cost Breakdown'
    )
    
    return fig
