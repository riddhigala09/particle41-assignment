from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_time_and_ip():
    # Get the current timestamp
    current_time = datetime.utcnow().isoformat() + "Z"  # UTC ISO 8601 format

    # Get the IP address of the client
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    return jsonify({
        "timestamp": current_time,
        "ip": client_ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)