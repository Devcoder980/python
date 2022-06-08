from tkinter import *
from tkinter.messagebox import *
def sum():
    r=''
    r=int(e.get())
    if r=='':
        showinfo('messae','Enter the value')
    else:
        t=r*r
        l2.configure(bg='#209f49',text='Area of circle: {:.1f}'.format(t))


root=Tk()
root.title('Calculate')
root.geometry('280x220')
root.configure(bg='white')

l1=Label(text='Enter the radius of circle',font='times 20')
l2=Label(font='times 20')
e=Entry(width=15,bd='5px',font='times 20',bg='#6ec1ff')
b3=Button(root,text='Ok',width=10,font=('times',15,'bold'),bd='3px',bg='#6ec1ff',command=sum)

l2.grid(row=4,column=0)
b3.grid(row=2,column=0)
l1.grid(row=0,column=0)
e.grid(row=1,column=0)
root.mainloop()