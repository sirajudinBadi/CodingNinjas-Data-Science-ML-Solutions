"""
Problem statement
Given File 'amazonjobsdataset.csv'

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Find the number of job openings in Canada?

Print the count as the Integer Value

Note: Here you should analyse the country code in location feature.( you can use dictionary for analyse part ). Output Format :
Count
"""
# www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

## Open and read data file as specified in the question
## Print the required output in given format
import csv

#Opened csv file using utf8 encoding in dictionary format.
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #Empty list to store canada based locations
    canada_list = []
    for row in file_list:
        key = row["location"].strip() # To remove extra spaces
        if key.startswith("CA"): # TO filter out locations based on countrycode
            canada_list.append(key)
    print(len(canada_list)) # Length of list will be number of openings in canada
