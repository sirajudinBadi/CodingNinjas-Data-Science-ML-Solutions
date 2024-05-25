"""
Problem statement
Fetch the name and air date of S06E05 of the TV Show 'The Big Bang Theory' from TMDb API.

Output Format:
episode_name - air_date
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# Stored the bearer token and url to find Big Bang theory id
bearer = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjE1YjkzMTcxMTMxODA5ZGZlMWRmNzA3MzJiYzIwNCIsInN1YiI6IjY2NDMzMTEyNGM3NTdiODUyYTc3ZjUzOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CawrFGCyFf-bgQXky5eCKLvu7KJxu8Muv5Pe4axPlOE"
tbbt_url = "https://api.themoviedb.org/3/search/tv?query=the%20big%20bang%20theory&include_adult=false&language=en-US&page=1"

# Header to authenticate using bearer token
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer}"
}

# To get the ID of Big Bang Theory
tbbt_response = requests.get(tbbt_url, headers=headers)
tbbt_id = tbbt_response.json()["results"][0]["id"]

# To get the Season 6 Episode 5 details
tbbt_s6e5_url = "https://api.themoviedb.org/3/tv/1418/season/6/episode/5?language=en-US"
tbbt_s6e5_response = requests.get(tbbt_s6e5_url, headers=headers)

# To get Season 6 Episode 5 name and airing date
tbbt_s6e5_name = tbbt_s6e5_response.json()["name"]
tbbt_s6e5_date = tbbt_s6e5_response.json()["air_date"]

# Printed the output
print(f"{tbbt_s6e5_name} - {tbbt_s6e5_date}")
