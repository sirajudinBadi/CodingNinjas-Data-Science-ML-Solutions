"""
Problem statement
For the given dataset "FuelEconomy.csv"

Create a Linear Regressor and fit the dataset in this and then print the training and testing score for this regressor.

Note: Inside the function "traintestsplit" use the "random_state = 42".Split the data into 70% in training data and 30% in testing data.

To know more about randomstate please read the document given regarding randomstate.

Output

Print the testing and training scores in separate lines rounded off to 3 decimal places.
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://x.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

# imported the libraries
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import numpy as np 

# Loaded the csv data using numpy
data = np.loadtxt("FuelEconomy.csv", delimiter = ",")

# Reshaped the data in 2d array beacause there is only 1 feature
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1 ,1) 

# split the train and test data
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state = 42, test_size = 0.3)

# created the algorithm object and fit the training data in it
alg1 = LinearRegression()
alg1.fit(x_train, y_train)


# printed the score of training and test data
score_train = alg1.score(x_train, y_train)
score_test = alg1.score(x_test, y_test)

print(round(score_test, 3))
print(round(score_train, 3))

