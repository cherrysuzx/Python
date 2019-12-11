import pymysql as mdb

# 连接MySQL
conn = mdb.connect("localhost","root","root","python")
cursor = conn.cursor()
cursor.execute('select * from test1')
data = cursor.fetchall()
print(data)

# 连接Linux下MySQL
conn = mdb.connect("192.168.106.120","root","123456","spark")
cursor = conn.cursor()
cursor.execute('select * from student')
data = cursor.fetchall()
print(data)