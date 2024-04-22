"""
Problem statement:
You are given an array of integers that contain numbers in random order. 
Write a program to find and return the number which occurs the maximum times in the given input.

If two or more elements are having the maximum frequency, return the element which occurs in the array first.
"""

# Read input as sepcified in the question
# Print output as specified in the question

from sys import stdin
def maxfreq(arr):
    #Write your code here 
    d = {} 
    for num in arr: 
        if num in d: 
            d[num] += 1 
        else: 
            d[num] = 1 
    ans = arr[0] 
    for num in arr: 
        if d[num] > d[ans]: 
            ans = num 
    return ans 

    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))
