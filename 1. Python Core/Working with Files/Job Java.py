"""
Problem statement
Given File 'amazonjobsdataset.csv'

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Find the country does Amazon need the most number of Java Developer?

Print the Country(Country Shortcut as given in Dataset) and number of job opening as integer value

Note :Here we will use the BASIC QUALIFICATIONS feature to find out whether Java is required for the job or not.Keyword is used is 'Java'.(Here case should not be changed).


Output Format :


Country NumberofJobs For example : US 40
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format


import csv

#Opened the csv file using utf8 encoding in dictionary format
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #TO store the listings in US with Java as a requirement.
    us_based_java_list = []

    for row in file_list:
        key = row['location'].strip()
        if "US" in key: # Filtered job posting in USA
            if "Java" in row["BASIC QUALIFICATIONS"]: # Filtered jobs with Java in USA
                us_based_java_list.append(row["BASIC QUALIFICATIONS"])

    # To store the java posting with Country as a key and frequency as a value.
    java_freq = {}
    for i in us_based_java_list:
        java_freq["US"] = java_freq.get("US", 0) + 1

    # Printed the output in specified format.
    for key, value in java_freq.items():
        print(key, value)

        
