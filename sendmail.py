##OTP Validation
from tkinter import *
import os,math
import random,sys
mailid=sys.argv[1]
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg="Your OTP Verification for app is"+OTP
f2=open("otp.txt","w")
f2.write(OTP)
f2.close()
wn=Tk()
wn.geometry("400x200")
wn.title("Verification Screen")
wn.configure(bg="cyan")
label1=Label(wn,text="OTP",relief="solid",font=("times",15),fg="black",bg="light pink").pack(fill=BOTH)
re1=Label(wn,text="{"+str(OTP)+"}",font=("times",25),bg="cyan").place(x=130,y=70)
print(OTP)
import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("mea@gmail.com","wodyrl")#emailid,apppassword
print(msg)
s.sendmail("mea@gmail.com",mailid,msg)
wn.mainloop()
os.system(r"C:\Users\Friends\AppData\Local\Programs\Python\Python310\second.py")#change path acc. to required
