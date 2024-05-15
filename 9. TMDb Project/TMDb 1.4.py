"""
Problem statement : 
Fetch the names of top 5 similar movies to 'Inception' from the TMDb API.

Note
While fetching the movie id, use the "original_title" field not the "title". Because the "title" field may contain duplicate values.
Output Format:
Print the name of the movies in a new line.
movie_name_1
movie_name_2
and so on
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


import requests
# Write your code here

# Stored the bearer_token, api_key and url inside the variable
bearer_token = "your bearer here"
api_key = "YOUR KEY HERE"
url_id = f'https://api.themoviedb.org/3/search/movie?query=Inception&api_key={api_key}' # URL to get the Inception movie id


# Defined the header to get the authorization
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}


# To get the id of incption movie
id_response = requests.get(url_id, headers = headers)
inception_id = id_response.json()["results"][0]["id"]


# URL to get the similar movies
url_similar = f"https://api.themoviedb.org/3/movie/{inception_id}/similar?&page=1" 


# sent a request to get the response
response = requests.get(url_similar, headers=headers)

# Ran a loop to get the top 5 Inception like movies
for i in range(5):
    print(response.json()["results"][i]["title"])
