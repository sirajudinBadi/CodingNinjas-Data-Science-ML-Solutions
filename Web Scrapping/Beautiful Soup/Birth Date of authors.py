"""
Problem statement
Find the birth date of authors whose name start with 'J' from this website

Note : Print a dictionary containing the name as key and the birth date as value.The Names of authors should be alphabetically sorted.

Output Format :
{'author_1': 'month day, year', 'author_2': 'month day, year', ....}
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

#import the libraries
import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com/"

# store url of all pages
all_pages_link = []
for i in range(1,11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    all_pages_link.append(url)

# get response from each page and store author detail page url for author name startswith "j"
j_named_link = set()
for page in all_pages_link:
    response = requests.get(page)
    soup = BeautifulSoup(response.text)

    # To get the master div
    master_div = soup.find_all("div", {"class" : "quote"})
    
    # if author_name starts with "J"
    for div in master_div:
        author_name = div.find("small")
        
        # Store the link of about for j named author in a set
        if author_name.text.lower().startswith("j"):
            a_el = div.find("a")["href"]
            j_named_link.add(base_url + a_el[1:])

# To store the name and Dob
di = {}
for author_detail in j_named_link:
    response_detail = requests.get(author_detail)
    soup_detail = BeautifulSoup(response_detail.text)

    # To get author detail div 
    detail_div = soup_detail.find("div", {"class" : "author-details"})
    author_name = detail_div.find("h3").text
    dob = detail_div.find("span", {"class" : "author-born-date"}).text
    di[author_name] = dob

sorted_dict = {key: value for key, value in sorted(di.items())}
print(sorted_dict)
