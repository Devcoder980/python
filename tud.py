from tkinter import *
from tkinter.messagebox import *
root=Tk()
def bonus():
    a=int(t1.get())
    if a>5000:
        print("You got bonus")
        showinfo("BONUS","you got bonus!")
        t1.delete(0,END)
    else:
        print("you not got bonus")
        showinfo("BONUS","you not got bonus")

root.geometry("300x400")
root.maxsize(300,300)
root.title("Calculate Bonus")
label=Label(root,text="Enter the salary:",font="Bahnschrift  15",bd="5px").pack()
t1=Entry(label,bd="5px",font="bahnschrift",width=22)

t1.pack()
t2=Button(label,text="Enter",font="bahnschrift  ",width=12,height=1,command=bonus)
t2.pack()


root.mainloop()