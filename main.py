import requests

API_URL = "https://countries.dev/countries"
def fetch_countries(url):
    response = requests.get(url, timeout=10)
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
def find_country(countries, country_name):
    search_name = country_name.strip().lower()
    for country in countries:
        if country.get("name", "Unknown").strip().lower() == search_name:
            return country
    return None
def display_country(country):
    print("\nCountry Information:")
    print("--------------------")
    print(f"Name: {country['name']}")
    print(f"Capital: {country['capital']}")
    print(f"Population: {country['population']}")
    print(f"Area: {country['area']}")
try:
    countries = fetch_countries(API_URL)
    clean_countries = transform_countries(countries)

    country_name = input("Enter the name of the country you want to search for: ").strip()

    if not country_name:
        print("No country name provided. Exiting.")
    else:
        result = find_country(clean_countries, country_name)
        if result is None:
            print(f"Country '{country_name}' not found.")
        else:
            display_country(result)
    
except requests.exceptions.RequestException:
        print("Could not load country data. Please try again later.")