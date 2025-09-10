from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location')
def get_location():
    user_ip = request.remote_addr
    try:
        r = requests.get(f"http://ip-api.com/json/{user_ip}")
        data = r.json()
        lat = data.get('lat', 0)
        lon = data.get('lon', 0)
        city = data.get('city', 'Unknown')
        country = data.get('country', 'Unknown')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append({
            'lat': lat,
            'lon': lon,
            'city': city,
            'country': country,
            'time': timestamp
        })
        return jsonify({
            'lat': lat,
            'lon': lon,
            'city': city,
            'country': country,
            'time': timestamp
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
