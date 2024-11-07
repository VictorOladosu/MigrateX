from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import pandas as pd
from database import get_db_connection

@dataclass
class Service:
    id: int
    name: str
    category: str
    status: str
    created_at: datetime

    @staticmethod
    def get_all_services():
        conn = get_db_connection()
        df = pd.read_sql("SELECT * FROM services", conn)
        conn.close()
        return df

    @staticmethod
    def add_service(name: str, category: str, status: str):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO services (name, category, status) VALUES (%s, %s, %s)",
            (name, category, status)
        )
        conn.commit()
        cur.close()
        conn.close()

@dataclass
class Metric:
    id: int
    service_id: int
    metric_name: str
    value: float
    timestamp: datetime

    @staticmethod
    def get_service_metrics(service_id: int):
        conn = get_db_connection()
        df = pd.read_sql(
            "SELECT * FROM metrics WHERE service_id = %s",
            conn,
            params=(service_id,)
        )
        conn.close()
        return df
