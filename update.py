import sqlite3
conn=sqlite3.connect("Data.db");
sql='''UPDATE student_2 SET s_name="name",s_email="email",s_phone="123456789",s_address="BD",status="0" WHERE s_id=1''';

conn.execute(sql)
conn.commit()
conn.close()



