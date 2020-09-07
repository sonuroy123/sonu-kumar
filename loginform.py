from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3



'''
bd=sqlite3.connect("sonu1.db")
cr=bd.cursor()
cr.execute("create table Regis(NAME text,PASS text,USN text)")
bd.commit()
bd.close()
'''

'''
db=sqlite3.connect("sonu1.db")
cr=db.cursor()
cr.execute("create table mark (USN text,Name text,Physics text,Chemistry text,Math text,Biology text)")
db.commit()
db.close()
'''




root=Tk()
root.geometry("400x400")
root.configure(background="dark blue")
root.resizable (0,0)

f55=None

x=StringVar()
y=StringVar()
z=StringVar()
a=StringVar()
g=StringVar()

def login():
    f2=Frame(bg="dark blue")
    f2.place(x=0,y=0,width=400,height=400)

    l1=Label(f2,text="Enter Name  :-",font=("Arial",15))
    l1.place(x=20,y=30)
    e1=Entry(f2,font=("Arial",15),width=13,textvariable=a)
    e1.place(x=200,y=30)
    l2=Label(f2,text="Enter Pass   :-",font=("Arial",15))
    l2.place(x=20,y=70)
    e2=Entry(f2,font=("Arial",15),width=13,textvariable=g,show="*")
    e2.place(x=200,y=70)

    def login1():
         db=sqlite3.connect("sonu1.db")
         cr=db.cursor()
         r=cr.execute("select * from Regis where NAME='"+a.get()+"' AND  PASS='"+g.get()+"' ")
         for i in r:
             #messagebox.showinfo("Title","Welcome")
             menu()
             break
         else:
             messagebox.showinfo("Title","Invalid UserName or Pass")
             
         
         db.commit()
         db.close()
         a.set("")
         g.set("")
         e1.focus()
         
        
    b3=Button(f2,text="Login.",font=("Arial",15),bd=10,command=login1)
    b3.place(x=150,y=150)
    b4=Button(f2,text="Home",font=("Arial",15),bd=10,command=home)
    b4.place(x=20,y=330)
    b5=Button(f2,text="Regs.",font=("Arial",15),bd=10,command=regs)
    b5.place(x=300,y=330)


def menu():
    n=ttk.Notebook()
    n.place(x=0,y=0,width=400,height=400)
    def demo(a):
        if(n.index("current")==5):
            home()
    n.bind("<<NotebookTabChanged>>",demo)
    insert(n)
    show(n)
    search(n)
    update(n)
    delete(n)
    logout(n)

def insert(n):

    
    a=StringVar()
    b=StringVar()
    c=StringVar()
    d=StringVar()
    e=StringVar()
    f=StringVar()

    def ins():
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        cr.execute("insert into mark (USN,Name,Physics,Chemistry,Math,Biology) VALUES ('"+a.get()+"' , '"+b.get()+"' , '"+c.get()+"' , '"+d.get()+"' ,  '"+e.get()+"' , '"+f.get()+"' )")
        messagebox.showinfo("Title","Saved")
        db.commit()
        db.close()
        a.set("")
        e1.focus()
        b.set("")
        c.set("")
        d.set("")
        e.set("")
        f.set("")
        #show1(f55)
        



                 
    f4=Frame(bg="dark blue")
    n.add(f4,text="Insert")
    u1=Label(f4,text="Roll No :-",font=("Arial",15))
    u1.place(x=30,y=30)
    e1=Entry(f4,font=("Arial",15),textvariable=a)
    e1.place(x=150,y=30)
    u1=Label(f4,text="Name  :-",font=("Arial",15))
    u1.place(x=30,y=80)
    e2=Entry(f4,font=("Arial",15),textvariable=b)
    e2.place(x=150,y=80)
    u1=Label(f4,text="Physics :-",font=("Arial",15))
    u1.place(x=30,y=130)
    e3=Entry(f4,font=("Arial",15),textvariable=c)
    e3.place(x=150,y=130)
    u1=Label(f4,text="Chemistry:-",font=("Arial",15))
    u1.place(x=30,y=180)
    e4=Entry(f4,font=("Arial",15),textvariable=d)
    e4.place(x=150,y=180)
    u1=Label(f4,text="Math :-",font=("Arial",15))
    u1.place(x=30,y=230)
    e5=Entry(f4,font=("Arial",15),textvariable=e)
    e5.place(x=150,y=230)
    u1=Label(f4,text="Biology:-",font=("Arial",15))
    u1.place(x=30,y=280)
    e6=Entry(f4,font=("Arial",15),textvariable=f)
    e6.place(x=150,y=280)

    b1=Button(f4,text="Insert",font=("Arial",15),bd=10,bg="cadet blue",command=ins)
    b1.place(x=170,y=320)

    b2=Button(f4,text="<",font=("Arial",10),bg="white",command=home)
    b2.place(x=5,y=5)




