import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const handleCityChange = (e) => {
        setCity(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get('http://localhost:5000/weather', {
                params: { city }
            });
            setWeather(response.data.weather);
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    };

    return (
        <div className="App">
            <h1>Weather Forecast</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" value={city} onChange={handleCityChange} placeholder="Enter city" />
                <button type="submit">Get Weather</button>
            </form>
            {weather && (
                <div>
                    <h2>Weather in {weather.city}</h2>
                    <p>Temperature: {weather.temperature} °C</p>
                    <p>Description: {weather.description}</p>
                    <img src={`http://openweathermap.org/img/wn/${weather.icon}.png`} alt="Weather icon" />
                </div>
            )}
        </div>
    );
}

export default App;
