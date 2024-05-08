"""
Problem statement
IMDB.sqlite' database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the count of each genre present in IMDB movie dataset?

Print the Genre and number of movies present in that genre.

Note: Ignore the empty value present in genre.

Output Format:
genre_1 num_movie_1
genre_2 num_movie_2
. . .
. . .
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the library
import sqlite3

# Connected the sqlite file and created the cursor
db = sqlite3.connect("IMDB.sqlite")
cur = db.cursor()

# Executed the sql query to fetch required data
cur.execute("select genre, count(genre) from genre group by genre")
ans = cur.fetchall()

# looped through fetched data while negating the empty value
for i in range(1, len(ans)):
    print(*ans[i])
