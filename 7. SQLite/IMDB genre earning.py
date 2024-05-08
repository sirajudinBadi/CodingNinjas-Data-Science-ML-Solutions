"""
Problem statement
IMDB.sqlite' database contains all details of movies and has three tables with name IMDB, genre and earning.

Find out the percentage of the total earning for each genre in IMDB Movie Dataset?Plot the pie chart.

Print the genre and percentage of movies total earning present in that genre with 2 decimal place after rounding off.

Note: Movies has multiple genres, so calculate the percentage for each genre.Total Earning=Domestic earning + WorldWide earning.

Output Format:
genre_1 percent_1
genre_2 percent_2
. . .
. . .
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the libraries
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connected the sqlite data and converted to pandas and joined the tables to get necessary columns
db = sqlite3.connect("IMDB.sqlite")
data = pd.read_sql_query("select IMDB.movie_id, IMDB.Title, earning.Domestic, earning.Worldwide, genre.genre from IMDB inner join earning on IMDB.Movie_id = earning.Movie_id inner join genre on earning.Movie_id = genre.Movie_id", db)
data["Gross"] = data["Domestic"] + data["Worldwide"] # Created column in dataframe

# TO store the genre and corresponding gross earning
di = {}
for i in range(len(data.Gross)):
    di[data.genre[i]] = di.get(data.genre[i], 0) + int(float(data.Gross[i]))

# To store each genre and corresponding gross income
genre_list = []
gross_list = []

for key, value in di.items():
    if key == "":
        continue
    else:
        genre_list.append(key)
        gross_list.append(int(value))

# Calculated total sum and percentages for each genre 
total_earning = sum(gross_list)
pct_list = []
for i in gross_list:
    pct = (i / total_earning) * 100
    pct_list.append("%.2f"%pct)

# Printed the genre and respective percentage of gross income
for i in range(len(pct_list)):
    print(genre_list[i], float(pct_list[i]))

# Plotted the pie chart
plt.pie(pct_list, labels = genre_list)
plt.show()
