import sqlite3
con=sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
    create table sales(
        sid,
        year,
        totalsale
    );""")
cur.execute("insert into sales values(1,2022, 56556),(2, 1972,777);")
con.commit()
con.close()