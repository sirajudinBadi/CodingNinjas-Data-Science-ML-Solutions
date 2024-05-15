"""
Problem statement
Fetch the names of the character played by Tom Cruise in the movies:

Top Gun
Mission: Impossible - Fallout
Minority Report
Edge of Tomorrow
Output Format:
Print the names of the characters played by Tom Cruise line separated, in the respective order given in question.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# stored the bearer_token and person_id_url inside the variable
bearer_token = "YOUR TOKEN HERE"
tom_id_url = "https://api.themoviedb.org/3/search/person?query=tom%20cruise&include_adult=false&language=en-US&page=1"

# Defined the headers for authentication
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# To get Tom Cruise Id
id_response = requests.get(tom_id_url, headers=headers)
tom_id = id_response.json()["results"][0]["id"]

# To get Tom Cruise Starrer movies through movie credits
tom_movie_credits_url = f"https://api.themoviedb.org/3/person/{tom_id}/movie_credits?language=en-US"
movie_credits_response = requests.get(tom_movie_credits_url, headers=headers)
movie_response = movie_credits_response.json()["cast"]

# Stored the movie list asked in the problem statement
movie_list = ["Top Gun", "Mission: Impossible - Fallout", "Minority Report", "Edge of Tomorrow"]

# To get the Tom Cruise's character name from movie inside the movie_list
for i in movie_list:
    for movie in movie_response:
        if movie["original_title"] == i:
            print(movie["character"])
            break
