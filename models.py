from pydantic import BaseModel
from datetime import datetime

class SystemMetrics(BaseModel):
    timestamp: datetime
    cpu_usage: float
    ram_usage: float
