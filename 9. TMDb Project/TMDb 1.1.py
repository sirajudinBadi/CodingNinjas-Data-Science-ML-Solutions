"""
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


import requests
# Write your code here

# Stored bearer token, api key and url in the variable
bearer_token = <your_bearer_token>
api_key = <your_api_key_here>
url = f'https://api.themoviedb.org/3/search/movie?query=Andhadhun&api_key={api_key}'

# defined the headers
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# To get the response
response = requests.get(url, headers=headers)

# Accessed the id of the movie
print(response.json()["results"][0]["id"])
