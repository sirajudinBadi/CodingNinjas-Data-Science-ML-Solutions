"""
Problem statement
Given File 'startup_funding.csv'

Find out which cities are generally chosen for starting a startup.

Find top 10 Indian cities which have most number of startups ?

Plot a pie chart and visualise it.

Print the city name and number of startups in that city also.

Note :
Take city name "Delhi" as "New Delhi".

Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore".

For few startups multiple locations are given, one Indian and one Foreign. Count those startups in Indian startup also. Indian city name is first.

Print the city in descending order with respect to the number of startups.

Output Format :
city1 number1
city2 number2
. . . 
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# Open and read data file as specified in the question
# Print the required output in given format

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#read csv
df = pd.read_csv("startup_funding.csv", encoding = "utf8")

#Remove NaN
df["CityLocation"].dropna(inplace = True)

# seperate the city using split("/")
def f(s):
    splitted = s.split("/")
    return splitted[0].strip()

# apply name changes based on the conditions 
df["CityLocation"] = df.CityLocation.apply(f)
df["CityLocation"].replace("Delhi", "New Delhi", inplace = True)
df["CityLocation"].replace("bangalore", "Bangalore", inplace = True)

#count top 10 city and number of fundings
count = df["CityLocation"].value_counts()[:10]
city = count.index
no_of_count = count.values

# To print the output
for i in range(len(city)):
    print(city[i], no_of_count[i])

#plot a pie chart
plt.pie(no_of_count, labels = city)
plt.show()
