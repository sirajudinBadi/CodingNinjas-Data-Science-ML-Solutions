"""
Problem statement
Download the file startup_funding

Problem Statement :
We want to find out the maximum amount of funding given to any startup in following regions -

Bangalore 
NCR (which includes New Delhi, Gurgaon and Noida)
Mumbai 
Pune 
Hydreabad 
So create your population data first by extracting those startups which are in given cities.

In the last question, we have used “Stratified Sampling” to sample our data. But you must have realized that our data is having different proportions of startups which are in given cities. So randomly selecting 20 values from each strata is not a good idea. Size of different stratas is quite different.

Ideally we should take number of samples from each stratum depending on their proportion in complete dataset.

So here we’ll apply “Proportional Stratified sampling”. To use this, first you need to calculate the number of data points that we need to take from each stratus and that can be calculated as -

(No_of_values_ith Strata / population_size ) * Sample_Size
Then take respective number of values from each strata based on its proportion (using SRS) and create your sample.

Find and print Sampling error.

Note:
Take city name "Delhi" as "New Delhi".

Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore"
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

# Load the libraries
import pandas as pd

# Load csv and copy
data = pd.read_csv("startups_funding.csv")
df = data.copy()

# Drop NaN
df.dropna(subset = ["CityLocation", "AmountInUSD"], inplace = True)

# Change the name and convert amount to integer format.
df["CityLocation"] = df["CityLocation"].replace({"bangalore" : "Bangalore", "Delhi" : "NCR", "Gurgaon" : "NCR", "New Delhi" : "NCR", "Noida" : "NCR"})
df["AmountInUSD"] = df["AmountInUSD"].str.replace(",", "")
df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"])

# Filter the rows based on the cities
all_city_filter = df[df["CityLocation"].isin(["Bangalore", "NCR", "Mumbai", "Pune", "Hyderabad"])]
population_size = len(all_city_filter)

# Create strata for each city and find max amount
bangalore_strata = all_city_filter[all_city_filter["CityLocation"].isin(["Bangalore"])]
hyderabad_strata = all_city_filter[all_city_filter["CityLocation"].isin(["Hyderabad"])]
mumbai_strata = all_city_filter[all_city_filter["CityLocation"].isin(["Mumbai"])]
ncr_strata = all_city_filter[all_city_filter["CityLocation"].isin(["NCR"])]
pune_strata = all_city_filter[all_city_filter["CityLocation"].isin(["Pune"])]

bang_max = bangalore_strata["AmountInUSD"].max()
hyd_max = hyderabad_strata["AmountInUSD"].max()
mum_max = mumbai_strata["AmountInUSD"].max()
ncr_max = ncr_strata["AmountInUSD"].max()
pune_max = pune_strata["AmountInUSD"].max()

# Getting the proportional sizes for each strata
strata_list = [bangalore_strata, hyderabad_strata, mumbai_strata, ncr_strata, pune_strata]
prop_samp_sizes_list = []
sample_size = 100
strata_max_list = []
for i in strata_list:
    prop_size = int((len(i) / population_size) * sample_size)
    prop_samp_sizes_list.append(prop_size)
    strata_max_list.append(i["AmountInUSD"].max())

# getting the sample from each strata
sample_list = []
for i in range(len(strata_list)):
    sample = list(strata_list[i]["AmountInUSD"].sample(prop_samp_sizes_list[i], random_state = 1))
    sample_list.append(sample)

# Finding the maximum for each strata
samp_max_list = []
for i in sample_list:
    samp_max_list.append(max(i))

# Counted the sampling error and stored in dictionary with its corresponding heading
samp_error_head = ["Bangalore Sampling Error is :", "Hyderabad Sampling Error is :", "Mumbai Sampling Error is :", "NCR Sampling Error is :", "Pune Sampling Error is :"]
samp_err_di = {}
for i in range(len(samp_max_list)):
    samp_err_di[samp_error_head[i]] = strata_max_list[i] - samp_max_list[i]

# To print the output
for key, value in samp_err_di.items():
    print(key, value)
