"""
Problem statement :
Create a function that determines whether a given number N belongs to the Fibonacci sequence. 
If N is found in the Fibonacci sequence, the function should return true; otherwise, it should return false.



Sample Input 1 :
5

Sample Output 1 :
true

Explanation :
Fibonacci sequence begins 0, 1, 1, 2, 3, 5, ... and so on. Since 5 appears in the sequence.
"""


def checkMember(n):
    # write your code logic here !!!!
    fib_list = [0, 1] # Will store all fib elements here
    a, b = 0, 1
    for i in range(n):
        c = a + b
        a, b = b, c
        fib_list.append(c)
    
    if n in fib_list: #Checked if n exists in fib series or not.
        return True
    else:
        return False
        




    
