from tkinter import *
from tkinter import messagebox
def sum():
    a = int(t1.get())
    c=a*a
    t4.configure(text='converted : {:.1f}'.format(c))
    t1.delete(0,END)
root = Tk()
root.maxsize(300,600)
root.title('Calculater')
root.geometry('320x280')
t3 = Label( text='Enter the number for calculate square',font='vardana 14')
t4=Label(font="vardana 20")
t1 = Entry( bd='5px', bg="white", font="80")
t2 = Button(text="OK", font="bold", bd="3px", command=sum)

t3.grid(column=0, row=0)
t1.grid(column=0, row=1)
t2.grid(column=0, row=2)
t4.grid(column=0,row=4)

root.mainloop()
