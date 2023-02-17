from tkinter import *
from tkinter.messagebox import *

def summit():
    a=e.get()
    a1=e1.get()
    a2=e2.get()
    a3=e3.get()
    a4=e4.get()
    if a==''and a1=='' and a2=='' and a3=='' and a4=='':
        showinfo('summit','Fill all Option')
    else:
        showinfo('Summit','Thank you for summit')
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


root=Tk()
root.title('Contact No')
root.geometry('400x400')
root.eval('tk::PlaceWindow . center')
l=Label(root,text='Contact Form',font=('times',25,'bold'),bd='5px')
l1=Label(root,text='Your name : ',font=('times',15,'bold'))
l2=Label(root,text='Your Email : ',font=('times',15,'bold'))
l3=Label(root,text='Mobial No : ',font=('times',15,'bold'))
l4=Label(root,text='Father name : ',font=('times',15,'bold'))
l5=Label(root,text='Date of birth : ',font=('times',15,'bold'))

e=Entry(font=('times',15),bd='2px')
e1=Entry(font=('times',15),bd='2px')
e2=Entry(font=('times',15),bd='2px')
e3=Entry(font=('times',15),bd='2px')
e4=Entry(font=('times',15),bd='2px')

b=Button(text='Summit',font='times 15',bd='3px',bg='#bfdcea',command=summit)
b.place(x=160,y=250)

e.place(x=160,y=50)
e1.place(x=160,y=90)
e2.place(x=160,y=130)
e3.place(x=160,y=170)
e4.place(x=160,y=210)

l.place(x=110,y=0)
l1.place(x=30,y=50)
l2.place(x=30,y=90)
l3.place(x=30,y=130)
l4.place(x=30,y=170)
l5.place(x=30,y=210)

root.mainloop()