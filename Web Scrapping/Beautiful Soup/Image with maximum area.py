"""
Problem statement
From this website :

Find and print the src of the <img> tag which occupies the maximum area on the page.

Note :

Ignore images which doesn't have height or width attributes

Output Format :
src_of_image
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## URL : https://en.wikipedia.org/wiki/Artificial_intelligence

## Print the required output in given format
# import the libraries
import requests
from bs4 import BeautifulSoup

# Get response from the url and create the soup
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.text)

# Find the master tag and all img elements
master_div = soup.find("div", {"id" : "bodyContent"})
img_el = master_div.find_all("img")

# To store the img src and the area of image
src_list = []
area_list = []
for el in img_el:

    # If height and width specified in the image element
    if el["height"] and el["width"]: 
        area = int(el["height"]) * int(el["width"]) # To find the area of image
        src = el["src"]
        src_list.append(src)
        area_list.append(area)
    else:
        continue

# To find the max value then according to value's index find the src
max_area_src = src_list[area_list.index(max(area_list))]
print(max_area_src)
