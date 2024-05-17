"""
Problem statement
From this link, your task is to retrieve the dropdown data from the 'Resources' category, and inside it, there is another dropdown for 'What is open source?' and 'Open source alternatives' Fetch this data as well. Ensure that you fetch data for all dropdowns within the 'Resources' category.

Output Format:
Resources
What is open source?
The open source way
Projects and applications
Organizations
Open source alternatives
Alternatives to Acrobat
.
.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


#url = "https://opensource.com/resources"

# Imported the libraries
import requests
from bs4 import BeautifulSoup as bs

# Stored the url and requested the response
url = "https://opensource.com/resources"
response = requests.get(url)

# converted to BS format
main_page_soup = bs(response.text)

# To get the parent tag of resources dropdown
parent_tag = main_page_soup.find("li", {"class" : "main__item main__item--active-trail is-expanded"})
all_text = parent_tag.text.replace("\n", " ").strip() # Replace unnecessary text
li = all_text.split("  ") # Converted to list

# Looped through list to print and negate the empty space
for i in li:
    i = i.strip()
    if i == "":
        continue
    else:
        print(i)
