"""
Problem statement
For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row or column) amongst all the rows/columns.

Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
"""

#https://twitter.com/Sirajudin79

from sys import stdin
MIN_VALUE = -2147483648


def findLargest(arr, nRows, mCols):
    #Your code goes here
    is_row = True #putting a flag for maintaining edge case.
    largest_sum = MIN_VALUE
    index = 0
  
    # To get the sum of Ith row
    for i in range(nRows):
        sum_of_row = 0 
        for j in range(mCols):
            sum_of_row += arr[i][j]
        if sum_of_row > largest_sum:
            largest_sum = sum_of_row
            index = i
          
    #To get the sum of Jth column.      
    for j in range(mCols):
        sum_of_column = 0 #for sum of jth column
        for i in range(nRows):
            sum_of_column += arr[i][j]
        if sum_of_column > largest_sum:
            largest_sum = sum_of_column
            index = j
            is_row = False
          
    # Printing the output in specified format.
    if is_row:
        print("row "+str(index)+" "+str(largest_sum))
    else:
        print("column "+str(index)+" "+str(largest_sum))


#Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
