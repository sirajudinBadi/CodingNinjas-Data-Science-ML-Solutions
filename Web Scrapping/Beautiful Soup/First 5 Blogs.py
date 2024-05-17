"""
Problem statement
Link to use

Print the title of the first 5 blogs written by Coding Ninjas

Note : Print the blog names line wise Output Format :
blog_name_1
blog_name_2
blog_name_3
.
.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


## URL : https://medium.com/codingninjas-blog

## Print the required output in given format
import requests 
from bs4 import BeautifulSoup

# stored url and got response and stored in soup
url = "https://medium.com/codingninjas-blog"
response = requests.get(url)
soup = BeautifulSoup(response.text)

# To get the master div element for each post 
master_div = soup.find_all("div", {"class" : "postArticle postArticle--short is-withAccentColors"})

# Iterated through all master div and printed the text of h3 element.
for div in master_div[:5]:
    h3_el = div.find("h3")
    print(h3_el.text)
