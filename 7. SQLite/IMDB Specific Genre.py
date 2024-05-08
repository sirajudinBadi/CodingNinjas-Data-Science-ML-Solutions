"""
Problem statement
IMDB.sqlite' database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the movie which has genre of 'Sci-Fi' and 'Mystery' and movie rating is greater or equal to 8 from IMDB Movie Database.

Print the movie name.

Movies has multiple genre.

Output Format:

movie_name
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


## Open and read data file as specified in the question
## Print the required output in given format

# Imported the libraries
import sqlite3
import pandas as pd

# Connected the sqlite data file and later converted to pandas dataframe and querried to get the conditional output
db = sqlite3.connect("IMDB.sqlite")
data = pd.read_sql_query("select IMDB.Movie_id, IMDB.Title, IMDB.Rating, genre.genre from IMDB inner join genre on IMDB.Movie_id = genre.Movie_id where genre in ('Sci-Fi', 'Mystery') and IMDB.Rating >= 8.0 ", db)

# If the movie has both the genre and rating >= 8 then it will be printed twice consecutively so used the below logoc
for i in range(len(data.Title)):
    if data.Title[i] == data.Title[i + 1]:
        print(data.Title[i])
        break
