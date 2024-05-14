"""
Problem statement :

Fetch the company id company 'Marvel Studios' using TMDb. Print the id.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


import requests
# Write your code here

# stored the bearer token, api key and url inside the variables
bearer_token = "your bearer token"
api_key = "YOUR API KEY HERE"
url = f'https://api.themoviedb.org/3/search/company?query=Marvel Studios&api_key={api_key}'

# Defined the headers for authorization purpose
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# To send the request and get the response
response = requests.get(url, headers=headers)

# Filtered the query to get the company id
print(response.json()["results"][0]["id"])
    
