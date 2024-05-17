"""
Problem statement
From this link,

Your task it to fetch the content from the table under the section "Land borders of India". In this you need to fetch all the columns and put them to the final dataframe in such a manner that following columns are present:

Columns Names : ['Land Border Country', 'Dispute', 'LengthKM', 'LengthMiles']

Note:

1. Land Border Country: This can directly be fetched from the original table (Only fetch the name not the image.)

2. Dispute: This can directly be fetched from the original table

3. LengthKM: Need to fetch only kilometer from the columnname "Length (Km) and (mi)"

4. LengthMiles: Need to fetch only miles(mi) from the columnname "Length (Km) and (mi)"

Ouput
 Land Border Country  Dispute  Length_KM  Length_Miles
0   Bangladesh           N       4096         2545
1     Bhutan             N       578          359
2     China              Y       3488         2167
3     Myanmar            N       1643         1021
4     Nepal              Y       1752         1089
5    Pakistan            Y       3310         2060
6   Afghanistan          Y       106           66
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

# Imported the necessary Libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Stored the URL and got the response from url
url = "https://en.wikipedia.org/wiki/Borders_of_India"
response = requests.get(url)

# Created soup format
soup = BeautifulSoup(response.text)

# Searched the table data and table rows inside it
table_data = soup.find("table")
tr_els = table_data.find_all("tr")

# To store each row data
all_row_list = []

# Iterated through every tr element
for tr in tr_els[1:]:
    row_data = [] # to store current row data

    # Searched every table data element to get actual data
    td_els = tr.find_all("td")
    
    count = 0 # To negate the last two columns

    # To get td text
    for td in td_els:
        if count < 3: # To make km and miles column the last column
            
            # To separate the km and miles column
            if count == 2: 
                km = int(td.text.replace(",", "")[:4].strip()) # To get the km from the string 
                ind_start = td.text.replace(",", "").index("(") + 1 # To get the index of paranthesis + 1 which will be start point of mile count
                ind_end = td.text.replace(",", "").rindex("m") - 1 # To get the index of last "m" character + 1 which will be end point of mile count
                miles = int(td.text.replace(",", "")[ind_start : ind_end]) # To get the mile count

                # Appended to current row data list for km and mile column
                row_data.append(km) 
                row_data.append(miles)
                break
                
            # Appended to current row data list for country name and dispute column
            row_data.append(td.text.strip())
            count += 1
        else: 
            break # If the column data of comment column
    all_row_list.append(row_data)

# COnverted to pandas dataframe
df = pd.DataFrame(all_row_list, columns = ["Land Border Country", "Dispute", "Length_KM", "Length_Miles"])
print(df)

