import csv
from datetime import datetime
import os

class WeatherStorage:
    def __init__(self):
        self.data_folder = 'data'  # Folder to store our CSV files
        self.filename = 'weather_data.csv'
        self.setup_storage()
        
    def setup_storage(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            
    def save_data(self, weather_data):
        """Save weather data to CSV"""
        file_path = os.path.join(self.data_folder, self.filename)
        file_exists = os.path.exists(file_path)
        
        # Define our CSV columns
        fieldnames = ['timestamp', 'city', 'temperature_c', 'temperature_f', 
                     'humidity', 'conditions']
        
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header only if file is new
            if not file_exists:
                writer.writeheader()
                
            writer.writerow(weather_data)
