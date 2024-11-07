import json
from openai import OpenAI
import pandas as pd
from models import Service, Metric

def get_service_recommendations(service_data, metrics_data):
    client = OpenAI()
    
    # Prepare data for AI analysis
    analysis_prompt = {
        "service_metrics": metrics_data.to_dict(orient='records'),
        "current_status": service_data.to_dict(orient='records'),
        "task": "Please analyze the service metrics and provide recommendations for:"
        "1. Service optimization opportunities\n"
        "2. Cost reduction suggestions\n"
        "3. Performance improvements\n"
        "4. Resource allocation adjustments"
    }
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": json.dumps(analysis_prompt)
            }],
            response_format={"type": "json_object"}
        )
        
        recommendations = json.loads(response.choices[0].message.content)
        return recommendations
    except Exception as e:
        return {
            "error": str(e),
            "recommendations": [],
            "optimization_score": 0
        }

def get_category_specific_recommendations(category):
    services = Service.get_all_services()
    category_services = services[services['category'] == category]
    
    all_metrics = []
    for _, service in category_services.iterrows():
        metrics = Metric.get_service_metrics(service['id'])
        if not metrics.empty:
            all_metrics.append(metrics)
    
    if all_metrics:
        combined_metrics = pd.concat(all_metrics)
        return get_service_recommendations(category_services, combined_metrics)
    
    return {
        "recommendations": [],
        "optimization_score": 0
    }
