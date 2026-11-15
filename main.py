import requests
response = requests.get("https://countries.dev/countries", timeout=10) 
print(response.status_code) 
data = response.json()
print(type(data))
print(data[0]) # see the first record from the coutry list
#print(data.keys())
print (data[0].keys()) # see the keys of the first record
print(data[0]['name']) # see the name of the first country
print(data[0]['population']) # see the cappopulation of the first country 

## Check for four fields accross all countries and counts missing keys and null values 
fields = ['name', 'capital', 'population', 'area']
for field in fields:
    missing_count = 0
    null_count = 0
    for country in data:
        if field not in country:
            missing_count += 1
        elif country[field] is None:
            null_count += 1
    print(f"Field '{field}': Missing keys: {missing_count}, Null values: {null_count}")