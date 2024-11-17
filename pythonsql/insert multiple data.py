import mysql.connector
mydb=(mysql.connector.connect(host='localhost',user='root',password='root',database='hima123'))
cursor=mydb.cursor()
s ="insert into book(bookid,title,price) values(1,'python',200)"
cursor.execute(s)
mydb.commit()
