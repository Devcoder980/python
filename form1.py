from tkinter import *
from tkinter.messagebox import *

def summit():
    a=e.get()
    a1=e1.get()
    a2=e2.get()
    a3=e3.get()
    a4=e4.get()
    # todo: Check Entry boxes are blank
    if a==''or a1=='' or a2=='' or a3=='' or a4=='':
        showinfo('Incomplete','Fill all Option')
    else:
        showinfo('Summit','Thank you for summit')

# todo:Deleter entere Boxes
def clear():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


root=Tk()
root.title('Contact No')
root.geometry('600x400')
root.configure(bg='#d5f4f2')
# root.maxsize(400,400)
root.eval('tk::PlaceWindow . center')
#todo:Label of from
l=Label(root,text='Contact Form',font=('times',20,'bold'),bd='5px',bg='#d5f4f2')
l1=Label(root,text='Your name : ',font=('times',15,'bold'),bg='#d5f4f2')
l2=Label(root,text='Your Email : ',font=('times',15,'bold'),bg='#d5f4f2')
l3=Label(root,text='Mobial No : ',font=('times',15,'bold'),bg='#d5f4f2')
l4=Label(root,text='Father name : ',font=('times',15,'bold'),bg='#d5f4f2')
l5=Label(root,text='Date of birth : ',font=('times',15,'bold'),bg='#d5f4f2')
#todo:l6=Label(root,text='Your Message : ',font=('times',15,'bold'),bd='5px')
#e5 todo:=Entry(font=('times',15),bd='2px',width=40)
#Main for Entry
e=Entry(font=('times',15),bd='2px')
e1=Entry(font=('times',15),bd='2px')
e2=Entry(font=('times',15),bd='2px')
e3=Entry(font=('times',15),bd='2px')
e4=Entry(font=('times',15),bd='2px')

#todo:buttons
b=Button(text='Summit',font='ar 10',width=10,bd='3px',bg='#bfdcea',command=summit)
b1=Button(text='clear',font='ar 10',width=10,bd='3px',bg='#bfdcea',command=clear)
b.place(x=270,y=250)
b1.place(x=170,y=250)
#todo:place control for entry boxes
e.place(x=160,y=50)
e1.place(x=160,y=90)
e2.place(x=160,y=130)
e3.place(x=160,y=170)
e4.place(x=160,y=210)
#e5.place(x=160,y=250)

#label place control of Label
l.place(x=110,y=0)
l1.place(x=30,y=50)
l2.place(x=30,y=90)
l3.place(x=30,y=130)
l4.place(x=30,y=170)
l5.place(x=30,y=210)
#l6.place(x=30,y=250)

root.mainloop()