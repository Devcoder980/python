import sqlite3
conn=sqlite3.connect('library.db')
c=conn.cursor()
# conn.execute('''create table SCompany
#     (cin int primary key,
#     cname text,
#     ctitle text,
#     contact text);''')
# print('Table create successfully')
c.execute("insert into scompany values(2202,'nayaka','beauty of nature',9898767687)")
print("insert successfully")
conn.commit()
conn.close()