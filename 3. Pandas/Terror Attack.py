"""
Problem statement
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Find out the Country with Highest Number of Terror Attack and in which year the most number of terrorist attack happened in that country ?

Print count of terror attacks as integer value.

Output Format :
Country NumberOfAttack Year
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import pandas as pd

terrorism = pd.read_csv("terrorismData.csv")

df = terrorism.copy()

country_max = df["Country"].value_counts()
country = country_max.index[0]

irq_sorted = df[df.Country == "Iraq"]
no_of_attacks = len(irq_sorted)

irq_sorted_year = irq_sorted["Year"].value_counts()
year = irq_sorted_year.index[0]

print(country, no_of_attacks, year)
