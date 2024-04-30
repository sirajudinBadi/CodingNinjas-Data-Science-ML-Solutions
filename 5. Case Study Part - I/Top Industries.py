"""

Problem statement
Given File 'startup_funding.csv'

Which type of companies got more easily funding. To answer this question, find -

Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)

Print the industry name and percentage of the amount funded with 2 decimal place after rounding off.

Note :
Ecommerce is the right word in IndustryVertical, so correct it.

Print the industry in descending order with respect to the percentage of the amount funded.

Output Format :
industry1 percent1
industry2 percent2
industry3 percent3
. . .

"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# Open and read data file as specified in the question
# Print the required output in given format

# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt 
import collections

# Load the csv file
data = pd.read_csv("startup_funding.csv", encoding = "utf8")
df = data.copy()

# Drop nan values
df.dropna(subset = ["IndustryVertical", "AmountInUSD"], inplace = True)

# Rename the ecommerce verticals
df["IndustryVertical"].replace("eCommerce", "Ecommerce", inplace = True)
df["IndustryVertical"].replace("ECommerce", "Ecommerce", inplace = True)
df["IndustryVertical"].replace("ecommerce", "Ecommerce", inplace = True)

# Function to change amount in integer form
def amount_sep(amt):
    amt = str(amt)
    new_amt = amt.replace(",", "")
    return int(new_amt)

# Applied the above function
df["AmountInUSD"] = df.AmountInUSD.apply(amount_sep)

# To store industry vertical and corresponding amount
di = {}

ind_vert_list = list(df.IndustryVertical)
amount_list = list(df.AmountInUSD)

for i in range(len(ind_vert_list)):
    di[ind_vert_list[i]] = di.get(ind_vert_list[i], 0) + int(amount_list[i])

di_sorted = dict(sorted(di.items(), key=lambda item: item[1])) # Sorted dict to reverse
reversed_dict = collections.OrderedDict(reversed(list(di_sorted.items()))) # Reversed to get descending order
# print(reversed_dict)

industries = []
amount = []
for key, value in reversed_dict.items():
    industries.append(key)
    amount.append(value)

# To get the top 5 Industries only
five_ind = list(industries[:5])
five_amt = list(amount[:5])

total_five = sum(five_amt) # Total amount of top 5 industries

percentage = [] # To store the percentage of each top 5 industrie investment
for i in five_amt:
    pct = (i / total_five) * 100
    percentage.append(round(pct, 2))

for i in range(5):
    print(five_ind[i], percentage[i])




