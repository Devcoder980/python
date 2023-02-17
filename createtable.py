
import sqlite3
conn = sqlite3.connect('college.db')
c = conn.cursor()
a=conn.execute("select * from stud_attendance;")
# print(a.fetchall())


# def ctr(tablename=None,f1=None,f2=None,f3=None,f4=None,f5=None):
#     import sqlite3
#     conn=sqlite3.connect('college.db')
#     c=conn.cursor()
#     formatstr=f'''create table {tablename}({f1} primary key not null,{f2} not null,{f3},{f4},{f5} );'''
#     conn.execute(formatstr)
#     print("Table created successfully")
#     conn.commit()
#     conn.close()
# def ctr(tablename=None,f1=None,f2=None,f3=None,f4=None,f5=None,f6=None):
#     import sqlite3
#     conn=sqlite3.connect('college.db')
#     c=conn.cursor()
#     conn.execute(f'''create table {tablename}({f1}primary key not null,{f2} not null,{f3} ,{f4} ,{f5},{f6} );''')
#     print("Table created succesfully")
#     conn.commit()
#     conn.close()
# def ctr(tablename=None,f1=None,f2=None,f3=None,f4=None):
#     import sqlite3
#     conn=sqlite3.connect('college.db')
#     c=conn.cursor()
#     formatstr=f'''create table {tablename}({f1} primary key not null,{f2} not null,{f3},{f4} not null);'''
#     conn.execute(formatstr)
#     print("Table created succesfully")
#     conn.commit()
#     conn.close()
