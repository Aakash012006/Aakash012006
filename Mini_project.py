import tkinter as tk
from tkinter import *

ad=Tk()
ad.title("Admission Checking")
ad.geometry('650x650')
ad.configure(bg="sky blue")
sample=StringVar()
num1=IntVar()
ans=StringVar()
def cl():
    a=sample.set("")
    b=num1.set("")
    v=ans.set("")

def vj():
    a=sample.get()
    b=num1.get()
    ans=Label(ad,text="""You Are Eligible for,
              AI&DS, AI&ML, CSBS, IT, CSE, ECE, EEE, BT 
              ⬆️ These Deparments
              """,font=('algerian',15,'bold'),bg='yellow').place(x=10,y=300)
    if(b== 200 or b >=180 ):
        
        Label(ad,text="""Fees per Year : 85,000
              """,font=('algerian',15,'bold')).place(x=10,y=400)
    elif(b == 179 or b >= 160):
      #   Label(ad,text="""You Are Eligible for,
      #         AI&DS, AI&ML, CSBS, IT, CSE, ECE, EEE, BT 
      #         ⬆️ These Deparments
      #         """,font=('algerian',15,'bold')).place(x=10,y=300)
        Label(ad,text="""Fees per Year : 1,00,000
              """,font=('algerian',15,'bold')).place(x=10,y=400)
    elif(b == 159 or b >= 140):
      #   Label(ad,text="""You Are Eligible for,
      #         AI&DS, AI&ML, CSBS, IT, CSE, ECE, EEE, BT 
      #         ⬆️ These Deparments
      #         """,font=('algerian',15,'bold')).place(x=10,y=300)
        Label(ad,text="""Fees per Year : 1,35,000
              """,font=('algerian',15,'bold')).place(x=10,y=400)
    elif(b == 139 or b >= 120):
      #   Label(ad,text="""You Are Eligible for,
      #         AI&DS, AI&ML, CSBS, IT, CSE, ECE, EEE, BT 
      #         ⬆️ These Deparments
      #         """,font=('algerian',15,'bold')).place(x=10,y=300)
        Label(ad,text="""Fees per Year : 1,60,000
              """,font=('algerian',15,'bold')).place(x=10,y=400)
    elif(b == 110 or b>=100):
      #   Label(ad,text="""You Are Eligible for,
      #         AI&DS, AI&ML, CSBS, IT, CSE, ECE, EEE, BT 
      #         ⬆️ These Deparments
      #         """,font=('algerian',15,'bold')).place(x=10,y=300)
        Label(ad,text="""Fees per Year : 1,85,000
              """,font=('algerian',15,'bold')).place(x=10,y=400)
    else:
        Label(ad,text="We Hope You Deserve a Better Collage than us",font=('algerian',15,'bold')).place(x=10,y=300)
    

Label(ad,text="Enter Your Name : ",font=('Arial',20,'bold'),bg='blue').place(x=10,y=10)
Label(ad,text="Enter Your 12th Cut off Mark :",font=('Arial',20,'bold'),bg='blue').place(x=10,y=120)
Label(ad,text="Eligible ⬇️",font=('Arial',20,'bold'),bg='blue').place(x=10,y=250)
Entry(ad,width=20,textvariable=sample,font=('Algerian',25),bg='white').place(x=10,y=60)
Entry(ad,width=20,textvariable=num1,font=('Algerian',25),bg='white').place(x=10,y=170)
# Label(ad,textvariable=ans,font=('arial',30,'bold'),bg='blue').place(x=10,y=300)
Button(ad,text='Check Eligiblity ',font=('algerian',15,'bold'),width=25,bg='orange',command=vj).place(x=250,y=500)
Button(ad,text='CLEAR ',font=('algerian',15,'bold'),width=25,bg='orange',command=cl).place(x=250,y=550)




ad.mainloop()