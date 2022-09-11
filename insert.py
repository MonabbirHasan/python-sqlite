import sqlite3

conn=sqlite3.connect("Data.db")

sql='''INSERT INTO student_2(s_name,s_email,s_phone,s_address,status) VALUES('khan','hmd320667@gmail.com','01743714489','Dhaka','1')''';

conn.execute(sql);
conn.commit()
conn.close()


