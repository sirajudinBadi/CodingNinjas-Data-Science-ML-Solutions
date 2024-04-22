"""
Problem statement
In a given string, find the first non-repeating character .
You are given a string, that can contain repeating characters. 
Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once. 
The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). 
If there is no non-repeating character print the first character of string.
"""
#https://twitter.com/Sirajudin79

def nonRepeatingChar(string):
    # Please add your code here
    d = {}
    for i in string:
        d[i] = d.get(i, 0) + 1

    for char in string:
        if d[char] == 1:
            return char  

# Main
string = input()
print(nonRepeatingChar(string))
