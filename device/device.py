import os
import sys
import requests
import time
import random
from flask import Flask, request, make_response

app = Flask(__name__)

device_id = os.environ.get("DEVICE_ID", "1")
load_balancer_url = "http://load_balancer:5000"  # Use the service name defined in Docker Compose


packet_id = random.randint(1, 100)
payload = { "packet_id": packet_id,
            "time_sent_lb": time.time(),
            "device_id": device_id
            }
response = requests.post(f"{load_balancer_url}/receive", json=payload)

# confirmation = {
#     "received_quantity": response.json().get("received_quantity", 0),
#     "timestamp_sent": payload["timestamp"],
#     "timestamp_received": response.json().get("timestamp_received", 0),
#     "round_trip_time": response.json().get("round_trip_time", 0),
#     "device_id": device_id,
# }

print(f"Device {device_id} -> Load balancer | Packet: {packet_id}")
sys.stdout.flush()
time.sleep(random.uniform(1, 5))

@app.route('/receive', methods=['POST'])
def receive_packets():
    data=request.json
    div_id=data.get("device_id")
    pack_id=data.get("packet_id")
    print(f"Packet recieved at device {div_id} | Packet: {pack_id}")
    return make_response('', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
