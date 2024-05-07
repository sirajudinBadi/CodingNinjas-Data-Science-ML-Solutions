"""
Problem statement
Find the number of employee working in different department in an investment firm from Employee SQLite Database.

Print the department and number of employee

Output Format:
department_1 num_employee_1
department_2 num_employee_2
department_3 num_employee_3
.  .  . 
.  .  .
.  .  .
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴

## Open and read data file as specified in the question
## Print the required output in given format

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

# Wrote a   query to get the department wise count using group by
cur.execute('select department, count(department) from Employee_Detail group by department')
ans = cur.fetchall()

for i in range(len(ans)):
    print(*ans[i])

# Commited and closed the sqlite table.
db.commit() 

