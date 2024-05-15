"""
Problem statement
Using the result obtained in previous question, find out if James McAvoy was credited for his role in movie Deadpool 2. Print Yes or No.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# stored the bearer_token and person_id_url inside the variable
bearer_token = "BEARER TOKEN HERE"
james_id_url = "https://api.themoviedb.org/3/search/person?query=james%20mcavoy&include_adult=false&language=en-US&page=1"

# Defined the headers for authentication
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# To get James McAvoy Id
id_response = requests.get(james_id_url, headers=headers)
james_id = id_response.json() ["results"][0]["id"]


# To get James McAvoy Starrer movies through movie credits
james_movie_credit_response = f"https://api.themoviedb.org/3/person/{james_id}/movie_credits?language=en-US"
movie_credits_response = requests.get(james_movie_credit_response, headers=headers)
movie_response = movie_credits_response.json()["cast"][41]

# To check if James McAvoy was credited for Deadpool 2 or not
if movie_response["credit_id"]:
    print("Yes")
else:
    print("No")

