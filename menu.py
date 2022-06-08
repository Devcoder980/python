import tkinter
from tkinter import *
root=Tk()
root.title("Menu")
t1=300
t2=300
root.geometry(f"{t1}x{t2}")

def mydef():
    print("hello prabhu")


t_menu=Menu(root)
t_root = Menu(t_menu,tearoff=0)
t_root.add_command(label="New project",command=mydef)
t_root.add_command(label="save",command=mydef)
t_root.add_command(label="save as",command=mydef)
t_root.add_command(label="print",command=mydef)
t_root.add_command(label="exit",command=quit)
root.config(menu=t_menu)
t_menu.add_cascade(label="file",menu=t_root)

t_root1 = Menu(t_menu,tearoff=0)
t_root1.add_command(label="cut",command=mydef)
t_root1.add_command(label="insert",command=mydef)
t_root1.add_command(label="paste",command=mydef)
t_root1.add_command(label="copy",command=mydef)
t_root1.add_command(label="exit",command=quit)
root.config(menu=t_menu)
t_menu.add_cascade(label="edit",menu=t_root1)


t_root1 = Menu(t_menu,tearoff=0)
t_root1.add_command(label="Feedback",command=mydef)
t_root1.add_command(label="help",command=mydef)
root.config(menu=t_menu)
t_menu.add_cascade(label="help",menu=t_root1)
root.mainloop()
tkinter.Label