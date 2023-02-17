import sqlite3
conn=sqlite3.connect('parent.db')
c=conn.cursor()
# c.execute("select * from stocks")
# print(c.fetchone())
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00)
#             ]
# c.executemany('insert into stocks values(?,?,?,?,?',purchases)
#
conn.execute('''create table company
            (id int primary key not null,
            name text not null,
            age int not null,
            address char,
            salary real);''')
print("Table created succesfully")

conn.execute("insert into company values(5,'ram',18,'daman',5000),(6,'prabhu',21,'vapi',3000)")
c.execute("select * from company")
# print(c.fetchone())
# for row in c:
#     print("id=",row[0])
#     print("Name=", row[1])
#     print("Age=", row[2])
#     print("Address=", row[3])
#     print("Salary=", row[4],"\n")
# conn.commit()
# conn.close()

