"""
Problem statement
Given File 'startup_funding.csv'

Find the top 5 startups who received the most number of funding rounds. That means, startups which got fundings maximum number of times.

Print the startup name in descending order with respect to the number of funding round as integer value.

Note:
Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. There are many errors in startup names, ignore correcting all, just handle important ones.

Output Format :
startup1 number1
startup2 number2
startup3 number3
. . . 
"""

# 🟡🔴🟡🔴🟡🔴🟡🔴https://www.linkedin.com/in/SirajudinBadi79🟡🔴🟡🔴🟡🔴🟡🔴
# 🟡🔴🟡🔴🟡🔴🟡🔴https://www.twitter.com/Sirajudin79🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡


# Open and read data file as specified in the question
# Print the required output in given format

# Import the libraries
import pandas as pd

#load csv file and drop the na entries from StartupName column
data = pd.read_csv("startup_funding.csv", encoding = "utf8")
df = data.copy()

df.dropna(subset = ["StartupName"], inplace = True)


# Check name error and correct it

df["StartupName"] = df.StartupName.replace("Flipkart.com", "Flipkart")
df["StartupName"] = df.StartupName.replace("Ola Cabs", "Ola")
df["StartupName"] = df.StartupName.replace("Olacabs", "Ola")
df["StartupName"] = df.StartupName.replace("Oyo Rooms", "Oyo")
df["StartupName"] = df.StartupName.replace("Oyorooms", "Oyo")
df["StartupName"] = df.StartupName.replace("OyoRooms", "Oyo")
df["StartupName"] = df.StartupName.replace("OYO Rooms", "Oyo")
df["StartupName"] = df.StartupName.replace("Paytm Marketplace", "Paytm")


#count the top five startup and their funding rounds and print the top five startup frequency
count = df.StartupName.value_counts()

startups = count.index
frequency = count.values
for i in range(5):
    print(startups[i], int(frequency[i]))


