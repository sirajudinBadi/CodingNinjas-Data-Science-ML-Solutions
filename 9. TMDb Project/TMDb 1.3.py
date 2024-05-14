"""
Problem statement :
Find the vote count and vote average of the movie "3 Idiots" using the TMDb API

Output format: Vote Count , Vote Average
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


import requests
## Write your code here

# stored bearer_token, api_key and url in the variable
bearer_token = "YOUR BEARER TOKEN HERE"
api_key = "YOUR API KEY HERE"
url = f'https://api.themoviedb.org/3/search/movie?query=3 Idiots&api_key={api_key}'

# Defined the header to get the authorization
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# sent the request to get the response
response = requests.get(url, headers=headers)

# Printed the result to get the vote count and vote average
print(response.json()["results"][0]["vote_count"], end = " ")
print(response.json()["results"][0]["vote_average"])
    
