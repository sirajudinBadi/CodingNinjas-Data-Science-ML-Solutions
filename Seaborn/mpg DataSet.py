"""
Problem statement
Load the existing dataset “mpg” in your python notebook.

By plotting a scatter plot, check if there is any relationship between two variables - mpg and horsepower.

Display the scatter plot and print if these two variables are related. If they are related, then print “Yes” otherwise print “No”.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the libraries and loaded default color pallete from Seaborn
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 
sns.set()

# Loaded the dataset
df = sns.load_dataset("mpg")

# Plotted the relational plot and it showed the scatter plot with linear relationship tendency so printed the Yes.
sns.relplot(x = "mpg", y = "horsepower", data = df)
plt.show()

print("Yes")
