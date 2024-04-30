"""
Problem statement
Given File:

amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the Bar graph between Month vs Job Openings.

Print the month name and the number of job posting as integer value.

Order of months doesn't matter.

Output Format :
month_name1 job_posting1
month_name2 job_posting2
. . . 
. . .
. . .
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# Open and read data file as specified in the question
# Print the required output in given format

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv

#open csv 
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    #split months and store as key value pairs in dictionary by counting frequency
    dict_month = {}
    for row in file_data:
        key_split = row["Posting_date"].split()
        month = key_split[0]
        dict_month[month] = dict_month.get(month, 0) + 1
    

    # print all the key value pairs
    month = []
    count = []
    for key, value in dict_month.items():
        month.append(key)
        count.append(value)
        print(key, value)

    # Plot the bar graph
    plt.bar(month, count)
    plt.xlabel("Month")
    plt.ylabel("Job Posting Count")
    plt.title("Plot Month_Job")
    plt.xticks(rotation = 60)
    plt.show()