def show(n):

    f5=Frame(bg="dark blue")
    n.add(f5,text="Show Data")
    #global f55
    #f55=f5
    #show(f5)


#def show1(f5):
    
    
    t=Text(f5,pady=20,width=400,height=400,bg="dark blue",fg="white",bd=4,font=("Arial",12))
    t.grid(row=0,column=0)

    t.delete("1.0",END)

    t.insert(END,"USN\tName\tPhy\tchem\tMath\tBio\n\n")
    

    
    
    db=sqlite3.connect("sonu1.db")
    cr=db.cursor()
    r=cr.execute("select * from mark")

    
    for i in r:
        t.insert(END,i[0]+"\t")
        t.insert(END,i[1]+"\t")
        t.insert(END,i[2]+"\t")
        t.insert(END,i[3]+"\t")
        t.insert(END,i[4]+"\t")
        t.insert(END,i[5]+"\n")
        
        
    

    db.commit()
    db.close()
        
    

def search(n):
    f6=Frame(bg="dark blue")
    n.add(f6,text="Search")

    l1=Label(f6,text="Enter USN  :-",font=("Arial",12),bg="dark blue",fg="white")
    l1.place(x=20,y=30)

    x=StringVar()
    
    e1=Entry(f6,font=("Arial",12),width=15,textvariable=x)
    e1.place(x=150,y=30)

   
    
    def search1():
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        r=cr.execute("select * from mark where USN='"+x.get()+"'")

        
        for i in r:
             Label(f6,text="USN is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=80)
             Label(f6,text=i[0],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=80)
             Label(f6,text="Name is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=120)
             Label(f6,text=i[1],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=120)
             Label(f6,text="Phy is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=160)
             Label(f6,text=i[2],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=160)
             Label(f6,text="chem is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=200)
             Label(f6,text=i[3],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=200)
             Label(f6,text="Math is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=240)
             Label(f6,text=i[4],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=240)
             Label(f6,text="Bio is :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=280)
             Label(f6,text=i[5],font=("Arial",10),bg="dark blue",fg="white").place(x=100,y=280)
             #x=x+60
             break
        else:
            messagebox.showinfo("Title","Invalid USN")
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=80,width=200)
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=120,width=200)
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=160,width=200)
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=200,width=200)
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=240,width=200)
            Label(f6,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=280,width=200)
            
            
        db.commit()
        db.close()
        x.set("")

    b5=Button(f6,text="Search",font=("Arial",10),bd=10,command=search1)
    b5.place(x=320,y=25)



def update(n):
    f7=Frame(bg="dark blue")
    n.add(f7,text="Update")

    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()
    s6=StringVar()


    l1=Label(f7,text="Enter USN : -",font=("Arial",12),bg="dark blue",fg="white")
    l1.place(x=10,y=20)
    e7=Entry(f7,font=("Arial",12),textvariable=s1,width=10)
    e7.place(x=150,y=20)


    
    
    def search1():
        
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        r=cr.execute("select * from mark where USN='"+s1.get()+"'")

        
        for i in r:
             
            
             l2=Label(f7,text="Name  :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=120)
             e2=Entry(f7,text=i[1],font=("Arial",10),bg="dark blue",fg="white",textvariable=s2)
             e2.insert(0,i[1])
             e2.place(x=100,y=120)
             l3=Label(f7,text="Phy  :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=160)
             e3=Entry(f7,text=i[2],font=("Arial",10),bg="dark blue",fg="white",textvariable=s3)
             e3.insert(0,i[2])
             e3.place(x=100,y=160)
             l4=Label(f7,text="Chem  :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=200)
             e4=Entry(f7,text=i[3],font=("Arial",10),bg="dark blue",fg="white",textvariable=s4)
             e4.insert(0,i[3])
             e4.place(x=100,y=200)
             l5=Label(f7,text="Math  :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=240)
             e5=Entry(f7,text=i[4],font=("Arial",10),bg="dark blue",fg="white",textvariable=s5)
             e5.insert(0,i[4])
             e5.place(x=100,y=240)
             l6=Label(f7,text="Bio  :-",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=280)
             e6=Entry(f7,text=i[5],font=("Arial",10),bg="dark blue",fg="white",textvariable=s6)
             e6.insert(0,i[5])
             e6.place(x=100,y=280)
             

                          
             break
        else:
            messagebox.showinfo("Title","Invalid USN")
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=80,width=200)
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=120,width=200)
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=160,width=200)
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=200,width=200)
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=240,width=200)
            Label(f7,text="",font=("Arial",10),bg="dark blue",fg="white").place(x=30,y=280,width=200)
            
            
        db.commit()
        db.close()
        x.set("")


    def update2():
        
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        cr.execute("update mark set Name='"+s2.get()+"', Physics='"+s3.get()+"',Chemistry='"+s4.get()+"', Math='"+s5.get()+"',Biology='"+s6.get()+"' where USN='"+s1.get()+"'")
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        s6.set("")
        #show1(f55)
        
        db.commit()
        db.close()
        

    b5=Button(f7,text="Updates",font=("Arial",10),bd=10,bg="powder blue",command=update2)
    b5.place(x=150,y=330)
    b5=Button(f7,text="Search",font=("Arial",10),bd=10,command=search1,bg="powder blue",height=1)
    b5.place(x=300,y=10)


    
    

    '''def up():

    
        
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        cr.execute("update mark set Name='"+w.get()+"', Physics='"+f.get()+"',Chemistry='"+g.get()+"', Math='"+j.get()+"',Biology='"+h.get()+"' where USN='"+x.get()+"'")
        db.commit()
        db.close()
        

    l1=Label(f7,text="Enter USN : -",font=("Arial",12),bg="dark blue",fg="white")
    l1.place(x=10,y=20)
    e7=Entry(f7,font=("Arial",12),textvariable=x)
    e7.place(x=150,y=20)

    
    u1=Label(f7,text="Name  :-",font=("Arial",12),bg="dark blue",fg="white")
    u1.place(x=10,y=80)
    e2=Entry(f7,font=("Arial",12),textvariable=w)
    e2.place(x=150,y=80)
    u1=Label(f7,text="Physics :-",font=("Arial",12),bg="dark blue",fg="white")
    u1.place(x=10,y=110)
    e3=Entry(f7,font=("Arial",12),textvariable=f)
    e3.place(x=150,y=110)
    u1=Label(f7,text="Chemistry:-",font=("Arial",12),bg="dark blue",fg="white")
    u1.place(x=10,y=140)
    e4=Entry(f7,font=("Arial",12),textvariable=g)
    e4.place(x=150,y=140)
    u1=Label(f7,text="Math :-",font=("Arial",12),bg="dark blue",fg="white")
    u1.place(x=10,y=170)
    e5=Entry(f7,font=("Arial",12),textvariable=j)
    e5.place(x=150,y=170)
    u1=Label(f7,text="Biology:-",font=("Arial",12),bg="dark blue",fg="white")
    u1.place(x=10,y=200)
    e6=Entry(f7,font=("Arial",12),textvariable=h)
    e6.place(x=150,y=200)

    b1=Button(f7,text="Update",font=("Arial",15),bd=10,bg="cadet blue",command=up)
    b1.place(x=130,y=270)'''
    


