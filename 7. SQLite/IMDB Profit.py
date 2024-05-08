"""
Problem statement
IMDB.sqlite database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the movie which has maximum net profit in IMDB Movie Database.

Print the movie name.

Note: Net Profit= Total Earning(Domestic+WorldWide earning) - budget

Output Format:
movie_name
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the library
import pandas as pd
import sqlite3

# Connected the sqlite data and created the cursor
db = sqlite3.connect("IMDB.sqlite")
cur = db.cursor()

# Executed the sql query with join and counted the net profit too.
data = cur.execute("SELECT IMDB.Title FROM IMDB INNER JOIN earning ON IMDB.Movie_id = earning.Movie_id ORDER BY ((earning.Domestic + earning.Worldwide) - IMDB.Budget) DESC LIMIT 1")
ans = data.fetchall()
print(*ans[0]) # Printed the final result
