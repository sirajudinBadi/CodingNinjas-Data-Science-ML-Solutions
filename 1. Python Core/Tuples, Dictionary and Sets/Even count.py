"""
Problem statement
You are provided with an integer array where each number is present either odd number of times or even number of times.
You have to find and return the number which is present even number of times.

If multiple numbers are present even number of times, then return that number which occurs first among these numbers in the given array. If no such number exists, then return -1.

Note : You may take extra space but solve this problem in O(n) time.
"""
#https://twitter.com/Sirajudin79

def evenCount(arr):
    frequency = {}  # Dictionary to store the frequency of every number in array.
    
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1
    
    # To find the first number with an even frequency
    for i in arr:
        if frequency[i] % 2 == 0:
            return i
    
    # To satisfy the edge case
    return -1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(evenCount(arr))
