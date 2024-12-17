import requests
import os

class WeatherExtractor:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cities = ['London']
        # Get API key from environment variable
        self.api_key = os.getenv('WEATHER_API_KEY')
        
    def get_weather_data(self):
        """
        Get weather data for predefined cities
        """
        if not self.api_key:
            print("Error: No API key found. Set WEATHER_API_KEY environment variable")
            return
            
        try:
            params = {
                'q': self.cities[0],
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            print(f"Weather in {self.cities[0]}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Conditions: {data['weather'][0]['main']}")
            
        except Exception as e:
            print(f"Error getting weather data: {str(e)}")

if __name__ == "__main__":
    extractor = WeatherExtractor()
    extractor.get_weather_data()
