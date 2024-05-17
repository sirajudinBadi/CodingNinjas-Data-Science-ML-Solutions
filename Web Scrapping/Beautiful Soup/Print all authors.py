"""
Problem statement
Find and print the names of all the different authors from all pages of this website

Note : Print the names of all authors line wise sorted in dictionary order

Output Format :
author1
author2
author3
.
.
.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## URL : http://quotes.toscrape.com/

## Print the required output in given format
# Imported the libraries
import requests
from bs4 import BeautifulSoup

# TO store every page links
all_pages_link = []
for i in range(1,11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    all_pages_link.append(url)

# To iterate through every pages
author_list = []
for page in all_pages_link:
    response = requests.get(page)
    soup = BeautifulSoup(response.text)

    # Found the master div of each quote
    div_el = soup.find_all("div", {"class" : "quote"})
    for div in div_el:
        author = div.find("small")
        author_list.append(author.text)

# TO remove duplicates       
list = set(author_list)

# Sorted in dictionary order
sorted_list = sorted(list)

# Printed the name
for i in sorted_list:
    print(i)
