"""
Problem statement
Find number of elements to be removed to make an array of all distinct elements.

Example:
Ar = {2,1,4,2,1} 
output = 2 (remove 2 and 1).
"""

def duplicateCount(arr):
    # Please add your code here
    return len(arr) - len(set(arr)) # First we counted the length of list then subtracted the length of set by converting list into set to have only unique entries.

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(duplicateCount(arr))
