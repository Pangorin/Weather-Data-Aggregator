from dotenv import load_dotenv
import requests
import os
import json
from datetime import datetime

def run():
    print("Start extraction process...")

    # Load environment variables
    load_dotenv()

    # Get configuration
    API_KEY = os.getenv("API_KEY")
    CITIES_STR = os.getenv("CITIES")

    # Ensure the script can run
    if not API_KEY or not CITIES_STR:
        print("Error: API key or cities not found in secret file.")
        print("Ensure your secret file is correctly setup.")
        return
    
    # Get the absolute path of the current project folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(BASE_DIR, "data", "raw")
    os.makedirs(output_dir, exist_ok=True)

    # Convert comma-seperated string to Python list
    cities = CITIES_STR.split(',')

    # Fetch data
    for city in cities:
        base_url = 'http://api.openweathermap.org/data/2.5/weather'

        # Parameters for API request
        params = {
            'q': city,
            'appid': API_KEY
        }

        try:
            # GET request
            response = requests.get(base_url, params = params)

            # Raise exception for bad status codes
            response.raise_for_status()

            data = response.json()

            # Timestamp for unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(output_dir, f"{city.strip()}_{timestamp}.json")

            # Write data
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Successfully fetched data for {city.strip()} to {filename}")

        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred for city {city.strip()}: {http_err}')
        except requests.exceptions.RequestException as request_err:
            print(f"Request error occurred for city {city.strip()}: {request_err}")
        except Exception as err:
            print(f'An unexpected error occurred for city {city.strip()}: {err}')

if __name__ == '__main__':
    run()