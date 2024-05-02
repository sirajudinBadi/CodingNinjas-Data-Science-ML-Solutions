"""
Problem statement :
Given File amazonjobsdataset.csv (Please check Dataset preview name)

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Find number of job openings in Bangalore,IN and in Seattle,US?

Print the Number of Job opening in Bangalore and Seattle as Integer value.

Output Format :
CountBangalore CountSeattle
"""

import csv

# Opened the csv file with utf8 encoding
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #appended the location with bangaluru or seattle only
    location_opening = []
    for row in file_list:
        key = row["location"].strip() # Notice every location has a space at the end.
        if key == "IN, KA, Bangalore" or key == "US, WA, Seattle":
            location_opening.append(key)

    #Stored the number of frequency of job opening in key value pairs
    freq = {}
    for key in location_opening:
        freq[key] = freq.get(key, 0) + 1

    print(freq["IN, KA, Bangalore"], end= ' ')
    print(freq["US, WA, Seattle"])
