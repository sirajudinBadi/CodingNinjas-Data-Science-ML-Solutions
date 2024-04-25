"""
Problem statement :
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. 
This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Find value of killed column only where country == ‘United States’?

Print 0 in place of missing values.

Print count of Killed as integer value.

Output Format :
Killed1
Killed2
Killed3
Killed4
. . .
. . .
. . .
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import numpy as np 
import csv

# Opened CSV file using utf8 encoding in dictionary format
with open("terrorismData.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    # To store all kill values including empty values of US
    killed = []
    for row in file_data:
        key = row["Country"].strip()
        if key == "United States": # Filtered US entries
            killed.append(row["Killed"])
    
    np_killed = np.array(killed) # Converted to numpy array
    np_killed[np_killed == ''] = '0.0' # Assigned '0.0' to empty values
    
    np_killed = np.array(np_killed, dtype = float) # Converted string into float
    
    # To meet the condition of output
    for i in np_killed: 
        print(int(i))
