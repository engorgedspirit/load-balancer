import os
import sys
import requests
import time
import random

manager_id = os.environ.get("MANAGER_ID", "1")
worker_url = "http://worker:5000"  # Use the service name defined in Docker Compose

while True:
    quantity = random.randint(1, 10)
    payload = {"quantity": quantity, "timestamp": time.time(), "manager_id": manager_id}
    response = requests.post(f"{worker_url}/receive", json=payload)

    confirmation = {
        "received_quantity": response.json().get("received_quantity", 0),
        "timestamp_sent": payload["timestamp"],
        "timestamp_received": response.json().get("timestamp_received", 0),
        "round_trip_time": response.json().get("round_trip_time", 0),
        "manager_id": manager_id,
    }

    print(f"Manager {manager_id}: Sent {quantity} packets to worker. Confirmation: {confirmation}")
    sys.stdout.flush()  # Add this line to flush the output

    time.sleep(random.uniform(1, 5))
