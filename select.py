import sqlite3
from tkinter import *
from tkinter import Label
root=Tk();
conn=sqlite3.connect("Data.db");
sql='''SELECT * FROM student_2 LIMIT 3''';
data=conn.execute(sql);
for i in data:
	mylabel=Label(root,text=(" Id::", i[0],"name:: ",i[1] ," E-mail::", i[2]," Phone::", i[3]," Address::", i[4]," status::", i[5]),fg='blue',bg='#bbb',pady=20,padx=20,font=('arial',12));
	mybutton=Button(root,text='button');
	Shadow(mybutton, color='#ff0000', size=1.3, offset_x=-5, onclick={'color':'#00ff00'})
	mylabel.pack()
root.mainloop()
conn.close()