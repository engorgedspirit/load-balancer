from flask import Flask, request, make_response
import time
import requests
import sys

app = Flask(__name__)
def send_server(data,time_recieve_lb):
    server_url = "http://server:5001"
    payload = { "packet_id":data.get("packet_id"),
                "time_sent_dev": data.get("time_sent_dev"),
                "device_id":data.get("device_id"),
                "time_sent_lb":time.time(),
                "time_recieve_lb":time_recieve_lb
                }
    response = requests.post(f"{server_url}/receive", json=payload)
    packet_id=payload.get("packet_id")
    # confirmation = {
    #     "received_quantity": response.json().get("received_quantity", 0),
    #     "timestamp_sent": payload["timestamp"],
    #     "timestamp_received": response.json().get("timestamp_received", 0),
    #     "round_trip_time": response.json().get("round_trip_time", 0),   
    # }
    # print(f"Load Balacner: Sent packets to server. Confirmation: {confirmation}")
    print(f"Load balancer -> Server | Packet: {packet_id}")
    sys.stdout.flush()

@app.route('/receive', methods=['POST'])
def receive_packets():
    data = request.json
    time_recieve_lb = time.time()
    send_server(data,time_recieve_lb)
    # time.sleep(random.uniform(1, 3))
    return make_response('', 200)
    # return jsonify(confirmation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

