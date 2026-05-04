from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return "Wave Cleanup Backend Running"

# Simulated AI detection API
@app.route('/detect', methods=['POST'])
def detect():
    hotspots = []

    for _ in range(5):
        hotspots.append({
            "lat": random.uniform(20.5, 21.5),
            "lng": random.uniform(72.5, 73.5),
            "waste_type": random.choice(["Plastic", "Metal", "Organic"])
        })

    return jsonify({"hotspots": hotspots})


if __name__ == '__main__':
    app.run(debug=True)
