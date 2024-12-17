from dotenv import load_dotenv
import os
import requests
from weather_transformer import WeatherTransformer  # Add this line

class WeatherExtractor:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cities = ['London', 'Bangalore']
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.transformer = WeatherTransformer()  # Add this line
        
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
                raw_data = response.json()
                
                # Transform the data
                transformed_data = self.transformer.transform_data(raw_data)
                
                # Print formatted data
                print(f"\nWeather in {transformed_data['city']}:")
                print(f"Temperature: {transformed_data['temperature_c']}°C ({transformed_data['temperature_f']}°F)")
                print(f"Humidity: {transformed_data['humidity']}%")
                print(f"Conditions: {transformed_data['conditions']}")
                
            except Exception as e:
                print(f"Error getting weather data for {city}: {str(e)}")
if __name__ == "__main__":
    extractor = WeatherExtractor()
    extractor.get_weather_data()
