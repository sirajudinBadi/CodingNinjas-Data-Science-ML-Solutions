"""
Problem statement
In Little Flowers Public School, there are many students with same first names. You are given a task to find the students with same names. You will be given a string comprising of all the names of students and you have to tell the name and count of those students having same. If all the names are unique, print -1 instead.

Note: We don't have to mention names whose frequency is 1.
"""
#https://twitter.com/Sirajudin79

def differentNames(l):
    d = {} # Created empty dict to store names with frequency.
    for name in l:
        d[name] = d.get(name, 0) + 1
    
    result = {} #To store names having frequency more than 1
    for key, value in d.items():
        if value > 1:
            result[key] = value

    return result # will return dictionary because CN has already provided output printing code.

# Main
names = input().strip().split()
m = differentNames(names)
if m:
    for name, count in m.items():
        print(name, count)
else:
    print(-1)
