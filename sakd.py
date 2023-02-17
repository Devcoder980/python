from tkinter import *
sv = Tk()
sv.geometry("500x300")

def submit():
    print('Accepted')

def newOpen():
    sb =Tk()
    sb.geometry("500x300")
    dis_if=Entry(sb,)
    na =n.get()
    Em =e.get()
    Ph =p.get()
    ad =a.get()
    ge =g.get()



Label(sv, Text='Demo Registration form',font='ar 15 bold')
name =Entry(sv)
Email = Entry(sv)
Phone = Entry(sv)
Address = Entry(sv)
gender =Entry(sv)

n =Label(sv,text='Enter your name', font='ar 15 ').pack(), name.pack()
e = Label(sv,text='Email', font='ar 15').pack(), Email.pack()
p = Label(sv,text='Phone no.', font='ar 15').pack(), Phone.pack()
a = Label(sv,text='Address', font='ar 15').pack(), Address.pack()
g = Label(sv,text='Gender', font='ar 15').pack(), gender.pack()
sub = Button(sv,text="Submit", font="ar 15", command=submit)
btn=Button(sv, text="Show detail", command=newOpen).pack()

