"""
Problem statement: 

You are given n triangles. You are required to find how many triangles are unique out of given triangles. 
For each triangle you are given three integers a, b and c (the sides of a triangle).
A triangle is said to be unique if there is no other triangle with same set of sides.
In other words, we have to find frequency of each triangle and return the count of triangles whose frequency is 1.

Note : It is always possible to form triangle with given sides. 

Input Constraints :
Line 1 : Integer n, the number of triangles
Next n lines : Three integers a,b,c (sides of a triangle).


Output Format :
print single integer, the number of unique triangles.


Constraints :
1 <= n <= 10^4

1 <= a,b,c <= 10^15.

Constraints :
1 <= n <= 10^4

1 <= a,b,c <= 10^15.

Sample Input :
5
7 6 5
5 7 6
8 2 9
2 3 4
2 4 3
Sample Output :
1

Explanation:
The answer will be 1, as there is only one triangle with unique set of sides. 
There are three triangles here: Triangle with sides 2, 3, 4 and Triangle with sides 5, 6, 7 and Triangle with sides 2, 8, 9. 
The frequency of first two triangles is 2 and the frequency of last triangle is 1. 
Hence, there is only one triangle with frequency equal to 1.

"""

#https://twitter.com/Sirajudin79

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def unique_triangles(l):
    areas_of_all_triangle = [] # To store areas of all triangles.
    
    #Looping over all three sizes and storing area of triangle
    for i in range(len(l)):
        area_of_triangle = 1
        for j in range(3): #Triangle always have three sides
            area_of_triangle *= l[i][j]
        areas_of_all_triangle.append(area_of_triangle)


    d = {} # To store frequency of sizes

    #To count the frequency of all triangle areas
    for sum in areas_of_all_triangle:
        d[sum] = d.get(sum, 0) + 1
    
    #To count the unique triangles.
    count = 0
    for value in d.values():
        if value == 1:
            count += 1
    return count


# TO GET INPUT
n = int(input()) # To get the size of list

l= [] # Empty list to populate triangle sizes
for i in range(n): 
    nextRow = [int(i) for i in input().split()] # sizes of triangles.
    l.append(nextRow)
print(unique_triangles(l))

