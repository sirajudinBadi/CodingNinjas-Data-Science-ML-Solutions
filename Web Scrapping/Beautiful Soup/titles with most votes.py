"""
Problem statement
Link to use

Print the names of movies with highest number of votes from year 2010 to 2014

Note : Print the titles line wise starting from year 2010 Output Format :
title_name_1
title_name_2
title_name_3
.
.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

##'https://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt'

##headers: {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# import the libraries
import requests
from bs4 import BeautifulSoup
import json

# Url and headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
all_urls = [
    "https://www.imdb.com/search/title/?release_date=2010-01-01,2010-12-31&sort=num_votes,desc",
    "https://www.imdb.com/search/title/?release_date=2011-01-01,2011-12-31&sort=num_votes,desc",
    "https://www.imdb.com/search/title/?release_date=2012-01-01,2012-12-31&sort=num_votes,desc",
    "https://www.imdb.com/search/title/?release_date=2013-01-01,2013-12-31&sort=num_votes,desc",
    "https://www.imdb.com/search/title/?release_date=2014-01-01,2014-12-31&sort=num_votes,desc"
]

# To get each year response and created the soup
for year_url in all_urls:
    response = requests.get(year_url, headers = headers)
    soup = BeautifulSoup(response.text)

    # TO get the master tag
    master_ul = soup.find("ul", {"class" : "ipc-metadata-list ipc-metadata-list--dividers-between sc-748571c8-0 jmWPOZ detailed-list-view ipc-metadata-list--base"})
    li_els = master_ul.find_all("li", {"class" : "ipc-metadata-list-summary-item"})

    # TO get the title of each years highest voted movie/show
    for each in li_els[0]:
        title = each.find("h3")
        print(title.text[3:])
    
    
    
