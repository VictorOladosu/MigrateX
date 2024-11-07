import time
import threading
from datetime import datetime
import pandas as pd
from database import get_db_connection
from utils import generate_sample_metrics

class MonitoringSystem:
    def __init__(self):
        self.alert_thresholds = {
            'cpu_usage': 80.0,
            'memory_usage': 85.0,
            'response_time': 800.0,
            'error_rate': 2.0
        }
        self.active_alerts = {}
        self._monitor_thread = None
        self._stop_flag = False

    def start_monitoring(self):
        if self._monitor_thread is None:
            self._stop_flag = False
            self._monitor_thread = threading.Thread(target=self._monitoring_loop)
            self._monitor_thread.daemon = True
            self._monitor_thread.start()

    def stop_monitoring(self):
        self._stop_flag = True
        if self._monitor_thread:
            self._monitor_thread.join()
            self._monitor_thread = None

    def _monitoring_loop(self):
        conn = get_db_connection()
        cur = conn.cursor()
        
        while not self._stop_flag:
            try:
                # Get all services
                cur.execute("SELECT id, name, category FROM services")
                services = cur.fetchall()
                
                for service_id, service_name, category in services:
                    metrics = generate_sample_metrics()
                    
                    # Store metrics
                    for metric_name, value in metrics.items():
                        cur.execute("""
                            INSERT INTO metrics (service_id, metric_name, value)
                            VALUES (%s, %s, %s)
                        """, (service_id, metric_name, value))
                    
                    # Check for alerts
                    self._check_alerts(service_id, service_name, metrics)
                
                conn.commit()
                time.sleep(60)  # Update every minute
                
            except Exception as e:
                print(f"Monitoring error: {str(e)}")
                time.sleep(60)  # Wait before retry
        
        cur.close()
        conn.close()

    def _check_alerts(self, service_id, service_name, metrics):
        for metric_name, value in metrics.items():
            if metric_name in self.alert_thresholds:
                threshold = self.alert_thresholds[metric_name]
                alert_key = f"{service_id}_{metric_name}"
                
                if value > threshold and alert_key not in self.active_alerts:
                    self.active_alerts[alert_key] = {
                        'service_name': service_name,
                        'metric_name': metric_name,
                        'value': value,
                        'threshold': threshold,
                        'timestamp': datetime.now()
                    }
                elif value <= threshold and alert_key in self.active_alerts:
                    del self.active_alerts[alert_key]

    def get_active_alerts(self):
        return list(self.active_alerts.values())

# Global monitoring system instance
monitoring_system = MonitoringSystem()