def delete(n):
    f8=Frame(bg="dark blue")
    n.add(f8,text="Delete")

    d1=StringVar()

    def delete1():
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        cr.execute("delete from mark where USN='"+d1.get()+"'")
        db.commit()
        db.close()
        d1.set("")
        messagebox.showinfo("Title","User Deleted")
        
        
    
    l1=Label(f8,text="Enter USN : -",font=("Arial",12),bg="dark blue",fg="white")
    l1.place(x=10,y=20)
    e7=Entry(f8,font=("Arial",12),width=10,textvariable=d1)
    e7.place(x=150,y=20)

    b5=Button(f8,text="Delete",command=delete1,font=("Arial",10),bd=10,bg="powder blue",height=1)
    b5.place(x=300,y=10)

def logout(n):
    f9=Frame(bg="blue")
    n.add(f9,text="Logout")




    
def regs():
    
    f3=Frame(bg="dark blue")
    f3.place(x=0,y=0,width=400,height=400)
    l1=Label(f3,text="Enter Name  :-",font=("Arial",15))
    l1.place(x=20,y=30)
    e1=Entry(f3,font=("Arial",15),width=13,textvariable=x)
    e1.place(x=200,y=30)
    l2=Label(f3,text="Enter Pass   :-",font=("Arial",15))
    l2.place(x=20,y=70)
    e2=Entry(f3,font=("Arial",15),width=13,textvariable=y)
    e2.place(x=200,y=70)
    l3=Label(f3,text="Enter USN   :-",font=("Arial",15))
    l3.place(x=20,y=110)
    e3=Entry(f3,font=("Arial",15),width=13,textvariable=z)
    e3.place(x=200,y=110)

    def regis1():
        if(x.get()=="" or y.get=="" or z.get()==""):
            messagebox.showinfo("Title","Enter Valid User Name")
            return
        else:
            db=sqlite3.connect("sonu1.db")
            cr=db.cursor()
            cr.execute("insert into Regis(NAME ,PASS ,USN ) VALUES ('"+x.get()+"','"+y.get()+"','"+z.get()+"')")
            db.commit()
            db.close()
            messagebox.showinfo("Title","Register Succesfully")
            x.set("")
            y.set("")
            z.set("")
            e1.focus()
        
    b3=Button(f3,text="Regis1",font=("Arial",15),bd=10,command=regis1)
    b3.place(x=150,y=180)
    b4=Button(f3,text="Home",font=("Arial",15),bd=10,command=home)
    b4.place(x=20,y=330)
    b5=Button(f3,text="Login.",font=("Arial",15),bd=10,command=login)
    b5.place(x=300,y=330)
    
