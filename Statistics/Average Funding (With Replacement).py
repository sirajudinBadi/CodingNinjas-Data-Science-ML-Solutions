"""
Problem statement
Download the file startup_funding

Problem Statement :
We want to find out the average amount of funding given to startups which are in either Bangalore or in New Delhi.

For this - rather than considering all the startups, take a sample of size 75 (with replacement). Then find the average amount of funding from this sample and calculate the Sampling Error.

Sampling Error = Average(Population) - Average(Sample)
Note:
Take city name "Delhi" as "New Delhi".

Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore"

Output :
 Print Sampling Error
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

# Load the libraries
import pandas as pd

# loaded the csv file and copied dataframe
data = pd.read_csv("startups_funding.csv")
df = data.copy()

# dropped the NaN from CityLocation and AmountInUSD columns
df.dropna(subset = ["CityLocation", "AmountInUSD"], inplace = True)

# Changed Names as per the condition
df["CityLocation"] = df.CityLocation.replace("bangalore", "Bangalore")
df["CityLocation"] = df.CityLocation.replace("Delhi", "New Delhi")

# Replaced the commas in amount and converted to the integer
df["AmountInUSD"] = df.AmountInUSD.str.replace(",", "")
df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"])

# Filtered the rows having the value Bangalore or New Delhi and counted the average of amount i.e. parameter
filtered_data = df[df["CityLocation"].isin(["Bangalore", "New Delhi"])]
pop = filtered_data["AmountInUSD"]
pop_avg = pop.mean()

# Selected the random samples and counted its average that is Statistic
sample_size = 100
s1 = pop.sample(sample_size, random_state = 1, replace = True)
sample_avg = s1.mean()

# Calculated the sampling error and printed the same.
sampling_error = pop_avg - sample_avg
print(sampling_error)
