# todo: sqlite3
# import sqlite3
# con = sqlite3.connect(":memory:")
# The special path name todo :memory: can be provided to create a temporary database in RAM
# Once a Connection has been established, create a Cursor object and call its execute()
# method to perform SQL commands:

# todo:Delter,insert ,create ,update use after commit statement
# con.commit()
# last me con ko close karna jaruri h


# import  createtable
# print("Please insert table name after colums name ")
# createtable.ctr('stud_attendell','rno','subject','month')

import pkg.i



# insert.fach('student_master')
def insertvalue(tablename,val1=None,val2=None,val3=None,val4=None,val5=None,val6=None):
    import sqlite3
    conn = sqlite3.connect('college.db', uri=True)
    c = conn.cursor()
    if val1!=None and val4!=None :
        conn.execute(f"insert into {tablename} values({val1},{val2},{val3},{val4});")
        print("Table inserted1")

    elif val1!=None and val6!=None:
        conn.execute(f"insert into {tablename} values({val1},{val2},{val3},{val4},{val5},{val6});")
        print("Table inserted3")
    else:
        print("no insert")
    conn.commit()
    conn.close()


# insertvalue('stud_assignment',3895,2,3,1,4)