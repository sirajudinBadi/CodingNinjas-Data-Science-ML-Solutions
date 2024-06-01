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

Then rather than using SRS for extracting sample, create 5 different stratas based on 5 regions and then apply stratified sampling on these 5 stratas to extract a sample of size 100 startups (taking 20 values from each strata)

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

# get the sample of size 20 from each strata
sample_size = 20

bang_sample = bangalore_strata["AmountInUSD"].sample(sample_size, random_state = 1)
hyd_sample = hyderabad_strata["AmountInUSD"].sample(sample_size, random_state = 1)
mum_sample = mumbai_strata["AmountInUSD"].sample(sample_size, random_state = 1)
ncr_sample = ncr_strata["AmountInUSD"].sample(sample_size, random_state = 1)
pune_sample = pune_strata["AmountInUSD"].sample(sample_size, random_state = 1)

# For samples find the max amount
bang_sample_max = bang_sample.max()
hyd_sample_max = hyd_sample.max()
mum_sample_max = mum_sample.max()
ncr_sample_max = ncr_sample.max()
pune_sample_max = pune_sample.max()

# find the sampling error
bang_samp_err = bang_max - bang_sample_max
hyd_samp_err = hyd_max - hyd_sample_max
mum_samp_err = mum_max - mum_sample_max
ncr_samp_err = ncr_max - ncr_sample_max
pune_samp_err = pune_max - pune_sample_max

# Print the sampling error
print("Bangalore Sampling Error : ", bang_samp_err)
print("Hyderabad Sampling Error : ", hyd_samp_err)
print("Mumbai Sampling Error : ", mum_samp_err)
print("NCR Sampling Error : ", ncr_samp_err)
print("Pune Sampling Error : ", pune_samp_err)
