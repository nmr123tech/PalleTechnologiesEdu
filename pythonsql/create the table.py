#creating the table
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hima123')
cursor=mydb.cursor()
s='create table student(id int,name varchar(40))'
cursor.execute(s)

