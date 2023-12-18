from flask import Flask, request, make_response
import time
import random
import requests
app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_packets():
    data = request.json
    time_recieve_serv=time.time()
    process()
    time_sent_serv=time.time()
    print("Packets at server")
    # quantity = data.get("quantity", 0)
    # timestamp = data.get("timestamp", 0)
    # start_time = time.time()
    # # Process the packets (simulated processing)
    # time.sleep(random.uniform(1, 3))
    # end_time = time.time()
    # round_trip_time = end_time - start_time
    # confirmation = {
    #     "received_quantity": quantity,
    #     "timestamp": timestamp,
    #     "round_trip_time": round_trip_time,
    # }
    # return jsonify(confirmation)
    
    
    device_id=data.get("device_id")
    packet_id=data.get("packet_id")
    device_url = "http://device1:5002"
    # device_url = "http://"+device_id+":50"
    # if device_id=='1':
    #     device_url=device_url+"51"
    # elif device_id=='2':
    #     device_url=device_url+"52"
    # elif device_id=='3':
    #     device_url=device_url+"53"
    payload = { "packet_id":data.get("packet_id"),
                "time_sent_dev": data.get("time_sent_dev"),
                "device_id":data.get("device_id"),
                "time_sent_lb":data.get("time_sent_lb"),
                "time_recieve_lb":data.get("time_recieve_lb"),
                "time_recieve_serv":time_recieve_serv,
                "time_sent_serv":time_sent_serv
                }
    response=requests.post(f"{device_url}/receive",json=payload)
    print(f"Server -> Device {device_id} | Packet : {packet_id}")
    return make_response('', 200)


def process():
    return
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
