#delete record from table
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hima123')
cursor=mydb.cursor()
s="delete from book where title ='java'"
cursor.execute(s)
mydb.commit()