"""
Problem statement
For this assignment, we'll be using "Amazon Job Dataset" which is collected by scraping https://amazon.jobs or can access the dataset from this link:

Amazon Job Dataset

Different fields of dataset and what they represent

Title : The title of the job
Location : Location of the job
Posting_date : Posting date of the job
Description: Overall description for the job
Basic Qualifications: Minimum Qualifications for the job
Preferred Qualifications: Preferred Qualifications for the job
By analysing this dataset, we can find out many interesting insights such as :
    - number of job openings in a specific location
"""
import csv

# File opened in dictionary format using "utf8" encoding
with open("amazon_job_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)

    #To store all locations in list
    location_opening = []
    for row in file_list:
        key = row["location"]
        location_opening.append(key)

    # Counted the frequency of location in list because location and job opening will be same.
    freq = {}
    for key in location_opening:
        freq[key] = freq.get(key, 0) + 1

    #Iterate through dictionary to print location and corresponding opening
    for key, value in freq.items():
        print(key, value)
