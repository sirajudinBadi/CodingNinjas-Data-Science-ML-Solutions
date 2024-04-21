"""
Problem statement:
Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.

That is, we can switch from one array to another array only at common elements.

If no intersection element is present, we need to take sum of all elements from the array with greater sum.

Sample Input :
6
1 5 10 15 20 25
5
2 4 5 9 15

Sample Output :
81

Explanation :
We start from array 2 and take sum till 5 (sum = 11). 
Then we'll switch to array at element 10 and take till 15. So sum = 36. 
Now, no elements left in array after 15, so we'll continue in array 1. 
Hence sum is 81
"""


def maxPathSum(arr1, arr2, m, n):

	#Variable initialization
    maxsum = 0
    sum1 = 0
    sum2 = 0
    i = 0
    j = 0

	#We used while loop to iterate over both the array at the same time.
    while i < m and j < n:
        if arr1[i] < arr2[j]: # To check in which array first element is smaller, we will append that to respective sum variable
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            maxsum += max(sum1, sum2) + arr1[i] # Whatever sum is greater will append ite to final sum.
            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    # Adding remaining elements
    while i < m:
        sum1 += arr1[i]
        i += 1
    while j < n:
        sum2 += arr2[j]
        j += 1
    maxsum += max(sum1, sum2)
    return maxsum


m = int(input())
arr1 = list(map(int, input().split()))
n = int(input())
arr2 = list(map(int, input().split()))

ans = maxPathSum(arr1, arr2, m, n)
print(ans)
