import sqlite3
conn=sqlite3.connect('parent.db')
c=conn.cursor()
# Todo:Fist method print values
c.execute("select * from company")
# print(c.fetchone())
# for row in c:
#     print("id=",row[0])
#     print("Name=", row[1])
#     print("Age=", row[2])
#     print("Address=", row[3])
#     print("Salary=", row[4],"\n")
# Todo:second method print values
# for row in c.execute("select * from company"):
#     print(row)
# Todo:third method to print values
# Print single matching row or call use a print id=5 type value print
# print(c.fetchone()[1]) print a value of colum index 1 only
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())
# All values print in single line
# print(c.fetchall())

# Todo:Total chages values
# print(conn.total_changes)

# Todo:table create statment
# conn.execute('''create table company
#             (id int primary key not null,
#             name text not null,
#             age int not null,
#             address char,
#             salary real);''')
conn.commit()
conn.close()