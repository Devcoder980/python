import sqlite3
con=sqlite3.connect(":memory:")
# con.execute("""
#     select * from pragma_compile_options
#     where compile_options like 'THREADSAFE=%'""").fetchall()
#
# con.close()
# con = sqlite3.connect("file:template.db?mode=ro", uri=True)
# Create a shared named in-memory database.
# con1 = sqlite3.connect("file:mem1?mode=memory&cache=shared", uri=True)
# con2 = sqlite3.connect("file:mem1?mode=memory&cache=shared", uri=True)
# con1.executescript("create table t(t); insert into t values(28);")
# rows = con2.execute("select * from t").fetchall()
# print(rows)

cur = con.cursor()
cur.executescript("""
    create table person(
        firstname,
        lastname,
        age
    );

    create table book(
        title,
        author,
        published
    );

    insert into book(title, author, published)
    values (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
    """).fetchall()
con.commit()
cur.execute('select * from book')
for row in cur:
    print(row)

con.close()