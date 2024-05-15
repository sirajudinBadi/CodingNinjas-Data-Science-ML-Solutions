"""
Problem statement
Did James McAvoy play a role in the movie Deadpool 2. Print Yes or No.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here
# stored the bearer_token and person_id_url inside the variable
bearer_token = "YOUR BEARER HERE"
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
james_movie_credits_url = f"https://api.themoviedb.org/3/person/{james_id}/movie_credits?language=en-US"
movie_credits_response = requests.get(james_movie_credits_url, headers=headers)
movie_response = movie_credits_response.json()["cast"]

for i in movie_response:
    if i["original_title"] == "Deadpool 2":
        print("Yes")
