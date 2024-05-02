"""
Problem statement
Given File 'amazonjobsdataset.csv'

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Among Java, C++ and Python, which of the language has more job openings in India for Bachelor Degree Holder?

Print the Language(i.e Java,C++,Python) and number of job opening as integer value.

Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not. Keywords that can be used are 'Bachelor', 'BS' and 'BA' and we will use the BASIC QUALIFICATIONS feature to find out whether Language is required for the job or not.Keywords that is used for language searching are 'Java','C++' or 'Python'.(There case should not be changed). Output Format :
Language Count
"""
# www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

## Open and read data file as specified in the question
## Print the required output in given format

import csv

#Opened the csv file using utf8 encoding in dictionary format
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #Created the list of languages for which we need to find the popularity
    langs = ["Java", "C++", "Python"]

    # To store all the job listing in India
    india_jobs = []  
    for row in file_list:
        key = row["location"].strip() # Removed extra space
        if key.startswith("IN"): # To filter job listings in India
            if "Bachelor" in row["BASIC QUALIFICATIONS"] or "BS" in row["BASIC QUALIFICATIONS"] or "BA" in row["BASIC QUALIFICATIONS"]: # To filter jobs that require Bachelor's Degree atleast.
                india_jobs.append(row["BASIC QUALIFICATIONS"])

    # To store the language as a key and listing count as a value
    lang_freq = {}
    for lang in langs:
        for job in india_jobs:
            if lang in job:
                lang_freq[lang] = lang_freq.get(lang,0) + 1

    # To get the highest postings of particular lang
    max_val = 0
    for value in lang_freq.values():
        value = int(value)
        if value > max_val:
            max_val = value
          
    # To print the output in specified format
    for key, value in lang_freq.items():
        if value == max_val:
            print(key, int(value))
