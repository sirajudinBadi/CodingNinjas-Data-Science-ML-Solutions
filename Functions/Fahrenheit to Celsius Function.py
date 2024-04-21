"""
Problem statement
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.


Note:
You don't have to write the main function or take input. It has already been taken care of and you need to just print the integer value . Just write the code that prints Fahrenheit to Celsius table in the function itself.
Formula is C = (F - 32) * 5/9

Sample Input 1:
0 
100 
20

Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37
"""




def printTable(start,end,step):
#Implement Your Code Here
	#First we will loop from start to end at step interval
	for i in range(start, end + 1, step):
		celsius = int((i - 32) * (5 / 9)) # Applied formula and stored in integer format.
		print(str(i) + " " + str(celsius)) #Printed the output in specified string format.
	

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)











