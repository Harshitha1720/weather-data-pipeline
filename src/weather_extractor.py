import requests
import os
from dotenv import load_dotenv

class WeatherExtractor:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cities = ['London','Bangalore']
        self.api_key = os.getenv('WEATHER_API_KEY')
        
    def get_weather_data(self):
        """
        Get weather data for predefined cities
        """
        if not self.api_key:
            print("Error: No API key found. Please check your .env file")
            return
            
        for city in self.cities:
            try:
                params = {
                    'q': city,
                    'appid': self.api_key,
                    'units': 'metric'
                }
                
                response = requests.get(self.base_url, params=params)
                data = response.json()
                
                print(f"\nWeather in {city}:")
                print(f"Temperature: {data['main']['temp']}°C")
                print(f"Humidity: {data['main']['humidity']}%")
                print(f"Conditions: {data['weather'][0]['main']}")
                
            except Exception as e:
                print(f"Error getting weather data for {city}: {str(e)}")

if __name__ == "__main__":
    extractor = WeatherExtractor()
    extractor.get_weather_data()
