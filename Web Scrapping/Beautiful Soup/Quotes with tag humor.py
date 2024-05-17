"""
Find all the quotes that have the tag as "humor" from this website

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
# Import the libraries
import requests
from bs4 import BeautifulSoup

# Store all page links
all_pages_link = []
for i in range(1,11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    all_pages_link.append(url)

# Get response from each page
for page in all_pages_link:
    response = requests.get(page)
    soup = BeautifulSoup(response.text)
    
    # find master div for quote
    master_div = soup.find_all("div", {"class" : "quote"})
    
    # find master div and store quote in variable also find all a_elements of tag
    for div in master_div:
        tag_el = div.find_all("a", {"class" : "tag"})
        quote = div.find("span", {"class" : "text"}).text

        # To print the quote if the tag is humor
        for a_el in tag_el:
            if a_el.text.strip() == "humor":
                print(quote)                      