def password():
    f6=Frame(bg="dark blue")
    f6.place(x=0,y=0,width=400,height=400)

    x1=StringVar()
    x2=StringVar()
    x3=StringVar()

    def change():
        db=sqlite3.connect("sonu1.db")
        cr=db.cursor()
        cr.execute("update Regis set NAME='"+x1.get()+"',PASS='"+x3.get()+"'  where PASS='"+x2.get()+"'")
        db.commit()
        db.close()
        x1.set("")
        x2.set("")
        x3.set("")
        messagebox.showinfo("Title","Password  Changed Succesfuly")
        home()
        

    l1=Label(f6,text="Enter Name  :-",font=("Arial",15),bg="dark blue",fg="white")
    l1.place(x=20,y=30)
    e1=Entry(f6,font=("Arial",15),width=13,textvariable=x1)
    e1.place(x=200,y=30)
    l2=Label(f6,text="Enter Pass   :-",font=("Arial",15),bg="dark blue",fg="white")
    l2.place(x=20,y=70)
    e2=Entry(f6,font=("Arial",15),width=13,show="*",textvariable=x2)
    e2.place(x=200,y=70)
    l3=Label(f6,text="Enter New Pass   :-",font=("Arial",15),bg="dark blue",fg="white")
    l3.place(x=20,y=110)
    e3=Entry(f6,font=("Arial",15),width=13,show="*",textvariable=x3)
    e3.place(x=200,y=110)
    b1=Button(f6,text="Change",font=("Arial",15),bd=10,command=change)
    b1.place(x=150,y=170)
    

    
def home():
    f1=Frame(bg="dark blue")
    f1.place(x=0,y=0,width=400,height=400)
    b1=Button(f1,text="Login",font=("Arial",15),bd=10,command=login)
    b1.place(x=100,y=50)
    b2=Button(f1,text="Regs.",font=("Arial",15),bd=10,command=regs)
    b2.place(x=190,y=50)
    b3=Button(f1,text="Change Password",font=("Arial",13),bd=10,command=password)
    b3.place(x=130,y=150)
    b4=Button(f1,text="Exit",font=("Arial",15),bd=10,command=root.destroy)
    b4.place(x=290,y=50)


home()




root.mainloop()

