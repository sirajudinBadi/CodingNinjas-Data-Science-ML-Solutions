"""
Problem statement
Fetch the top rated english movies in the US region using the TMDb API. From the result, print the first 10 movies which have original language as english. Also print their genres.

Note: Do not use the search/movies API for finding genres.

Output Format:
movie_name_1 - genre_1, genre_2 ....
and so on..
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# Stored the bearer token inside the variable 
bearer_token = "YOUR BEARER TOKEN HERE"

# Url to find top rated movies in english language and US region.
top_rated_url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

# Defined the headers to get the authorization.
headers = {
    "accept": "application/json",
    "Authorization" : f"Bearer {bearer_token}"
}

# Requested to get the top rated movie response
response = requests.get(top_rated_url, headers=headers)
movie_list = response.json()["results"]

# To get the genre id and genre name
genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
response_for_genre = requests.get(genre_url, headers=headers)
genre_response = response_for_genre.json()["genres"]

# TO store the genre id as key and genre name as value
di = {}
for i in range(len(genre_response)):
    di[genre_response[i]["id"]] = genre_response[i]["name"]

# To print the movie name, genre1, genre2...
count = 0
for i in range(len(movie_list)):
    if count < 10:
        if movie_list[i]["original_language"] == "en":
        
            print(movie_list[i]["title"], end= " - ")
            for j in movie_list[i]["genre_ids"]:
                print(di[j], end=', ')
            count += 1
            print()
