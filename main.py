# import sqlite3
# conn=sqlite3.connect('parent.db')
# c=conn.cursor()
# c.execute('''create table stocks
#             (date text,trans text,symbole text,qty real,price real)''')
# c.execute("insert into stocks values('12-23-2002','byy','rhat',34.6,67.9)")
# conn.commit()
# conn.close()
from tkinter import *

sv = Tk()
sv.geometry("500x300")


def submit():
    print('Accepted')
    na = name.get()
    Em = Email.get()
    Ph = Phone.get()
    ad = Address.get()
    ge = gender.get()
    display = Entry( width=300, font='ar 15').pack()

def newOpen():
    sb = Tk()
    sb.geometry("500x300")

    # display.insert(0, f'{na} {Em}{Ph}{ad}{ge}.')


name = Entry(sv)
Email = Entry(sv)
Phone = Entry(sv)
Address = Entry(sv)
gender = Entry(sv)

n = Label(sv, text='Enter your name', font='ar 15 ').pack()
e = Label(n, text='Email', font='ar 15').pack, Email.pack()
p = Label(sv, text='Phone no.', font='ar 15').pack(), Phone.pack()
a = Label(sv, text='Address', font='ar 15').pack(), Address.pack()
g = Label(sv, text='Gender', font='ar 15').pack(), gender.pack()
sub = Button(sv, text="Submit", font="ar 15", command=submit()).pack()
btn = Button(sv, text="Show detail", command=newOpen()).pack()

sv.mainloop()
