import sqlite3
conn=sqlite3.connect('parent.db')
c=conn.cursor()


print("Opened Database successfully")
conn.execute("delete from company where id=5")
conn.commit()
print("Total number of changes:",conn.total_changes)
c.execute("select * from company")
print(c.fetchone())
print(c.fetchone())

conn.close()