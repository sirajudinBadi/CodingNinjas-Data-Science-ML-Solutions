"""
Problem statement
IMDB.sqlite database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the least budgeted movie in IMDB Movie Database.

If there is more than one least budgeted movies then print the movie which has maximum net profit.

Note: Net Profit= Total Earning(Domestic+WorldWide earning) - budget

Output Format:
movie_name
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the library
import sqlite3

# connected the sqlite data and created the cursor of the same.
db = sqlite3.connect("IMDB.sqlite")
cur = db.cursor()

# Executed the sql query to get the movie with the least budget and among them having highest net profit.
data = cur.execute("select IMDB.Title from IMDB inner join earning on IMDB.Movie_id = earning.Movie_id where IMDB.Budget = 1000000.0 order by((earning.Domestic + earning.Worldwide) - IMDB.Budget) DESC LIMIT 1")
ans = data.fetchall()
for i in ans:
    print(*i)
