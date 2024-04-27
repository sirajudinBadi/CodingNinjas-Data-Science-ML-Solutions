"""
Problem statement:
Given file "terrorismData.csv"

It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period

Problem Statement :
The Most Dangerous city in Jammu and Kashmir and the terrorist group which is most active in that city?

Print count of number of attacks in that city as integer value.

Note:Ignoring the Unknown Terrorist Group.Here Dangerous related with the number of terrorist attacks.

Output Format :
City NumberOfAttack Group
"""
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉www.linkedin.com/in/SirajudinBadi79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
# 👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉https://twitter.com/Sirajudin79     👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈


import pandas as pd
df = pd.read_csv('terrorismData.csv')

# To Filter out the states value with Jammu and Kashmir
df = df[df.State=='Jammu and Kashmir']

# To get the count of each city
df_list = df['City'].value_counts()

city = df_list.index[0] # Stored city with highest number of attacks
count = df_list.values[0] # Stored the number of attacks in Dangerous City

df = df[df['City']==city]
group = df['Group'].value_counts().index[1] # To get the notorious group

print(city,count,group)
