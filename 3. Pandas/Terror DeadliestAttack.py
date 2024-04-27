"""
Problem statement
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
Most Deadliest attack in a history of HumanKind?

Print count of Killed people as integer value.

Note: Here Deadliest attack means, in which the most number of people killed.

Output Format :
NumberOfPeopleKilled Country TerroristGroup
"""

# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


## Open and read data file as specified in the question
## Print the required output in given format

import pandas as pd

terrorism = pd.read_csv("terrorismData.csv")

df = terrorism.copy()

kill_count  = df.iloc[df['Killed'].argmax()].Killed
country = df.iloc[df['Killed'].argmax()].Country
group = df.iloc[df['Killed'].argmax()].Group
print(int(kill_count), country, group)
