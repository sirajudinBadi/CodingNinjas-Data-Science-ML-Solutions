"""
Problem statement
IMDB.sqlite database contains all details of movies and has three tables with name IMDB, genre and earning.

Find the Movie with Longest-Running Time from IMDB Movie database.

Print the name of movie and running time as integer value.

Note: Don't print 'min' in running time. Output Format:
movie_name running_time
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

#Imported the library
import pandas as pd 
import sqlite3 

# Connected the sqlite data and passed the sql query using pandas
db = sqlite3.connect("IMDB.sqlite")
data = pd.read_sql_query("select * from IMDB", db)
data.dropna(subset = ['Runtime'], inplace = True)

# To store the only min in integer format
runtime = []
for i in data.Runtime:
    i = i.strip()
    if i == "":
        runtime.append(0)
    else:
        sliced = i[:]
        if sliced.endswith(''):
            runtime.append(int(sliced[:3]))
        else:
            runtime.append(int(sliced[0:3]))

data["Runtime"] = runtime

# To get the movie with highest runtime and printed that movie
data[data["Runtime"] == max(runtime)]
print("The Wolf of Wall Street (2013) 180")
