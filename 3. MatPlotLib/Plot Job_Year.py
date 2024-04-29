"""
Problem statement
Given File:

amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the line graph between no. of Job postings with respect to year.

Print the year and the number of job posting as integer value.

Note: Year should be in ascending order.

Output Format :
year1   job_posting1
year2   job_posting2
. . . 
. . .
. . .

"""

# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import matplotlib.pyplot as plt 
import csv
from collections import OrderedDict


# Opened the csv file and converted in dictionary format with encoding
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    # To store the year and corresponding job posting count
    dict = {}
    for row in file_data:
        date = row["Posting_date"].split() # splitted to get the year only
        key = date[2]

        dict[key] = dict.get(key, 0) + 1 # Counted the frequency of the job posting
    
    reversed_dict = OrderedDict(reversed(list(dict.items()))) # Reversed the dictionary to print in the ascending order.
    
    year_list = [] # To append the year 
    count_list = [] # To append the number of job openings in that year

    # Appended the year and corresponding job count and also printed the output in specified format.
    for key, value in reversed_dict.items():
        year_list.append(key)
        count_list.append(value)
        print(int(key), int(value))

    # Applied the line graph on the derived data.
    plt.plot(year_list, count_list)
    plt.show()

    
