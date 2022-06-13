##Generating,Storing and Sending OTP
import tkinter
from tkinter import *
from tkinter import messagebox
import time
import os
wn=Tk()
wn.geometry("800x400")
wn.title("Verification Screen")
wn.configure(bg="cyan")
count=3
def verify():
    global count
    global wn
    end=time.time()
    t=format(end-start)
    print(float(t))
    if float(t)>=120:
        meassagebox.showinfo("Time out","Session Expired  ...Time out Please regenerate OTP")
        wn.destroy()
    else:
        cmd1=str(a.get())
        os.system(r"C:\Users\Friends\AppData\Local\Programs\Python\Python310\verify.py"+" "+cmd1)
        ok="Invalid OTP: "+str((count-1))+" attempts remaining"
        count=count-1
        f1=open("status.txt","r")
        bh=f1.read()
        if count>=1 and bh!="success":
            tkinter.messagebox.askretrycancel("Error",ok)
            f1.close()
        elif count==0 and bh!="success":
            f=open("otp.txt","w")
            f.write("")
            f.close
            messagebox.showinfo("Your 3 attempts were over.Please regenerate the OTP")
            f1.close()
            wn.destroy()
        elif bh=="success":
            f1.close()
            wn.destroy()
start=time.time()
label1=Label(wn,text="Verification Screen",relief="solid",font=("times",15),fg="black",bg="light pink").pack(fill=BOTH)
a=StringVar()
Re=Label(wn,text="Enter the OTP",font=("arial",15,"bold"),bg="cyan").place(x=0,y=50)
w1=Entry(wn,borderwidth=7,width=26,textvariable=a)
w1.place(x=300,y=50)
re1=Label(wn,text="Please enter the  OTP within 1 minutes",font=("times",14),bg="cyan").place(x=250,y=100)
ver=Button(wn,text="Verify",relief="raised",bg="blue",font=("arial",15),fg="black",command=verify).place(x=500,y=150)
wn.mainloop()
