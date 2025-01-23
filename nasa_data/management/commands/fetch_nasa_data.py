import csv
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch live fire data from NASA FIRMS'

    def handle(self, *args, **kwargs):
        # Example NASA FIRMS API endpoint
        url = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/09d1c3e4f877cfe35f7c6f77f3d0e44a/VIIRS_NOAA20_NRT/world/1"
        response = requests.get(url)

        if response.status_code == 200:
            file_path = 'static/nasa_fire_data.csv'
            with open(file_path, 'w') as file:
                file.write(response.text)
            self.stdout.write(self.style.SUCCESS(f"Successfully saved NASA fire data to {file_path}"))
        else:
            self.stderr.write(self.style.ERROR("Failed to fetch NASA fire data"))
