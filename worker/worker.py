from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_packets():
    data = request.json
    quantity = data.get("quantity", 0)
    timestamp = data.get("timestamp", 0)

    start_time = time.time()
    # Process the packets (simulated processing)
    time.sleep(random.uniform(1, 3))
    end_time = time.time()

    round_trip_time = end_time - start_time

    confirmation = {
        "received_quantity": quantity,
        "timestamp": timestamp,
        "round_trip_time": round_trip_time,
    }

    return jsonify(confirmation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
