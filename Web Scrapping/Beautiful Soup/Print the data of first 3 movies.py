"""
Problem statement
From this link,

Find and print the name of the first 3 titles

Output Format :
title_name_1 
title_name_2 
title_name_3
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

##url : 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# Import the libraries
import requests
from bs4 import BeautifulSoup

# Get response from the url and created the soup.
url = "https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc"
response = requests.get(url, headers = headers)
# response.status_code
soup = BeautifulSoup(response.text)

# To get the master element and all movie_block element
master_div = soup.find("ul", {"class" : "ipc-metadata-list ipc-metadata-list--dividers-between sc-748571c8-0 jmWPOZ detailed-list-view ipc-metadata-list--base"})
li_el = master_div.find_all("li", {"class" : "ipc-metadata-list-summary-item"})

# To get each movie title
for movie_name in li_el[:3]:
    title = movie_name.find("h3", {"class" : "ipc-title__text"}).text
    print(title[3:])
