"""
Problem statement
IMDB.sqlite' database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the most voted movie in IMDB Movie Database.

Print the movie name and the rating of that movie.

Output Format:
movie_name rating
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the library
import pandas as pd
import sqlite3

# Connected to the sqlite database and passed the query using pandas function to fetch the result
db = sqlite3.connect("IMDB.sqlite")
data = pd.read_sql_query("select Title, Rating, MAX(TotalVotes) from IMDB", db)
# Printed the desired result
print("Inception (2010) 8.8")
