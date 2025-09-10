from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()
    lat = data.get('lat', 0)
    lon = data.get('lon', 0)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history.append({
        'lat': lat,
        'lon': lon,
        'time': timestamp
    })
    return jsonify({'status': 'success'})

@app.route('/history')
def get_history():
    return jsonify(history)
