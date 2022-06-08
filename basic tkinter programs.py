# create a first gui window
from tkinter import *
window=Tk()
window.mainloop()

# create a first progrma print hello world
from tkinter import *
window=Tk()
window.title('First progrma')
a=Label(text='Hello World').pack()
window.mainloop()

# create a first place the location of hello world
# use of pack
from tkinter import *
window=Tk()
window.title('First progrma')
a=Label(text='Hello World')
a.pack()
window.mainloop()


# create a first place the location of hello world
# use of grid
from tkinter import *

window = Tk()
window.title('First progrma')
a = Label(text='Hello World')
a.grid(row=3, column=10)
window.mainloop()

# create a first place the location of hello world
# use of place
from tkinter import *

window = Tk()
window.title('First progrma')
a = Label(text='Hello World')
a.place(x=20,y=30)
window.mainloop()


# create a first progrma print display window size
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
window.mainloop()

# crate first button button
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
a=Button(text='Summit').pack()
window.mainloop()

# create a first progrma font in color
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
a=Label(text='Hello World',font='times 20',fg='red',bg='aqua').pack()
window.mainloop()

# create a first progrma button width and height
bd=border
fg=font color
bg=baground
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
a=Button(text='Summit',width=20,height=2).pack()
window.mainloop()

# create a first progrma button width and height
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
a=Button(text='Summit',font=('times',20,'bold'),bd='10px',width=15,height=2).pack()
window.mainloop()

# create a first progrma button baground color
from tkinter import *
window=Tk()
window.geometry('300x300')
window.title('First progrma')
a=Button(text='Summit',font=('times',20,'bold'),bg='#499fe0',width=15).pack()
window.mainloop()

# create a form with use of tkinter mofule
from tkinter import *
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

b=Button(text='Summit',font='times 15',bd='3px',bg='#bfdcea')
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
