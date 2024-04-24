## Open and read data file as specified in the question
## Print the required output in given format
"""
Problem statement
Given File 'amazonjobsdataset.csv'

It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Find the month having most job openings in Year 2018 ?

Print the month (Month Name i.e January, February, March) and Number of job opening as Integer Value

Output Format :
MonthName Count

"""

# www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

import csv

#opened dataset file using utf8 encoding in DictReader format
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #stored every month entry in empty list
    monthly_list = []
    for row in file_list:
        key = row["Posting_date"].strip() # Removed extra spaces
        if key.endswith("2018"): # checked if listing is in 2018 or not
            monthly_list.append(key[:key.index(" ")]) # Sliced month name

    # To store month and corresponding listings on that month.
    month_freq = {} 
    for i in monthly_list:
        month_freq[i] = month_freq.get(i, 0) + 1

    # To find maximum count of listing
    max_val = 0
    for value in month_freq.values():
        value = int(value)
        if value > max_val:
            max_val = value
          
    # Based on max listing found corresponding month and printed the output in specified format. 
    for key, value in month_freq.items():
        value = int(value)
        if value == max_val:
            print(key, value)

