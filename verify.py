from tkinter import messagebox
from tkinter import *
import time
import sys
b=sys.argv[1]
print(b)
f1=open("otp.txt","r")
b1=f1.read()
f1.close()
if b==b1:
    f=open("status.txt","w")
    f.write("success")
    f.close
    wn=Tk()
    wn.geometry("300x200")
    wn.configure(bg="black")
    wn.title("Success")
    l=Label(wn,text="Success",font=("times",30,"italic"),fg="red",bg="black").place(x=50,y=50)
    wn.mainloop()
else:
    f=open("status.txt","w")
    f.write("failure")
    f.close
