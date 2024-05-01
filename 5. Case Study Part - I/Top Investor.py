"""
Problem statement
Given File 'startup_funding.csv'

Find the Investors who have invested maximum number of times.

Print the investor name and number of times invested as integer value.

Note:
In startup, multiple investors might have invested. So consider each investor for that startup.

Ignore the undisclosed investors.

Output Format :
investorname number
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://www.linkedin.com/in/SirajudinBadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://www.twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡

# Open and read data file as specified in the question
# Print the required output in given format

# import the library
import pandas as pd 

# Load csv file and drop na entries
data = pd.read_csv("startup_funding.csv", encoding = "utf8")

df = data.copy()
df.dropna(subset = ["InvestorsName"], inplace = True)

# To store each investor name
investors = []
for i in df.InvestorsName:
    i = str(i).strip()
    if i == "" or i == "Undisclosed investors" or i == "Undisclosed Investors": # negate the undisclosed or blank fields
        continue
    else:
        split = i.split(',')
        for i in split :
            investors.append(i)

# To store name and respected number of funding
di = {}
for i in investors:
    i = i.strip()
    if i ==  "":
        continue
    di[i] = di.get(i, 0) + 1

# To sort dictionary in descending order
descend_di = dict(sorted(di.items(), key = lambda item : item[1], reverse = True))

investor_name = []
no_of_investments = []
for key, value in descend_di.items():
    investor_name.append(key)
    no_of_investments.append(value)

# Print the first entry in both the lists.
print(investor_name[0], int(no_of_investments[0]))
    
