import os
import json
import requests
import datetime
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv('/opt/airflow/.env')

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Ensure the directory exists before saving
os.makedirs("data/bronze", exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data/bronze/jobs_raw_{timestamp}.json"

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "data analyst",
    "results_per_page": 50
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved raw data to {filename}")
else:
    print("Error details:", response.text)