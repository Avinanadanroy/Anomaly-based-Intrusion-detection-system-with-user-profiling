import os
from datetime import datetime

LOG_FILE = "logs/anomalies.log"

def log_anomaly(user_id, data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().isoformat()
        f.write(f"[{timestamp}] Anomaly Detected - User: {user_id} | Data: {data}\n")
