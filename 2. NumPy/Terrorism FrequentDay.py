"""
Problem statement :
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Find the most frequent day of attack in a terrorismDataset ?

Note: Here np.unique can be used.

Print count of frequent day and number of attack as Integer value.

Output Format :
Day NumberOFAttack
"""

# 👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

## Open and read data file as specified in the question
## Print the required output in given format

import csv
import numpy as np

# Opened CSV file in dictionary format using UTF8 encoding
with open("terrorismData.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    # TO store all day value
    day_list = []
    for row in file_data:
        day_key = row["Day"]
        day_list.append(float(day_key))

    # To store unique day and corresponding frequency  
    dict = {}
    for i in day_list:
        i = int(i)
        dict[i] = dict.get(i, 0) + 1

    # To find which day has the highest frequency
    max_val = 0
    for value in dict.values():
        if value > max_val:
            max_val = value

    # TO find corresponding key to most frequent day
    for key, value in dict.items():
        if value == max_val:
            print(key, value)
