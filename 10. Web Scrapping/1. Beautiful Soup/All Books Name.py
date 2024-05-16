"""
Problem statement
Print the title of all books which are present on first 10 pages of this website.

Output Format :
 Book1 Name
 Book2 Name
 Book3 Name
 .
 .
 .
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


## Print the required output in given format
## You are given page links in variable allPages, use this

import requests
from bs4 import BeautifulSoup

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']

# To loop through each page
for page in allPages:

    # To get the response from the page link
    page_response = requests.get(page)
    page_soup = BeautifulSoup(page_response.text)

    #Found the corresponding li element and inside list found the name of the book and printed the same
    page_li_el = page_soup.find_all("li", {"class" : "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for book in page_li_el:
        print(book.img["alt"])
        
