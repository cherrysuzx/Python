import cx_Oracle
db=cx_Oracle.connect('scott/123456@localhost:1521/orcl')
cursor=db.cursor()
cursor.execute("select * from test")
data=cursor.fetchall()
print(data)
cursor.execute("select name,class,score,row_number() over(partition by class order by score desc) from test")
data2=cursor.fetchall()
print(data2)