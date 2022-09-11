import sqlite3

conn=sqlite3.connect("Data.db");

create_table='''CREATE TABLE student_2(
s_id INTEGER PRIMARY KEY AUTOINCREMENT,
s_name TEXT NOT NULL,
s_email TEXT NOT NULL,
s_phone TEXT NOT NULL,
s_address TEXT NOT NULL,
status INTEGER NOT NULL
)
''';
conn.execute(create_table);
conn.close()