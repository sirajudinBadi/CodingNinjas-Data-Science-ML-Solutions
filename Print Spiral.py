"""
Problem statement
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:

a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
 Mind that every element will be printed only once.
"""

from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    top = 0 # for index of topmost row
    bottom = nRows - 1 # for index of bottommost row
    left = 0 # for the index of leftmost that is first column
    right = mCols - 1 #for the index of rightmost column

    while top <= bottom and left <= right: # To bypass the index error

        # for left to right row
        for i in range(left, right + 1):
            print(mat[top][i], end=' ')
        top += 1 # to eliminate the top row that is already printed.


        # To print the rightmost column
        for i in range(top, bottom + 1):
            print(mat[i][right], end= ' ')
        right -= 1 #To eliminate the last column that is already printed.


        #If there are more than two rows are provided in the input.
        if top <= bottom:

            #To print the bottom most row
            for i in range(right, left - 1, -1):
                print(mat[bottom][i], end=' ')
            bottom -= 1 #To exclude the bottom most row
        

        #To check if more than 2 columns provided or not
        if left <= right:

            #To print the right most column that is the first column
            for i in range(bottom, top - 1, -1):
                print(mat[i][left], end=' ')
            left += 1 # Will eliminate first column.
    



























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
