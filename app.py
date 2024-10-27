from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Example endpoint for basic pit stop strategy
@app.route('/calculate_strategy', methods=['POST'])
def calculate_strategy():
    data = request.json
    laps = data.get('laps')
    tire_degradation = data.get('tire_degradation')
    
    # Simple strategy: Pit every 15 laps or if tire degradation > threshold
    pit_stops = [lap for lap in range(15, laps + 1, 15)]
    if tire_degradation > 70:
        pit_stops = [lap for lap in range(10, laps + 1, 10)]

    return jsonify({
        "recommended_pit_stops": pit_stops
    })

if __name__ == '__main__':
    app.run(debug=True)
