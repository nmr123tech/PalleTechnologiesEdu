import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='hima123')
cursor=mydb.cursor()
s="insert into book values(3,'javascript',500)"
cursor.execute(s)
mydb.commit()