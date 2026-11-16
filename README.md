# Country Explorer

## API Exploration 
The API Returns a list of dictionaries, with each dictionary representing a country. 
Fielsds include name, capital, region, population and area. 
some values are nested: maps is a dictionary, and languages is a list. 

In the response I checked:
- name: 0 missing keys, 0 null values
- capital: 5 missing keys, 0 null values
- population: 0 missing keys, 0 null values
- area: 10 missing keys, 0 null values

## Project Plan 

My command-line tool will ask the user for a country name and
look up that country using the countries.dev API. It will display
the country's name, capital, population, and area with clear labels.
The search will ignore capitalization and surrounding spaces.
Missing details will display as "Unknown". Empty input, no matching
country, and network errors will produce helpful messages.
Fetching, transforming, searching, and displaying data will each
have a separate function.
## Setup and Run

Requires Python 3 and an internet connection.

### 1. Clone the project branch

```bash
git clone --branch country-explorer https://github.com/atnafb/country-explorer.git
cd country-explorer
```

### 2. Create and activate a virtual environment (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the program

```bash
python main.py
```

Enter a full country name, such as Ethiopia. Capitalization and
surrounding spaces do not affect the search.

The program displays the country's name, capital, population,
and area. Missing fields display as "Unknown".

Blank input, an unmatched country name, or a failed API request
produces a helpful message.

## API Used

https://countries.dev/countries