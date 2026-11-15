import requests

API_URL = "https://countries.dev/countries"
def fetch_countries(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
def transform_countries(countries):
    transformed = []

    for country in countries:
        record = {
            "name": country.get("name", "Unknown"),
            "capital": country.get("capital", "Unknown"),
            "population": country.get("population", "Unknown"),
            "area": country.get("area", "Unknown"),

        }
        transformed.append(record)
    return transformed

try:
    countries = fetch_countries(API_URL)
    clean_countries = transform_countries(countries)
    print(f"Prepared {len(clean_countries)} countries for display.")
    if clean_countries:
        print(clean_countries[0])
    
except requests.exceptions.RequestException:
        print("Counld not load county data. Please try again later.")