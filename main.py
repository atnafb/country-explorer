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
def main():
    country_name = input("Enter a country name: ").strip()

    if not country_name:
        print("Please enter a country name.")
        return

    try:
        countries = fetch_countries(API_URL)
    except requests.exceptions.RequestException:
        print("Could not load country data. Please try again later.")
        return

    clean_countries = transform_countries(countries)
    result = find_country(clean_countries, country_name)

    if result is None:
        print(f"Country '{country_name}' not found.")
    else:
        display_country(result)


if __name__ == "__main__":
    main()