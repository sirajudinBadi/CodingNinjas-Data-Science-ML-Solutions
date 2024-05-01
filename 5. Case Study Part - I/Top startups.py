"""
Problem statement
Given File 'startup_funding.csv'

Find top 5 startups with most amount of total funding.

Print the startup name in descending order with respect to amount of funding.

Note:
Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. There are many errors in startup names, ignore correcting all, just handle important ones.

Output Format :
startup1
startup2
startup3
...
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# Open and read data file as specified in the question
# Print the required output in given format

# import the libraries
import pandas as pd
from collections import OrderedDict 

# load the csv file and drop the nan entries from the startup and amount column
data = pd.read_csv("startup_funding.csv", encoding = "utf8")
df = data.copy()

df.dropna(subset = ["StartupName", "AmountInUSD"], inplace = True)

# Find duplicate names and modify the startup names
df["StartupName"] = df.StartupName.replace("Flipkart.com", "Flipkart")
df["StartupName"] = df.StartupName.replace("Ola Cabs", "Ola")
df["StartupName"] = df.StartupName.replace("Olacabs", "Ola")
df["StartupName"] = df.StartupName.replace("Oyo Rooms", "Oyo")
df["StartupName"] = df.StartupName.replace("Oyorooms", "Oyo")
df["StartupName"] = df.StartupName.replace("OyoRooms", "Oyo")
df["StartupName"] = df.StartupName.replace("OYO Rooms", "Oyo")
df["StartupName"] = df.StartupName.replace("Paytm Marketplace", "Paytm")


# Remove commas from the amount and apply the function to AmountInUSD column
def amt_int(amt):
    amt = str(amt).strip()
    split = amt.replace(",", "")
    return split

df["AmountInUSD"] = df["AmountInUSD"].apply(amt_int)

# Club the startup names and corresponding amount in the dictionary
di = {}
startups = list(df.StartupName)
amount = list(df.AmountInUSD)

for i in range(len(startups)):
    di[startups[i]] = di.get(startups[i], 0) + int(amount[i]) # To get the startup name and total funding 


# sort and reversed the dictionary to get the startups with the highest amount of funding 
reversed_dict = dict(sorted(di.items(), key=lambda item: item[1], reverse=True))

# store the top five startup in the seperate list 
top_five = []
for key in reversed_dict.keys():
    top_five.append(key)

# print the output in the descending order
for i in range(5):
    print(top_five[i])
