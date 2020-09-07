from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3




''''
db=sqlite3.connect("tic-tac-toe.db")
cr=db.cursor()
cr.execute("create table history (Name text,Result text)")
db.commit()
db.close()


print("Create")
'''







root=Tk()
root.geometry("650x800")
root.resizable(0,0)
root.title("Tic Tac Toe ")

c=1

        

def login():
    f2=Frame()
    f2.place(x=0,y=0,width=650,height=800)

    x=StringVar()
    y=StringVar()
    z=StringVar()


    def show1():
        b1["text"]=""
        b2["text"]=""
        b3["text"]=""
        b4["text"]=""
        b5["text"]=""
        b6["text"]=""
        b7["text"]=""
        b8["text"]=""
        b9["text"]=""
        y.set("")
        z.set("")
        x.set("")
        global c
        c=1
    
    
    def show(b):
        global c
        c=c+1
        if(c%2==0 and b["text"]==""):
            b["text"]="0"
            b["fg"]="red"
            
        if(c%2!=0 and b["text"]==""):
            b["text"]="x"
            b["fg"]="blue"
            

        if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0" or
            b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0" or
            b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0" or
            b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0" or
            b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0" or
            b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0" or
            b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0" or
            b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0" ):
             
             a=y.get()
             x.set(a)
             messagebox.showinfo("Mesage Box"," Player - 1 is Winner  !!!!")
             db=sqlite3.connect("tic-tac-toe.db")
             cr=db.cursor()
             cr.execute("insert into history (Name,Result) VALUES ('"+y.get()+"','Winner')")
             db.commit()
             db.close()
        
        if(b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x" or
            b4["text"]=="x" and b5["text"]=="x" and b6["text"]=="x" or
            b7["text"]=="x" and b8["text"]=="x" and b9["text"]=="x" or
            b1["text"]=="x" and b4["text"]=="x" and b7["text"]=="x" or
            b2["text"]=="x" and b5["text"]=="x" and b8["text"]=="x" or
            b3["text"]=="x" and b6["text"]=="x" and b9["text"]=="x" or
            b1["text"]=="x" and b5["text"]=="x" and b9["text"]=="x" or
            b3["text"]=="x" and b5["text"]=="x" and b7["text"]=="x" ):
             b=z.get()
             x.set(b)
             
             messagebox.showinfo("Message Box"," Player - 2 is Winner !!!!")
             db=sqlite3.connect("tic-tac-toe.db")
             cr=db.cursor()
             cr.execute("insert into history (Name,Result) VALUES ('"+z.get()+"','Winner')")
             db.commit()
             db.close()

       
            



        

    l=Label(f2,text="Player - 1 ",font=("Algerian",20))
    l.grid(row=0,column=0)

    e1=Entry(f2,font=("Arial",15),width=18,textvariable=y,fg="red",bd=16,bg="powder blue")
    e1.grid(row=0,column=1)

    l2=Label(f2,text=" -   0",font=("Algerian",40),fg="red")
    l2.grid(row=0,column=2)
    
    l1=Label(f2,text="Player - 2 ",font=("Algerian",20))
    l1.grid(row=1,column=0)

    e2=Entry(f2,font=("Arial",15),width=18,textvariable=z,fg="blue",bd=16,bg="powder blue")
    e2.grid(row=1,column=1)

    l3=Label(f2,text=" -   x",font=("Algerian",40),fg="blue")
    l3.grid(row=1,column=2)

    b1=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b1))
    b1.grid(row=2,column=0)

    b2=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b2))
    b2.grid(row=2,column=1)

    b3=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b3))
    b3.grid(row=2,column=2)


    b4=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b4))
    b4.grid(row=3,column=0)

    b5=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b5))
    b5.grid(row=3,column=1)

    b6=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b6))
    b6.grid(row=3,column=2)


    b7=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b7))
    b7.grid(row=4,column=0)

    b8=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b8))
    b8.grid(row=4,column=1)

    b9=Button(f2,text="",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=lambda :show(b9))
    b9.grid(row=4,column=2)

    l4=Label(f2,text="Winner -  ",font=("Algerian",20))
    l4.grid(row=5,column=0)

    e1=Entry(f2,font=("Arial",15),width=18,textvariable=x,fg="red",bd=16,bg="powder blue")
    e1.grid(row=5,column=1)

    b10=Button(f2,text="Reset",width=15,height=5,font=("Arial"),bd=10,bg="powder blue",command=show1)
    b10.grid(row=6,column=1)


    b11=Button(f2,text="Home",font="Arial",width=15,height=5,bd=10,bg="powder blue",command=home)
    b11.grid(row=6,column=2)

count=0
st=''


def home():
    f1=Frame(background="cadet blue")
    f1.place(width=650,height=800)
    def his():
        
        f6=Frame(f1,background="dark blue",bd=15,relief=RIDGE)
        f6.grid(row=2,column=0,padx=10,pady=20)
        la=Label(f6,text="Last 5 Match Winner ",bg="white",font=("Arial",15))
        la.pack()

        f7=Frame(f1,background="dark blue",bd=15,relief=RIDGE)
        f7.grid(row=3,column=0,padx=10,pady=20)

        db=sqlite3.connect("tic-tac-toe.db")
        cr=db.cursor()
        r=cr.execute("select * from history")

        x=0
        y=0
        
        for i in r:    
            Label(f7,text=i[0],font=("Arial",15)).grid(row=x,column=y,pady=5)
            y=y+1
            Label(f7,text=i[1],font=("Arial",15)).grid(row=x,column=y)
            x=x+1
            y=0
           
            
       
            
        db.commit()
        db.close()




    def delete():
        db=sqlite3.connect("tic-tac-toe.db")
        cr=db.cursor()
        cr.execute("delete from history")
        db.commit()
        db.close()
        




    #c=0
    #st=''


    def display():
        global count,st
        if(count>=len(s)):
            l1["text"]=""
            count=0
            st=""
        else:
            st=st+s[count]
            l1["text"]=st
            count=count+1
        l1.after(400,display)

        
    s="Tic - Tac - Toe  Game"
    
    f4=Frame(f1,background="dark blue",bd=15,relief=RIDGE)
    f4.grid(row=0,column=0,padx=30,pady=10)
    l1=Label(f4,text=s,font=("Algerian",40),bg="powder blue")
    l1.pack()
    f5=Frame(f1,background="dark blue",bd=15,relief=RIDGE)
    f5.grid(row=1,column=0,padx=10,pady=20)
    b1=Button(f5,text="Start",font=("Arial",20),bg="powder blue",bd=10,command=login)
    b1.grid(row=0,column=0,padx=10)
    b2=Button(f5,text="Quit",font=("Arial",20),bg="powder blue",bd=10,command=root.destroy)
    b2.grid(row=0,column=1,padx=10)
    b3=Button(f5,text="History",font=("Arial",20),bg="powder blue",bd=10,command=his)
    b3.grid(row=0,column=2,padx=10)
    b4=Button(f5,text="Clear history",font=("Arial",20),bg="powder blue",bd=10,command=delete)
    b4.grid(row=0,column=3,padx=10)
    display()


    
    
   

home()




root.mainloop()





