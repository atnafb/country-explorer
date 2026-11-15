import requests

API_URL = "https://countries.dev/countries"
def fetch_countries(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status() 
    return response.json()
try:
    countries = fetch_countries(API_URL)
    print(f"Fetched {len(countries)} countries.")
except requests.exceptions.RequestException:
        print("Counld not load county data. Please try again later.")