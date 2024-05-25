"""
Problem statement
Fetch the overview of the TV Show "FRIENDS" using TMDb API.

Output Format:
Print the Overview.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import requests
## Write your code here

# Stored the bearer token and tv details url inside the variable
bearer_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjE1YjkzMTcxMTMxODA5ZGZlMWRmNzA3MzJiYzIwNCIsInN1YiI6IjY2NDMzMTEyNGM3NTdiODUyYTc3ZjUzOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CawrFGCyFf-bgQXky5eCKLvu7KJxu8Muv5Pe4axPlOE"
tv_details_url = "https://api.themoviedb.org/3/search/tv?query=FRIENDS&include_adult=false&language=en-US&page=1"

# Defined the headers to authenticate
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

# Sent request to get the TV Series details
tv_details_response = requests.get(tv_details_url, headers=headers)
# print(tv_details_response.status_code)
# Querried for friends TV Series overview and printed.
friends_overview1 = tv_details_response.json()["results"][0]["overview"]
friends_overview2 = tv_details_response.json()["results"][1]["overview"]

print(friends_overview1.strip())
print(friends_overview2.strip())
