from datetime import datetime

class WeatherTransformer:
    def __init__(self):
        self.temperature_unit = 'C'  # Default to Celsius
    
    def transform_data(self, raw_data):
        """
        Transform raw weather data into structured format
        """
        transformed_data = {
            'city': raw_data['name'],
            'timestamp': datetime.utcnow(),
            'temperature_c': raw_data['main']['temp'],
            'temperature_f': self.celsius_to_fahrenheit(raw_data['main']['temp']),
            'humidity': raw_data['main']['humidity'],
            'conditions': raw_data['weather'][0]['main']
        }
        
        return transformed_data
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return round((celsius * 9/5) + 32, 2)