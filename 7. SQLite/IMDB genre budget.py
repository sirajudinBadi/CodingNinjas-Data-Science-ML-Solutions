"""
Problem statement
IMDB.sqlite' database contains all details of movies and has three tables with name IMDB, genre and earning.

Find out the percentage of the budget for each genre in IMDB Movie Dataset?Plot the pie chart.

Print the genre and percentage of movies budget present in that genre with 2 decimal place after rounding off..

Note: Movies has multiple genres, so calculate the percentage for each genre.Replace empty budget column to zero.

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

#Imported the libraries
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 

# Connected the sqlite file and converted to pandas dataframe
db = sqlite3.connect("IMDB.sqlite")
df = pd.read_sql_query("select IMDB.Movie_id, Title, Budget, genre.genre from IMDB inner join genre on IMDB.Movie_id = genre.Movie_id", db)
df[df["Budget"] == ""] = 0.0 # Where budget is empty

# To store the genre and respected budget allocation.
di = {}
for i in range(len(df.genre)):
    di[df.genre[i]] = di.get(df.genre[i], 0) + int(float(df.Budget[i]))

# To store each genre, correesponding budget and counted total amount of budget of budget column
genre_list = []
budget = []
total = 0

for key, value in di.items():
    if key == "" or key == 0.0:
        continue
    genre_list.append(key)
    budget.append(value)
    total += value

# Counted the percentages of budget for each genre
pct_list = []
for i in budget:
    pct = (i / total) * 100
    pct_list.append(pct)

# Printed the genre and corresponding percentage amount of budget
for i in range(len(genre_list)):
    print(genre_list[i], "%.2f" %pct_list[i])

# Plotted the pie chart 
plt.pie(pct_list, labels = genre_list, autopct = "%.2f")
plt.show()
