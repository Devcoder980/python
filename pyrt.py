from tkinter import *

def sum():
    a=int(t3.get())
    b=int(t4.get())
    c=a+b
    t.configure(text='Total Sum : {:.1f} '.format(c))
  #  t3.delete(0,END)
  #  t4.delete(0,END)
def add():
    a=int(t3.get())
    b=int(t4.get())
    if a=='' or b=='':
        ta.confiqure(text='enter the value')
    else:
        c=a*b
    ta.configure(text='Addition : {:.1f} '.format(c))
   # t3.delete(0,END)
   # t4.delete(0,END)
def sub():
    a=int(t3.get())
    b=int(t4.get())
    c=a-b
    tb.configure(text='Subtraction : {:.1f} '.format(c))
   # t3.delete(0,END)
   # t4.delete(0,END)
root =Tk()
root.title('Calculate')
root.geometry('300x300')
root.maxsize(300,300)
tt=PhotoImage(file='C:/Users/shivani/Dropbox/PC/Desktop/yyy.png')
label=Label(root,image=tt)
#label.pack(pady=200)
#label
t1=Label(text="Number 1",font='Algerian 15')
t2=Label(text="Number 2",font='Algerian 15')
t=Label(font='Algerian 10',bg='aqua')#sum
ta=Label(font='Algerian 10',bg='yellow')#add
tb=Label(font='Algerian 10',bg='white')#sub
#entry
t3=Entry(bd='3px',font='Algerian 10',width=14)
t4=Entry(bd='3px',font='Algerian 10',width=14)
#button
t5=Button(root,text='      Sum      ',bd='4px',bg='white',command=sum)
t6=Button(root,text='  addition  ',bd='4px',bg='white',command=add)
t7=Button(root,text='subtraction',bd='4px',bg='white',command=sub)

#grids
t.grid(row=4,column=80)
ta.grid(row=5,column=80)
tb.grid(row=6,column=80)

#output grid
t5.grid(row=4,column=30)
t6.grid(row=5,column=30)
t7.grid(row=6,column=30)

t4.place(x=160,y=25)
t3.grid(row=2,column=30)

root.mainloop()
