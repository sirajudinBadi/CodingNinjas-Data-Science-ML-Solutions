"""
Problem statement
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
There was formation of new government in India on 26 May 2014. So current government's span is from 26th May 2014 to current. Find out two things from this period-

1. Total number of attacks done in this period in India. Find this count as integer.
2. Which Terrorist group was most active in this period in India. Most active means, group which has done maximum number of attacks. 
3.Ignore the Unknown group. 
Output Format :
TotalAttacks MostActiveTerroristGroup
## Open and read data file as specified in the question
## Print the required output in given format

import pandas as pd 

terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()

# Sorted from 26 May, 2014 to 31 May, 2014
may_sorted = df[(df.Country == "India") & (df.Year == 2014) & (df.Month == 5) & (df.Day >= 26)]
…
# To sort unknowns
known_sorted = unknown_concat[unknown_concat.Group != "Unknown"]

# To get most active group
notorious_group = known_sorted["Group"].value_counts().index[0]
print(total_count, notorious_group)

"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import pandas as pd 

terrorism = pd.read_csv("terrorismData.csv")
df = terrorism.copy()

# Sorted from 26 May, 2014 to 31 May, 2014
may_sorted = df[(df.Country == "India") & (df.Year == 2014) & (df.Month == 5) & (df.Day >= 26)]

# 1 June, 2014 to 31 Dec, 2014 sorted
rest_2014_sorted = df[(df.Country == "India") & (df.Year == 2014) & (df.Month > 5)]

# Sorted 2015 onwards
rest_all_sorted = df[(df.Country == "India") & (df.Year > 2014)]

# Total attacks including unknown group too
unknown_concat = pd.concat([may_sorted, rest_2014_sorted, rest_all_sorted], axis = 0)
total_count = len(unknown_concat)

# To sort unknowns
known_sorted = unknown_concat[unknown_concat.Group != "Unknown"]

# To get most active group
notorious_group = known_sorted["Group"].value_counts().index[0]
print(total_count, notorious_group)
