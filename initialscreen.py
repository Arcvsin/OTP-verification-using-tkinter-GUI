##Email Input Screen
import os
from tkinter import  *
wn=Tk()
wn.geometry("1000x600")
wn.title("OTP Verification")
wn.configure(bg="cyan")
def verify():
    c=str(a.get())
    os.system(r"C:\Users\Friends\AppData\Local\Programs\Python\Python310\sendmail.py"+" "+c)
label=Label(wn,text="OTP Verification",relief="solid",font=("Times New Roman",30),fg="black",bg="light pink").pack(fill=BOTH)
a=StringVar()
Re=Label(wn,text="EMAIL ID :-",font=("Times New Roman",25,"italic"),bg="cyan").place(x=200,y=70)
w=Entry(wn,borderwidth=7,width=26,validate="key",textvariable=a)
w.place(x=500,y=90)
log=Button(wn,text="Proceed",relief="ridge",bg="black",font=("red",23),fg="light blue",command=verify).place(x=700,y=250)
wn.mainloop()
