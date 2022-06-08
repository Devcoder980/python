from tkinter import *
#calculate area of tringle
def area():
    b=int(e.get())
    h=int(e1.get())
    a=0.5*b*h
    l4.configure(bg='#fffc88',text='Area of tringle: {:.1f}'.format(a))
#main root
root=Tk()
root.title('Area of tringel')
root.geometry('320x320')

#Labels
l1=Label(text='Enter the base and height',font='times 15')
t=Label(text='Calculate Area of Tringle',font=('times', 20,'bold'))
l2=Label(text='Base :',font='times 15')
l3=Label(text='height :',font='times 15')
l4=Label(font=('times',20,'bold'),bd='3px')
#Input the values
e=Entry(width=15,font='times',bd='3px')
e1=Entry(width=15,font='times',bd='3px')
#buttons
b=Button(font=('times',15,'bold'),text='Calculate',bd='5px',command=area)
b.place(x=120,y=140)
e.place(x=100,y=70)
e1.place(x=100,y=100)
l2.place(x=30,y=70)
l3.place(x=30,y=100)
l4.place(x=30,y=220)
l1.grid(row=1,column=0)
t.grid(row=0,column=0)
root.mainloop()