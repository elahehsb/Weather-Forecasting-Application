# Purpose:
# This code creates a Flask backend:

# Weather Data Endpoint: Provides an endpoint to fetch weather data for a given city using the OpenWeatherMap API and return the relevant weather information.


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API Key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City not provided'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve weather data'}), response.status_code

    data = response.json()
    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    return jsonify({'weather': weather_info})

if __name__ == '__main__':
    app.run(debug=True)
