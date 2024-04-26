"""
Problem statement :
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Find the casualty in the Red Corridor States ? Mainly Red corridor states include Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh.

Note: Casualty=Killed +Wounded

Print count of Casualty as integer value.

Output Format :
Count
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import csv
import numpy as np 

# Opened CSV file in dictionary format using utf8 encoding
with open("terrorismData.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    # TO store kill and wounded count
    killed_list = []
    wounded_list = []

    # TO fill kill and wounded list
    for row in file_data:
        state_key = row["State"].strip()
        kill_key = row["Killed"].strip()
        wound_key = row["Wounded"].strip()

        # Filtered out the entries to meet the conditions
        if state_key == "Jharkhand" or state_key == "Odisha" or state_key == "Andhra Pradesh" or state_key == "Chhattisgarh":
            killed_list.append(kill_key)
            wounded_list.append(wound_key)

    # Converted to NumPy array
    np_killed = np.array(killed_list)
    np_wounded = np.array(wounded_list)

    # Dealt with the empty values
    np_killed[np_killed == ''] = '0.0'
    np_wounded[np_wounded == ''] = '0.0'

    # Converted to float
    np_killed = np.array(np_killed, dtype = float)
    np_wounded = np.array(np_wounded, dtype = float)

    # To count the casualties and Integer conversion and later printed the sum of casualty
    np_casualty = np.array(np_killed + np_wounded, dtype=int)
    print(np.sum(np_casualty))





