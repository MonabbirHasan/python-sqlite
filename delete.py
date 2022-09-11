import sqlite3
conn=sqlite3.connect("Data.db");
sql='''DELETE FROM student_2 WHERE s_id=1''';

conn.execute(sql)
conn.commit()
conn.close()
