"""
Problem statement
For the given dataset "FuelEconomy.csv"

Create a Linear Regressor and fit the dataset in this. After that, print the coefficient and intercept.

Note:

 1. Inside the function "train_test_split", use the "random_state = 42".
 2. Split the dataset in the ratio of 70:30 into the training and testing datasets.
To know more about randomstate please read the document given regarding randomstate.

Output

Print the coefficient and intercept in separate lines rounded off to 2 decimal places.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# Imported the libraries
import numpy as np 
from sklearn import model_selection
from sklearn.linear_model import LinearRegression

# Loaded the csv file using numpy and set the delimiter as coma
data = np.loadtxt("FuelEconomy.csv", delimiter = ",")

# reshaped the data because there is only one feature in the data.`
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

# defined the test and train data in 30:70 ratio and using random_state
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state = 42, test_size = 0.3)

# Created the linear object and fitted the train data
alg1 = LinearRegression()
alg1.fit(x_train, y_train)

# To print the coefficient and intercept 
m = alg1.coef_[0]
c = alg1.intercept_[0]
print(np.round(m[0], 2))
print(np.round(c, 2))
