"""
Problem statement
Use case: In the age of information, accessing data about different countries can be crucial for travelers, researchers, and many other professionals. While there are many APIs available to fetch this data, they come with certain limitations, like rate limits, which can restrict the number of requests one can make in a given period.

Exercise: Your goal is to write a Python script that fetches data for a list of countries from the REST Countries API. However, you need to ensure that your script respects the rate limits of the API and can handle situations where it reaches the rate limit.

Your script should fetch country data for the following countries: USA, Canada, Mexico, Germany, France, India, China, Japan, Australia, New Zealand, Russia, Brazil, South Africa, Egypt, Kenya, Argentina, Chile, Spain, Italy, and Portugal.

Use the REST Countries API (https://restcountries.com/v3.1/name/) to fetch the data.

If your script encounters a rate limit (usually indicated by a 429 HTTP status code), it should wait for a reasonable amount of time (e.g., 60 seconds) and then retry the request. Introduce a small delay between consecutive requests to minimize the risk of hitting the rate limit. If data is successfully fetched for a country, print the data.


Sample Output
{'common': 'United States', 'official': 'United States of America', 'nativeName': {'eng': {'official': 'United States of America', 'common': 'United States'}}}
{'common': 'Canada', 'official': 'Canada', 'nativeName': {'eng': {'official': 'Canada', 'common': 'Canada'}, 'fra': {'official': 'Canada', 'common': 'Canada'}}}
{'common': 'Mexico', 'official': 'United Mexican States', 'nativeName': {'spa': {'official': 'Estados Unidos Mexicanos', 'common': 'México'}}}
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
import time

BASE_URL = "https://restcountries.com/v3.1/name/"  # URL endpoint for REST Countries API

def fetch_country_data(country_name):
    # Your code goes here
    # Created the empty list to store the each country url
    url_list = [] 
    for country in countries:
        if country in country_name:
            url_list.append(BASE_URL + country)
        else:
            continue
          
    # To fetch the data using country name parameter
    for i in url_list:
        response = requests.get(i)

        # If the request is within the rate limit
        if response.status_code == 200: 
            print(response.json()[0]["name"])

        # If rate limit exceeded
        elif response.status_code == 429:
            time.sleep(61) # Waited for a minute to get rate limit renewed
            response = requests.get(i)
            print(response.json()[0]["name"])
        
        else:
            return 0

        
    """
    Fetches country data from the REST Countries API.

    :param country_name: Name of the country to search.
    :return: JSON response from the API or None if any issues.
    """



countries = [
    'USA', 'Canada', 'Mexico', 'Germany', 'France', 
    'India', 'China', 'Japan', 'Australia', 'New Zealand', 
    'Russia', 'Brazil', 'South Africa', 'Egypt', 'Kenya', 
    'Argentina', 'Chile', 'Spain', 'Italy', 'Portugal'
] 

for country in countries:
    data = fetch_country_data(country)
    if data:
        print(data[0]["name"])
