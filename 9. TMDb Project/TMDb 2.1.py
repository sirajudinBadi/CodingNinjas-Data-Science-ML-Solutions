"""
Problem statement
Find the name and birthplace of the present most popular person according to TMDb API.

Output Format:
id
name - birthplace
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# Stored the bearer token and the popular person url inside the variable
bearer_token = "YOUR BEARER HERE
id_url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

# Defined the header to get authorization
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# Sent the request to get the popular person's id
id_response = requests.get(id_url, headers=headers)
person_id = id_response.json()["results"][0]["id"]

# Based on the person Id requested name and place of birth
perosn_detail_url = f"https://api.themoviedb.org/3/person/{person_id}?language=en-US"
profile_response = requests.get(perosn_detail_url, headers=headers)

# Querried the name and birthplace
name = profile_response.json()["name"]
birthplace =  profile_response.json()["place_of_birth"]

# Printed the output
print(person_id)
print(name + " - " + birthplace)
