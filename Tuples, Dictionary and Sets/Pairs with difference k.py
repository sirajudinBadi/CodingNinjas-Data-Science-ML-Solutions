"""
Problem statement :
You are given with an array of integers and an integer K. 
You have to find and print the count of all such pairs which have difference K.

Note: Take absolute difference between the elements of the array.


"""
# https://twitter.com/Sirajudin79

def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pairCount = 0
    m = {}
    for num in l:
        if num+k in m:
            pairCount += m[num+k]
        if k!=0 and num-k in m:
            pairCount += m[num-k]

        # Update map        
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
            
    return pairCount
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
