"""
Problem statement :
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
As we knew the Kargil ( in Jammu and Kashmir) War that took place between May 1999 and July 1999 (3 Months) ,so there was a huge conflict in Kashmir Valley during this period.

In this dataset, there is no information regarding the war between the two countries to find out the casualty during the war.

So find out the attack in this period in which maximum casualties happened.

Print the count of casualties (as integer), city in which that attack happened and name of attack group.

Note : Casualty = Killed + Wounded.Fill the empty value in killed or wounded feature to 0.

Output Format :
Casualty City TerroristGroup
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np 
import csv

# Opened a CSV file with utf8 encoding in dictreader format
with open("terrorismData.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    # To store corresponding values
    kill_list = []
    wounded_list = []
    city_list = []
    group_list = []

    # To iterate over row values
    for row in file_data:
        year_key = row["Year"]
        country_key = row["Country"].strip()
        state_key = row["State"].strip()
        month_key = row["Month"].strip()
        kill_key = row["Killed"].strip()
        wound_key = row["Wounded"].strip()
        city_key = row["City"].strip()
        group_key = row["Group"].strip()

        # To filter out the values based on the conditions
        if country_key == "India" and year_key == "1999" and state_key == "Jammu and Kashmir" and (month_key == '5' or month_key == '6' or month_key == '7') :
            kill_list.append(kill_key)
            wounded_list.append(wound_key)
            city_list.append(city_key)
            group_list.append(group_key)

    # Converted to NumPy array
    np_killed = np.array(kill_list)
    np_wounded = np.array(wounded_list)
    np_city = np.array(city_list)
    np_group = np.array(group_list)

    # Dealt with the empty values
    np_killed[np_killed == ''] = '0.0'
    np_wounded[np_wounded == ''] = '0.0'

    # Float conversion
    np_killed = np.array(np_killed, dtype = float)
    np_wounded = np.array(np_wounded, dtype = float)

    # Kill + wound in integer format
    np_casuality = np.array(np_killed + np_wounded, dtype = int)
    ind = np.argmax(np_casuality)

    # Printed the output in specified format.
    print(np_casuality[ind], np_city[ind], np_group[ind])
    
            
    
