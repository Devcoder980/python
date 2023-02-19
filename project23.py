# from tkinter import *
# import time
# root=Tk()
# root.title('Clock')
# root.maxsize(396,80)
# root.minsize(396,80)
#
# def time_curent():
#     a=time.strftime("%I:%M:%S %p")
#     root_display.config(text=a)
#     root_display.after(200,time_curent)
#
# root_display=Label(root,font=('arial',50,'bold'),bg='green',fg='red')
#
# root_display.pack()
# time_curent()
# root.mainloop()
count=0
a=0
n=int(input("enter numbe"))
for i in range(n):
    a=i*i
    for i in range(i):
        a=a+a
        count=count+1


print(count)