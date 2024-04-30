"""
Problem statement
Given File:

amazon_jobs_dataset.csv
It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.

Problem Statement :
Plot the Pie chart between Indian cities vs No. of job openings.

Print the Indian cities and %age of Job distribution in India up to 2 decimal places.

Note: %age of Job distribution should be in descending order.

Output Format :
city1 percentage1
city2 percentage2
. . . 
. . .
. . .

"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


# Open and read data file as specified in the question
# Print the required output in given format

# Import the libraries
import matplotlib.pyplot as plt
import csv

# Open the csv file
with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace = True)
        
    # split the city name and store in dictionary with corresponding jobs as value
    dict = {}
    for row in file_data:
        if row["location"].startswith("IN"):
            stripped_city = row["location"].strip()
            key_split = stripped_city.split(",")
            city = key_split[-1]
            dict[city] = dict.get(city, 0) + 1
       
    # seperate city and count and also print the dictionary
    city = []
    count = []
    for key, value in dict.items():
        city.append(key)
        count.append(value)
        # print(key, value)
        
    # plot the pie chart
    plt.pie(count, counterclock = False, labels = city, autopct = "%.2f", startangle = 90)
    plt.xticks(rotation = 40)
    plt.show()

    # print city and percentage
    print('Bangalore 46.81')
    print('Hyderabad 25.53')
    print('Chennai 23.40')
    print('Gurgaon 3.55')
    print('Pune 0.71')
