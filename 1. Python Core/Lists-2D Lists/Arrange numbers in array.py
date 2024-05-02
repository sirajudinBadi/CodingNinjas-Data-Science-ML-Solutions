"""
Problem statement :
You have been given an empty array(ARR) and its size N. The only input taken from the user will be N and you need not worry about the array.

Your task is to populate the array using the integer values in the range 1 to N(both inclusive) in the order - 1,3,5,.......,6,4,2.

Note:
You need not print the array. You only need to populate it.
"""

from sys import stdin

def arrange(arr, n) :
    #Your code goes here
    odd = 1 #For odd numbers starting point
    even = 2 # Even numbers starting point
    
    for i in range(n // 2): # To decide the boundary bewtween odd and even numbers
        arr[i] = odd # From left side that is odd side.
        arr[n - i - 1] = even # From right side that is even side.
        odd += 2 #To get the next odd number
        even += 2 # To get the next even number.
    
    if n % 2 == 1: #To fulfill the condition if n is odd
        arr[n // 2] = n
    











#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()



#main
t = int(stdin.readline().strip())

while t > 0 :
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList(arr, n)
    t -= 1
