#inserting data :
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hima123')
mycursor = mydb.cursor()
s="insert into book(bookid,title,price) values(2,'python',688)"#variables
mycursor.execute(s)
mydb.commit()