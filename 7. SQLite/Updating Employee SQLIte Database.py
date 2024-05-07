"""
Problem statement
A given data of 12 Employees working in an investment firm. 
So add the Employee Data in Employee SQLite Database of Employee_Detail Table which was created by you.

Print 'Done' when you have completed the task.

Note:Save the SQLIte Database in your local system.As it will be used in future question.

Output Format
Done
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

import sqlite3

## Open and read data file as specified in the question
## Print the required output in given format
employee_id=[101,102,103,104,105,106,107,108,109,110,111,112]
name=['Aadarsh','Aarti','Siddharth','Aman','Amit','Shivansh','Vaibhav','Himanshu','Raman','Kunal','Adhira','Tanya']
age=[25,27,25,24,30,26,23,26,25,26,29,24]
department=['Marketing','Operations','Finance','Human Resource','Marketing','IT','Finance','IT','Operations','Marketing','Human Resource','Marketing']
salary=[50000,60000,85000,75000,50000,90000,85000,90000,60000,50000,75000,50000]

db = sqlite3.connect("Employee.sqlite")
cur = db.cursor()

# Created a table
cur.execute("create table Employee_Detail(Employee_ID int primary key, Name text, Age int, Department text, Salary int)")

# Used for loop to iterate through every list and inserted each row in the database
for i in range(len(employee_id)):
    cur.execute('insert into Employee_Detail values(?, ?, ?, ?, ?)', (employee_id[i], name[i], age[i], department[i], salary[i]))

# Commited and closed the sqlite table.
db.commit() 
db.close()
print("Done")
