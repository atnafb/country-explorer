import requests
response = requests.get("https://countries.dev/countries", timeout=10) 
print(response.status_code) 