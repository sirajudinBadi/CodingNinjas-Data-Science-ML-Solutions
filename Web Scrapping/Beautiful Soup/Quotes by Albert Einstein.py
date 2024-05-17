"""
Problem statement
Find all the quotes by Albert Einstein(in the order they appear on the page) from this website

Note : Fetch data from all the pages.

Output Format :
quote1
quote2
quote3
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

# To iterate through every pages and if author is Einstein then print the quote
for page in all_pages_link:
    response = requests.get(page)
    soup = BeautifulSoup(response.text)

    # Found the master div of each quote
    div_el = soup.find_all("div", {"class" : "quote"})
    for div in div_el:
        author = div.find("small")
        if author.text == "Albert Einstein":
            quote = div.find("span")
            print(quote.text)
