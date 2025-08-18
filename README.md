# Weather Data Aggregator
Simple ETL pipeline to collect weather data for a few cities and store it for historical analysis.

## Phase 0: 
1. Get API access:
- Go to OpenWeatherAPI, generate an API key.

2. Project structure
- Create a main project folder.
```plaintext
weather_pipeline/
├── core/
│   ├── extract.py
│   ├── load.py
│   └── transform.py
├── docs/
│   └── readme.md
├── .env
├── .gitignore
└── requirements.txt
```

3. Environment & dependencies
- Create and active a Python virtual environment in project folder.
- Create a `requirements.txt` file and add the necessary libraries:
    - `python-dotenv`
    - `requests`
    - `pandas`
- Install them using `pip install -r requirements.txt`.

4. Configuration (`.env` file):
- In the `.env` file, store your secrets and configurations. **Never commit this file to Git**.

## Phase 1: E - Extract (`extract.py`)
- Connect to the OpenWeatherMap API and download the raw weather data for each city. Save this raw data without changing it.
- Logic:
    - Load configuration: Read the secrets from the `.env` file.
    - Prepare a place for raw data: Create a directory to store the output.
    - Loop & fetch:
        - Iterate through your list of cities.
        - For each city, construct the correct API URL. The OpenWeatherMap documentation will show you how.
        - Use the `requests` library to make a GET request to that URL.
    - Check for success: After making the request, check the HTTP status code. If it's `200 OK`, proceed. If not (e.g., `401 Unauthorized`, `404 Not Found`), should handle the error (printing a message, ...).
    - Save the raw data:
        - If the request was successful, get the content of the response, which will be a JSON text string.
        - Save this JSON string to a file.
        - **Important**: Name the file something unique and descriptive. This prevent overwriting data and makes it easy to trace back.
