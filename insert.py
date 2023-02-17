# import sqlite3
# conn=sqlite3.connect('parent.db',uri=True)
# c=conn.cursor()
# #
# # purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
# #              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
# #              ('2006-04-06', 'SELL', 'IBM', 500, 53.00)
# #             ]
# # c.executemany('insert into stocks values(?,?,?,?,?',purchases)
#
#
# conn.execute("insert into company values(60,'ram',18,'daman',5000),(9,'prabhu',21,'vapi',3000)")
# # cur.execute("insert into lang values (?, ?)", ("C", 1972))
# conn.commit()
# conn.close()


# import sqlite3
# conn = sqlite3.connect('college.db', uri=True)
# c = conn.cursor()
# a=conn.execute("select * from stud_assignment where total_assignment>=3;")
# print(a.fetchall())
#
#
import sqlite3
conn = sqlite3.connect('college.db', uri=True)
c = conn.cursor()
rno=input('enter the roll no for accept assignment')
a=[4,5,6,7,8,11,12,14,56,78,34,45]
for i in a:
    conn.execute(f"insert into  stud_attendentce values({i*10},'math',5,5,4);")
    print("insert")
conn.commit()
a=conn.execute(f"select total_lect from stud_attendentce where rno={rno} and total_lect>=10;")
print("assignment accepted")
print(a.fetchone())
conn.close()

# conn.close()
# import  csv
# c=open('csv3.csv','w',newline='')
# c1=csv.writer(c)
# import sqlite3
# conn = sqlite3.connect('college.db', uri=True)
# c = conn.cursor()
# a=conn.execute("select rno,name ,division from student_master where  age>19;")
# v=a.fetchall()
# c1.writerow(v)
# print("succesfulay werite")
# c.close()
# conn.close()

def insertvalue7(tablename=None,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None,val7=None):
    import sqlite3
    conn = sqlite3.connect('college.db', uri=True)
    c = conn.cursor()
    conn.execute(f"insert into {tablename} values({val1},{val2},{val3},{val4},{val5},{val6},{val7});")
    print("Table inserted")
    conn.commit()
    conn.close()
