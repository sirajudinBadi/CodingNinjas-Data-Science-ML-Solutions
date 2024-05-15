"""
Problem statement
Fetch the Instagram and Twitter handle of Indian Actress "Alia Bhatt" from the TMDb API.

Output Format
Print the Instagram and Twitter IDs space separated.
instagram_id twitter_id
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# Stored person id url and bearer token inside the variable
id_url = "https://api.themoviedb.org/3/search/person?query=alia%20bhatt&include_adult=false&language=en-US&page=1"
bearer_token = "YOUR TOKEN HERE"

# Defined the headers for authentication
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# Requested to get person id
id_response = requests.get(id_url, headers=headers)
alia_id = id_response.json()["results"][0]["id"]

# To get the external IDs
social_med_url = f"https://api.themoviedb.org/3/person/{alia_id}/external_ids"
social_med_response = requests.get(social_med_url, headers=headers)

# Serched and stored instagram and twitter IDs
insta_id = social_med_response.json()["instagram_id"]
twitter_id = social_med_response.json()["twitter_id"]
print(f"{insta_id} {twitter_id}")
