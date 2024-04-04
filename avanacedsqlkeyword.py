import mysql.connector

connection = mysql.connector.connect(
    host ="localhost", 
    user="root", 
    password="*****",##your passward of MySQL workbench 
    database= "employeedb")
if connection.is_connected():
    print("MySQL Connected...")
else:
    print("not connected")

#CURD operation
createEmployee ="create table if not exists employee(empname text, empdept text, empemail text, empsalary int)"
mycursor = connection.cursor()
mycursor.execute(createEmployee)

##insert data
# addEmployee= "insert into employee values('{}', '{}', '{}', {})".format(input("Enter employee name:"), input("Enter employee department:"), input("Enter employee email:"), int(input("Enter salary:")))
# mycursor.execute(addEmployee)
# connection.commit()

##mysql keyword
##AND operator- to validate more then one condition (both condition must be truee)
# andQuery= "select * from employee where empdept ='gamer' AND empsalary >60000"
# mycursor.execute(andQuery)
# print(mycursor.fetchall())
# connection.commit()

##OR operator - to validate any of the conditions is true or not (any one condition  must be true)
# orQuery = "Select * From Employee Where empname='avi' OR empsalary > 60000"
# mycursor.execute(orQuery)
# print(mycursor.fetchall())
# connection.commit()

##Not operator- to give -ve result(print data which not fullfill the given condition)
# notQuery = "Select * From Employee Where NOT empdept='gamer'"
# mycursor.execute(notQuery)
# print(mycursor.fetchall())
# connection.commit()

##LIMIT operator- return data based on limit no
##find the higest 2 paid emp
# limitQuery = "select * from employee Order By empsalary DESC LIMIT 2"
# mycursor.execute(limitQuery)
# print(mycursor.fetchall())
# connection.commit()

##order by- it will returnm dara in sequence format ascending or descending
# orderbyQuery = "select * from employee Order By empname DESC"
# mycursor.execute(orderbyQuery)
# print(mycursor.fetchall())
# connection.commit()

##MAX- it return the max value from record
# maxQuery="SELECT MAX(empsalary) FROM employee"
# mycursor.execute(maxQuery)
# print(mycursor.fetchall())
# connection.commit()

##MIN- it will return the min value
# minQuery="SELECT MIN(empsalary) FROM employee"
# mycursor.execute(minQuery)
# print(mycursor.fetchall())
# connection.commit()

##COUNT- it will retun the no of rows
# countQuery="SELECT COUNT(empname) FROM employee"
# mycursor.execute(countQuery)
# print(mycursor.fetchall())
# connection.commit()

##AVG- it will find the avg value from the record
# avgQuery="SELECT AVG(empsalary) FROM employee"
# mycursor.execute(avgQuery)
# print(mycursor.fetchall())
# connection.commit()

##SUM- it will add all the values and give the total sum
# sumQuery="SELECT SUM(empsalary) FROM employee"
# mycursor.execute(sumQuery)
# print(mycursor.fetchall())
# connection.commit()

##Alias- rename the column name or table name
# aliasQuery = "select empname as EmployeeName from employee"
# mycursor.execute(aliasQuery)
# print(mycursor.fetchall())
# connection.commit()

##between- it will show the record in range
# betweenQuery = "select * from employee where empsalary between 60000 AND 70000"
# mycursor.execute(betweenQuery)
# print(mycursor.fetchall())
# connection.commit()

#find the emp name a to z
# betweenQuery = "select * from employee where empsalary between 'a' AND 'z' order by empname"
# mycursor.execute(betweenQuery)
# print(mycursor.fetchall())
# connection.commit()

##LIKE- search the record based on the string pattern matching(start with % end with, string____%)(for mid %string%)
# likeQuery = "select * from employee where  empname LIKE 'n___%'" 
# mycursor.execute(likeQuery)
# print(mycursor.fetchall())
# connection.commit()

##NOTLIKE- (-ve statement)give all data Except the fivrn string(start with % end with, string____%)(for mid %string%)
# notlikeQuery = "select * from employee where  empname NOT LIKE 'n%'" 
# mycursor.execute(notlikeQuery)
# print(mycursor.fetchall())
# connection.commit()

##IN- it will work on multiple value and act like OR
# inQuery = "Select * From employee Where  empdept IN ('SD','software developer')"
# mycursor.execute(inQuery)
# print(mycursor.fetchall())
# connection.commit()

##Group By- combine multiple rows and use with count, max, min, avg, sum
# groupByQuery = "select COUNT(empname), empdept from employee Group By empdept"
# mycursor.execute(groupByQuery)
# print(mycursor.fetchall())
# connection.commit()

##having - it will work with where and order by, group by also check conditionbased on AVG, COUNT, SUM
##check the team having  more than one person or not
# havingQuery = "select COUNT(empname), empdept from employee Group By empdept HAVING  COUNT(empname) >=1"
# mycursor.execute(havingQuery)
# print(mycursor.fetchall())
# connection.commit()