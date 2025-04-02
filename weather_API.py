import requests
import datetime
from config import API_KEY, BASE_URL

def get_weather_data(city):
    """fetch current temperature, humidity & past 12-month total rainfall for a city."""
    
    # Fetch current weather data
    current_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}"
    response = requests.get(current_url)
    data = response.json()

    if "error" in data:
        return None  # handle invalid locations

    total_rainfall = 0  # Initialize yearly rainfall

    # fetch rainfall data for the past 12 months
    for i in range(1, 13):
        past_date = (datetime.datetime.now() - datetime.timedelta(days=i * 30)).strftime("%Y-%m-01")
        history_url = f"{BASE_URL}/history.json?key={API_KEY}&q={city}&dt={past_date}"
        
        history_response = requests.get(history_url)
        history_data = history_response.json()

        if "error" in history_data:
            return None  # handle errors

        total_rainfall += history_data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]

    return {
        "temperature": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "rainfall": total_rainfall  # total annual rainfall
    }
