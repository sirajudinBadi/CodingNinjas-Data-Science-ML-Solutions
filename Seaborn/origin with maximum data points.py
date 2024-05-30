"""
Problem statement
In the above plot, from which origin we have majority data points ?

Print the region name. You can take help of scatter plot and some parameters to figure this out.
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
sns.relplot(x = "mpg", y = "horsepower", data = df, hue = 'origin')
plt.show()

print("usa")
