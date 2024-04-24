"""
Problem statement
Given File 'amazon_jobs_dataset.csv'

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Find the number of job openings are present if applicant have Bachelor degree?

Print the count as Integer value

Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not. Keywords that can be used are 'Bachelor', 'BS' and 'BA'. Output Format :
Count
"""

# www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import csv

# Opened csv file using utf8 encoding in dictionary format
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    # To store bachelor based job postings
    listing_with_bachelor = []
    for row in file_list:
        key = row["BASIC QUALIFICATIONS"].strip() # Selected the column
        if "Bachelor" in key or "BS" in key or "BA" in key: # Filtered out post using keywords
            listing_with_bachelor.append(key) #appended the final listing to list
    print(len(listing_with_bachelor)) # Length of list wiil be the count of jobs requiring bachelor degree.
