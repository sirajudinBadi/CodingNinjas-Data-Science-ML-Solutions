"""
Find the employee_id of employee whose is working in Finance Department in Investment firm from Employee SQLite Database.

Print the employee_id as integer value

Output Format:

employee_id_1
employee_id_2
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

# Commited sqlite table.
db.commit() 

# Wrote the qquery to get the employee_id who is working in finance department.
cur.execute("select employee_id from Employee_Detail where department = 'Finance'")
ans = cur.fetchall()

# Ran a for loop to get the employee id and converted into integer format
for i in range(len(ans)):
   for j in range(1):
       print(int(ans[i][j]))
