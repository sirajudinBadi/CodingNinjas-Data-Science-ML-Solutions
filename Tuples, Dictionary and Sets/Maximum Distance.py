"""
Problem statement
Given an array that might contain duplicate elements, 
find the maximum possible distance between occurrences of two repeating elements i.e. elements having the same value. 
If there are no duplicate elements in the array, return 0.
"""

# https://twitter.com/Sirajudin79 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈

def max_dist(arr):
    index_map = {}  # Dictionary to store the last seen index of each element
    max_distance = 0
    
    for i, num in enumerate(arr):
        if num in index_map:
            distance = i - index_map[num]
            if distance > max_distance:
                max_distance = distance
        else:
            index_map[num] = i
    
    return max_distance

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Print output
print(max_dist(arr))
