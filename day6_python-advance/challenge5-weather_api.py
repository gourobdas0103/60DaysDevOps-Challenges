from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# 🌍 Replace with your OpenWeatherMap API key
API_KEY = "aaa3889159763eeeba03eee0a6284fe7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    """🌤️ Fetch live weather data for a given city."""
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "❌ City parameter is required"}), 400

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Unknown error")}), response.status_code

        weather_data = {
            "🌆 City": data["name"],
            "🌡️ Temperature (°C)": data["main"]["temp"],
            "🌦️ Weather": data["weather"][0]["description"],
            "💧 Humidity (%)": data["main"]["humidity"],
            "🌬️ Wind Speed (m/s)": data["wind"]["speed"]
        }
        return jsonify(weather_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)