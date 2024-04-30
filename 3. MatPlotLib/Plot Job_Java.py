"""
Problem statement
Given File:

amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the scatter graph between year vs No. of jobs opening related to Java.

Print the year and number of Jobs opening in Java Profile.

Note: Use the Keyword 'Java' or 'java' in Basic Qualification feature for finding the job opening related to Java Profile. Print the year in ascending order.

Output Format :
year1 JobOpening1
year2 JobOpening2
. . . 
. . .
. . .
"""


# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

# Open and read data file as specified in the question
# Print the required output in given format

#import the libraries
import matplotlib.pyplot as plt 
import csv
from collections import OrderedDict

#open the csv and read
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)

    #split the year and filter java jobs and store as key-value pairs in dictionary
    di = {}
    for row in file_data:
        year = row["Posting_date"].split()[2]
    
        if "Java" in row["BASIC QUALIFICATIONS"] or "java" in row["BASIC QUALIFICATIONS"]:
            di[year] = di.get(year, 0) + 1
    # print(di)

    #reverse the dictionary

    reversed_dict = OrderedDict(reversed(list(di.items())))

    # Print the output and store years and count in list for scatter plot
    years = []
    count = []
    for key, value in reversed_dict.items():
        years.append(key)
        count.append(value)
        print(key, value)

    #plot the scatter graph
    plt.scatter(years, count)
    plt.show()


