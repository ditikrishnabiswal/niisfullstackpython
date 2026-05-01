import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT * FROM student")
rows=cur.fetchall()
for  r in 'row':
	print(r)
conn.close()