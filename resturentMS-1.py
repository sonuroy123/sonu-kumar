from tkinter import*
import time as tm
import datetime
import tkinter.messagebox
from tkinter import BOTH , LEFT , FLAT , RIDGE 


'''
root=Tk()
root.geometry("400x400")
root.configure(background="darkblue")

def login():
    f2=Frame()                                      # Setting Second Frame 
    f2.place(x=0,y=0,width=400,height=400)
    e1=Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b2=Button(f2,text="LogIn  !!!!")
    b2.pack()
    

f1=Frame()                                                 # Setting First frame
f1.place(x=0,y=0,width=400,height=400)
f1.configure(background="darkblue")

b1=Button(f1, text="Click  !!!!",font=("Algerian",20),command=login)
b1.pack()
'''
'''
root=Tk()
r=Tk()
root.geometry("400x400")
r.geometry("400x400")

def show():
    e=Entry(r,font=("Arial",20))
    e.pack()
b=Button(root,text="Click",font=("Arial",20),command=show)
b.pack()
root.mainloop()
r.mainloop()
'''







root=Tk()
root.geometry("1350x750")
root.title("Restaurent Management System")
root.configure(background="cadet blue")

def window():
    
    #fmain=Frame(root,bg="cadet blue")
    #fmain.pack()


    fmain=Frame(root)                                                 # Setting First frame
    fmain.place(x=0,y=0,width=1550,height=850)
    fmain.configure(background="cadet blue")
    
    f1=Frame(fmain,bg="cadet blue",bd=20,pady=5 ,relief=RIDGE)   # Top Frame  , relief is boarder styl method , RIDGE is one styl
    f1.pack(side=TOP)


    l1=Label(f1,font=("Algerian",60),bg="cadet blue",text="Restaurent Management System",bd=20,fg="cornsilk",justify=CENTER)
    l1.grid(row=0,column=0)





    #============================================================================



    f3=Frame(fmain,bg="powder blue",bd=10,relief=RIDGE)  # Receipt Claculator Frame on Right side
    f3.pack(side=RIGHT)

    f4=Frame(f3,bg="powder blue",bd=3,relief=RIDGE)    # Button frame on Receipt calculator Frame
    f4.pack(side=BOTTOM)

    f5=Frame(f3,bg="powder blue",bd=6,relief=RIDGE)    # Calculator Frame On Receipt calculator frame
    f5.pack(side=TOP)

    f6=Frame(f3,bg="powder blue",bd=4,relief=RIDGE)    # Receipt frame on Receipt calculator farme
    f6.pack(side=BOTTOM)


    #==================================================================================


    f2=Frame(fmain,bg="cadet blue",bd=20,relief=RIDGE)  # Menue Frame on Left side
    f2.pack(side=LEFT)

    f7=Frame(f2,bg="powder blue",bd=4,relief=RIDGE)    # Cost frame on Menue frame
    f7.pack(side=BOTTOM)

    f9=Frame(f2,bg="powder blue",bd=4,relief=RIDGE)    # Drinks frame on Menue frame
    f9.pack(side=TOP)

    f8=Frame(f2,bg="powder blue",bd=4,relief=RIDGE)    # Drinks frame on Menue frame
    f8.pack(side=LEFT)

    f10=Frame(f2,bg="powder blue",bd=4,relief=RIDGE)    # Chicken frame on Menue frame
    f10.pack(side=RIGHT)


    #=======================================Variable=============================================================================================


    v0=IntVar()
    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
    v4=IntVar()
    v5=IntVar()
    v6=IntVar()
    v7=IntVar()
    v8=IntVar()
    v9=IntVar()
    v10=IntVar()
    v11=IntVar()
    v12=IntVar()
    v13=IntVar()
    v14=IntVar()
    v15=IntVar()
    v16=IntVar()



    var16=StringVar()
    var17=StringVar()       # For Date of order
    var18=StringVar()       # for Receipt
    var19=StringVar()       #For Paid Tax
    var20=StringVar()       # For sub total
    var21=StringVar()       # Ttal cost
    var22=StringVar()       # Cost of sweets
    var23=StringVar()       # cost of Chicken
    var24=StringVar()       # service charge

    x=StringVar()       # For Claculator
    

    var26=StringVar()       # For Sweets Item
    var27=StringVar()       
    var28=StringVar()       
    var29=StringVar()       
    var30=StringVar()       
    var31=StringVar()       
    var32=StringVar()       
    var33=StringVar()       #  Up to here


    var34=StringVar()       # For Chicken Item
    var35=StringVar()       
    var36=StringVar()       
    var37=StringVar()       
    var38=StringVar()
    

    vp1=StringVar()
    vp2=StringVar()
    vp3=StringVar()
    vp4=StringVar()
    vp5=StringVar()
    vp6=StringVar()
    vp7=StringVar()
    vp8=StringVar()
    vp9=StringVar()
    vp10=StringVar()
    vp11=StringVar()
    vp12=StringVar()
    vp13=StringVar()
    vp14=StringVar()
    vp15=StringVar()
    vp16=StringVar()



    v1.set(0)     
    v2.set(0)
    v3.set(0)
    v4.set(0)
    v5.set(0)
    v6.set(0)
    v7.set(0)
    v8.set(0)
    v9.set(0)
    v10.set(0)
    v11.set(0)
    v12.set(0)
    v13.set(0)
    v14.set(0)
    v15.set(0)
    v0.set(0)

    vp1.set("0")
    vp2.set("0")
    vp3.set("0")
    vp4.set("0")
    vp5.set("0")
    vp6.set("0")
    vp7.set("0")
    vp8.set("0")
    vp9.set("0")
    vp10.set("0")
    vp11.set("0")
    vp12.set("0")
    vp13.set("0")
    vp14.set("0")
    vp15.set("0")
    vp16.set("0")
    

    var16.set("0")
    var17.set("0")
    var18.set("0")
    var19.set("0")
    var20.set("0")
    var21.set("0")
    var22.set("0")
    var23.set("0")
    var24.set("0")


    var26.set("0")
    var27.set("0")
    var28.set("0")
    var29.set("0")
    var30.set("0")
    var31.set("0")
    var32.set("0")

    var33.set("0")
    var34.set("0")
    var35.set("0")
    var36.set("0")
    var37.set("0")
    var38.set("0")



    def Reset():
        
        v1.set(0)     
        v2.set(0)
        v3.set(0)
        v4.set(0)
        v5.set(0)
        v6.set(0)
        v7.set(0)
        v8.set(0)
        v9.set(0)
        v10.set(0)
        v11.set(0)
        v12.set(0)
        v13.set(0)
        v14.set(0)
        v15.set(0)
        v0.set(0)

        var16.set("0")
        var17.set("0")
        var18.set("0")
        var19.set("0")
        var20.set("0")
        var21.set("0")
        var22.set("0")
        var23.set("0")
        var24.set("0")


        var26.set("0")
        var27.set("0")
        var28.set("0")
        var29.set("0")
        var30.set("0")
        var31.set("0")
        var32.set("0")

        var33.set("0")
        var34.set("0")
        var35.set("0")
        var36.set("0")
        var37.set("0")
        var38.set("0")
            
        vp1.set("0")
        vp2.set("0")
        vp3.set("0")
        vp4.set("0")
        vp5.set("0")
        vp6.set("0")
        vp7.set("0")
        vp8.set("0")
        vp9.set("0")
        vp10.set("0")
        vp11.set("0")
        vp12.set("0")
        vp13.set("0")
        vp14.set("0")
        vp15.set("0")
        vp16.set("0")

        e1.configure(state=DISABLED)     
        e2.configure(state=DISABLED)
        e3.configure(state=DISABLED)
        e4.configure(state=DISABLED)
        e5.configure(state=DISABLED)
        e6.configure(state=DISABLED)
        e7.configure(state=DISABLED)
        e8.configure(state=DISABLED)
        e9.configure(state=DISABLED)
        e10.configure(state=DISABLED)
        e11.configure(state=DISABLED)
        e12.configure(state=DISABLED)
        e13.configure(state=DISABLED)
        e14.configure(state=DISABLED)
        e15.configure(state=DISABLED)
        e16.configure(state=DISABLED)

        ep1.configure(state=DISABLED)     
        ep2.configure(state=DISABLED)
        ep3.configure(state=DISABLED)
        ep4.configure(state=DISABLED)
        ep5.configure(state=DISABLED)
        ep6.configure(state=DISABLED)
        ep7.configure(state=DISABLED)
        ep8.configure(state=DISABLED)
        ep9.configure(state=DISABLED)
        ep10.configure(state=DISABLED)
        ep11.configure(state=DISABLED)
        ep12.configure(state=DISABLED)
        ep13.configure(state=DISABLED)
        ep14.configure(state=DISABLED)
        ep15.configure(state=DISABLED)
        ep16.configure(state=DISABLED)

        t.delete("1.0",END)


    def costofitem():
        item1=float(var16.get())
        price1=float(vp1.get())
        item2=float(var17.get())
        price2=float(vp2.get())
        item3=float(var18.get())
        price3=float(vp3.get())
        item4=float(var19.get())
        price4=float(vp4.get())
        item5=float(var20.get())
        price5=float(vp5.get())
        item6=float(var21.get())
        price6=float(vp6.get())
        item7=float(var22.get())
        price7=float(vp7.get())
        item8=float(var23.get())
        price8=float(vp8.get())
        item9=var24.get()
        price9=vp9.get()
        item10=var26.get()
        price10=vp10.get()
        item11=var27.get()
        price11=vp11.get()
        item12=var28.get()
        price12=vp12.get()
        item13=var29.get()
        price13=vp13.get()
        item14=var30.get()
        price14=vp14.get()
        item15=var31.get()
        price15=vp15.get()
        item16=var32.get()
        price16=vp16.get()
        

        priceofsweets=(item1*price1)+(item2*price2)+(item3*price3)+(item4*price4)+(item5*price5)+(item6*price6)+(item7*price7)+(item8*price8)

        priceofchicken=(float(item9)*float(price9))+(float(item10)*float(price10))+(float(item11)*float(price11))+(float(item12)*float(price12))\
                       +(float(item13)*float(price13))+(float(item14)*float(price14))+(float(item15)*float(price15))+(float(item16)*float(price16))


        sweetsprice="Rs",str("%.2f"%(priceofsweets))
        chickenprice="Rs",str("%.2f"%priceofchicken)
        var33.set(sweetsprice)
        var34.set(chickenprice)
        sc="Rs",str("%.2f"%(1.59))
        var35.set(sc)

        subtotal="Rs",str("%.2f"%(priceofsweets+priceofchicken+1.59))
        var37.set(subtotal)
        tax="Rs",str("%.2f"%((priceofsweets+priceofchicken+1.59)*0.15))
        var36.set(tax)
        tt=((priceofsweets+priceofchicken)*0.15)
        tc="Rs",str("%.2f"%(priceofsweets+priceofchicken+tt+1.59))
        var38.set(tc)





    
            

    def cb2():
        if(v2.get()==1):
            e2.configure(state=NORMAL)
            ep2.configure(state=NORMAL)
            e2.focus()
            e2.delete("0",END)
            ep2.delete("0",END)
            var17.set("")
            vp2.set("")
        elif(v2.get()==0):
            e2.configure(state=DISABLED)
            ep2.configure(state=DISABLED)
            var17.set("0")
            vp2.set("0")


    def cb1():
        if(v1.get()==1):
            e1.configure(state=NORMAL)
            ep1.configure(state=NORMAL)
            e1.focus()
            e1.delete("0",END)
            ep1.delete("0",END)
            var16.set("")
            vp1.set("")
        elif(v1.get()==0):
            e1.configure(state=DISABLED)
            ep1.configure(state=DISABLED)
            var16.set("0")
            vp1.set("0")


    def cb3():
        if(v3.get()==1):
            e3.configure(state=NORMAL)
            ep3.configure(state=NORMAL)
            e3.focus()
            e3.delete("0",END)
            ep3.delete("0",END)
            var18.set("")
            vp3.set("")
        elif(v3.get()==0):
            e3.configure(state=DISABLED)
            ep3.configure(state=DISABLED)
            var18.set("0")
            vp3.set("")

    def cb4():
        if(v4.get()==1):
            e4.configure(state=NORMAL)
            ep4.configure(state=NORMAL)
            e4.focus()
            e4.delete("0",END)
            ep4.delete("0",END)
            var19.set("")
            vp4.set("")
            
        elif(v4.get()==0):
            e4.configure(state=DISABLED)
            e4.configure(state=DISABLED)
            var19.set("0")
            vp4.set("")



    def cb5():
        if(v5.get()==1):
            e5.configure(state=NORMAL)
            ep5.configure(state=NORMAL)
            e5.focus()
            e5.delete("0",END)
            ep5.delete("0",END)
            var20.set("")
            vp5.set("")
            
        elif(v5.get()==0):
            e5.configure(state=DISABLED)
            ep5.configure(state=DISABLED)
            var20.set("0")
            vp5.set("")

            

    def cb6():
        if(v6.get()==1):
            e6.configure(state=NORMAL)
            ep6.configure(state=NORMAL)
            e6.focus()
            e6.delete("0",END)
            ep6.delete("0",END)
            var21.set("")
            vp6.set("")
        elif(v6.get()==0):
            e6.configure(state=DISABLED)
            ep6.configure(state=DISABLED)
            var21.set("0")
            vp6.set("")


    def cb7():
        if(v7.get()==1):
            e7.configure(state=NORMAL)
            ep7.configure(state=NORMAL)
            e7.focus()
            e7.delete("0",END)
            ep7.delete("0",END)
            var22.set("")
            vp7.set("")
        elif(v7.get()==0):
            e7.configure(state=DISABLED)
            ep7.configure(state=DISABLED)
            var22.set("0")
            vp7.set("")


    def cb8():
        if(v8.get()==1):
            e8.configure(state=NORMAL)
            ep8.configure(state=NORMAL)
            e8.focus()
            e8.delete("0",END)
            ep8.delete("0",END)
            var23.set("")
            vp8.set("")
            
        elif(v8.get()==0):
            e8.configure(state=DISABLED)
            ep8.configure(state=DISABLED)
            var23.set("0")
            vp8.set("")


    def cb9():
        if(v9.get()==1):
            e9.configure(state=NORMAL)
            ep9.configure(state=NORMAL)
            e9.focus()
            e9.delete("0",END)
            ep9.delete("0",END)
            var24.set("")
            vp9.set("")
        elif(v9.get()==0):
            e9.configure(state=DISABLED)
            ep9.configure(state=DISABLED)
            var24.set("0")
            vp9.set("0")


    def cb10():
        if(v10.get()==1):
            e10.configure(state=NORMAL)
            ep10.configure(state=NORMAL)
            e10.focus()
            e10.delete("0",END)
            ep10.delete("0",END)
            var26.set("")
            vp10.set("")
        elif(v10.get()==0):
            e10.configure(state=DISABLED)
            ep10.configure(state=DISABLED)
            var26.set("0")
            vp10.set("")


    def cb11():
        if(v11.get()==1):
            e11.configure(state=NORMAL)
            ep11.configure(state=NORMAL)
            e11.focus()
            e11.delete("0",END)
            ep11.delete("0",END)
            var27.set("")
            vp11.set("")
        elif(v11.get()==0):
            e11.configure(state=DISABLED)
            ep11.configure(state=DISABLED)
            var27.set("0")
            vp11.set("")
            

    def cb12():
        if(v12.get()==1):
            e12.configure(state=NORMAL)
            ep12.configure(state=NORMAL)
            e12.focus()
            e12.delete("0",END)
            ep12.delete("0",END)
            var28.set("")
            vp12.set("")
        elif(v12.get()==0):
            e12.configure(state=DISABLED)
            ep12.configure(state=DISABLED)
            var28.set("0")
            vp12.set("0")



    def cb13():
        if(v13.get()==1):
            e13.configure(state=NORMAL)
            ep13.configure(state=NORMAL)
            e13.focus()
            e13.delete("0",END)
            ep13.delete("0",END)
            var29.set("")
            vp13.set("")
        elif(v13.get()==0):
            e13.configure(state=DISABLED)
            ep13.configure(state=DISABLED)
            var29.set("0")
            vp13.set("0")
            


    def cb14():
        if(v14.get()==1):
            e14.configure(state=NORMAL)
            ep14.configure(state=NORMAL)
            e14.focus()
            e14.delete("0",END)
            ep14.delete("0",END)
            var30.set("")
            vp14.set("")
        elif(v14.get()==0):
            e14.configure(state=DISABLED)
            ep14.configure(state=DISABLED)
            var30.set("0")
            vp14.set("0")


    def cb15():
        if(v15.get()==1):
            e15.configure(state=NORMAL)
            ep15.configure(state=NORMAL)
            e15.focus()
            e15.delete("0",END)
            ep15.delete("0",END)
            var31.set("")
            vp15.set("")
        elif(v15.get()==0):
            e15.configure(state=DISABLED)
            ep15.configure(state=DISABLED)
            var31.set("0")
            vp31.set("0")

    def cb16():
        if(v0.get()==1):
            e16.configure(state=NORMAL)
            ep16.configure(state=NORMAL)
            e16.focus()
            e16.delete("0",END)
            ep16.delete("0",END)
            var32.set("")
            vp16.set("")
        elif(v0.get()==0):
            e16.configure(state=DISABLED)
            ep16.configure(state=DISABLED)
            var32.set("0")
            vp16.set("")




    def receipt():
        t.delete("1.0",END)

        t.insert(END,"Item\t\t\t\t"+"Quantity\t"+"Cost\n\n\n")
        t.insert(END,"Raj Drabar : -  \n\n")
        t.insert(END,"Litti : \t\t\t\t"+var16.get()+"\t"+vp1.get()+"\n")
        t.insert(END,"Samosa : \t\t\t\t"+var17.get()+"\t"+vp2.get()+"\n")
        t.insert(END,"Spunj : \t\t\t\t"+var18.get()+"\t"+vp3.get()+"\n")
        t.insert(END,"Latta : \t\t\t\t"+var19.get()+"\t"+vp4.get()+"\n")
        t.insert(END,"Raskadam : \t\t\t\t"+var20.get()+"\t"+vp5.get()+"\n")
        t.insert(END,"Khirkadam : \t\t\t\t"+var21.get()+"\t"+vp6.get()+"\n")
        t.insert(END,"Jalebi : \t\t\t\t"+var22.get()+"\t"+vp7.get()+"\n")
        t.insert(END,"Butter : \t\t\t\t"+var23.get()+"\t"+vp8.get()+"\n")
        t.insert(END,"Masala : \t\t\t\t"+var24.get()+"\t"+vp9.get()+"\n")
        t.insert(END,"Dehati : \t\t\t\t"+var26.get()+"\t"+vp10.get()+"\n")
        t.insert(END,"Kadhai : \t\t\t\t"+var27.get()+"\t"+vp11.get()+"\n")
        t.insert(END,"Maharaja : \t\t\t\t"+var28.get()+"\t"+vp12.get()+"\n")
        t.insert(END,"Nawabi : \t\t\t\t"+var29.get()+"\t"+vp13.get()+"\n")
        t.insert(END,"Fried : \t\t\t\t"+var30.get()+"\t"+vp14.get()+"\n")
        t.insert(END,"Lolipo : \t\t\t\t"+var31.get()+"\t"+vp15.get()+"\n")
        t.insert(END,"Litti : \t\t\t\t"+var32.get()+"\t"+vp16.get()+"\n")
        t.insert(END,"Tax : \t\t\t\t"+var36.get()+"\n")
        t.insert(END,"Service Charge : \t\t\t\t"+var35.get()+"\n")
        t.insert(END,"Total : - : \t\t\t\t"+var38.get()+"\n")
        


        
    #============================================= SWEETS =================================================================================================================



    lb=Label(f8,text="Item",font=("Arial",18),bg="powder blue",bd=4)
    lb.grid(row=0,column=0)
    
    c1=Checkbutton(f8,text="Litti",command=cb1,variable=v1,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Litti Check Button  on Drink frame
    c1.grid(row=1,sticky=W)

    c2=Checkbutton(f8,text="Samosa",command=cb2,variable=v2,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Samosa Check Button  on Drink frame
    c2.grid(row=2,sticky=W)

    c3=Checkbutton(f8,text="Spunj",command=cb3,variable=v3,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Spunj Check Button  on Drink frame
    c3.grid(row=3,sticky=W)

    c4=Checkbutton(f8,text="Latta",command=cb4,variable=v4,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Latta Check Button  on Drink frame
    c4.grid(row=4,sticky=W)

    c5=Checkbutton(f8,text="RasKadam",command=cb5,variable=v5,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Rasamkadam Check Button  on Drink frame
    c5.grid(row=5,sticky=W)

    c6=Checkbutton(f8,text="KhirKadam",command=cb6,variable=v6,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # KhirKadam Check Button  on Drink frame
    c6.grid(row=6,sticky=W)

    c7=Checkbutton(f8,text="Jalebi",command=cb7,variable=v7,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Jalebi Check Button  on Drink frame
    c7.grid(row=7,sticky=W)

    c8=Checkbutton(f8,text="Raskadam",command=cb8,variable=v8,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # RasKadam Check Button  on Drink frame
    c8.grid(row=8,sticky=W)

    #====================================================Entry box for Sweets===================================================================================================


    lb1=Label(f8,text="Quantity",font=("Arial",18),bg="powder blue",bd=4)
    lb1.grid(row=0,column=1)

    lb2=Label(f8,text="Price",font=("Arial",18),bg="powder blue",bd=4)
    lb2.grid(row=0,column=2)

    
    e1=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var16,state=DISABLED)
    e1.grid(row=1,column=1)

    ep1=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=vp1,state=DISABLED)
    ep1.grid(row=1,column=2)

    e2=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var17,state=DISABLED)
    e2.grid(row=2,column=1)

    ep2=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp2)
    ep2.grid(row=2,column=2)

    e3=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var18,state=DISABLED)
    e3.grid(row=3,column=1)

    ep3=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp3)
    ep3.grid(row=3,column=2)

    e4=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var19,state=DISABLED)
    e4.grid(row=4,column=1)

    ep4=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp4)
    ep4.grid(row=4,column=2)

    e5=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var20,state=DISABLED)
    e5.grid(row=5,column=1)

    ep5=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp5)
    ep5.grid(row=5,column=2)

    e6=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var21,state=DISABLED)
    e6.grid(row=6,column=1)

    ep6=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp6)
    ep6.grid(row=6,column=2)

    e7=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var22,state=DISABLED)
    e7.grid(row=7,column=1)

    ep7=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp7)
    ep7.grid(row=7,column=2)

    e8=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var23,state=DISABLED)
    e8.grid(row=8,column=1)

    ep8=Entry(f8,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp8)
    ep8.grid(row=8,column=2)


    #=====================================================CHICKEN============================================================================================================================



    lb3=Label(f10,text="Item",font=("Arial",18),bg="powder blue",bd=4)
    lb3.grid(row=0,column=0)

    lb4=Label(f10,text="Quantity",font=("Arial",18),bg="powder blue",bd=4)
    lb4.grid(row=0,column=1)

    lb5=Label(f10,text="Price",font=("Arial",18),bg="powder blue",bd=4)
    lb5.grid(row=0,column=2)



    c9=Checkbutton(f10,text="Butter Chicken",command=cb9,variable=v9,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Butter Chicken Check Button  on Drink frame
    c9.grid(row=1,sticky=W)

    c10=Checkbutton(f10,text="Masala Chicken",command=cb10,variable=v10,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Masala Chicken Check Button  on Drink frame
    c10.grid(row=2,sticky=W)

    c11=Checkbutton(f10,text="Dehati Chicken",command=cb11,variable=v11,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Dehati Chicken Check Button  on Drink frame
    c11.grid(row=3,sticky=W)

    c12=Checkbutton(f10,text="Kadhai Chicken",command=cb12,variable=v12,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Kadhai Chicken Check Button  on Drink frame
    c12.grid(row=4,sticky=W)

    c13=Checkbutton(f10,text="Chicken Maharaja",command=cb13,variable=v13,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Chicken Maharaja Check Button  on Drink frame
    c13.grid(row=5,sticky=W)

    c14=Checkbutton(f10,text="Chicken Nawabi",command=cb14,variable=v14,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Chicken Nawabi Check Button  on Drink frame
    c14.grid(row=6,sticky=W)

    c15=Checkbutton(f10,text="Fried Chicken",command=cb15,variable=v15,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Fried Chicken Check Button  on Drink frame
    c15.grid(row=7,sticky=W)

    c16=Checkbutton(f10,text="Chicken Lolipop",command=cb16,variable=v0,onvalue=1,offvalue=0,font=("Arial",18),bg="powder blue",bd=4,relief=RIDGE)    # Chicken Lolipop Check Button  on Drink frame
    c16.grid(row=8,sticky=W)



    #====================================================Entry box for Chicken===================================================================================================



    e9=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var24,state=DISABLED)
    e9.grid(row=1,column=1)

    ep9=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp9)
    ep9.grid(row=1,column=2)

    e10=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var26,state=DISABLED)
    e10.grid(row=2,column=1)

    ep10=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp10)
    ep10.grid(row=2,column=2)

    e11=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var27,state=DISABLED)
    e11.grid(row=3,column=1)

    ep11=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp11)
    ep11.grid(row=3,column=2)

    e12=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var28,state=DISABLED)
    e12.grid(row=4,column=1)

    ep12=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp12)
    ep12.grid(row=4,column=2)

    e13=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var29,state=DISABLED)
    e13.grid(row=5,column=1)

    ep13=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp13)
    ep13.grid(row=5,column=2)

    e14=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var30,state=DISABLED)
    e14.grid(row=6,column=1)

    ep14=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp14)
    ep14.grid(row=6,column=2)

    e15=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var31,state=DISABLED)
    e15.grid(row=7,column=1)

    ep15=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp15)
    ep15.grid(row=7,column=2)

    e16=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,textvariable=var32,state=DISABLED)
    e16.grid(row=8,column=1)

    ep16=Entry(f10,font=("Arial",16),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=vp16)
    ep16.grid(row=8,column=2)
    

    #===============================================Total Cost=======================================================================================================================================================


    l2=Label(f7,font=("Arial",14),text="Cost of Sweets\t",bg="powder blue",fg="black")           # Label for cost of sweets
    l2.grid(row=0,column=0,sticky=W)

    e17=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var33)             # Entry field for cost of sweets
    e17.grid(row=0,column=1)

    l3=Label(f7,font=("Arial",14),text="Cost of Chicken\t",bg="powder blue",fg="black")     # Label for cost of chicken
    l3.grid(row=1,column=0,sticky=W)

    e18=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var34)                # Entry field for cost of chicken
    e18.grid(row=1,column=1)

    l4=Label(f7,font=("Arial",14),text="Service Charge\t",bg="powder blue",fg="black")             # Label for service charge
    l4.grid(row=2,column=0,sticky=W)

    e19=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var35)               # Entry  for service service charge
    e19.grid(row=2,column=1)



    #===========================================Payment Information===============================================================================================================




    l5=Label(f7,font=("Arial",14),text="\tPaid Tax\t",bg="powder blue",fg="black")           # Label for paid tax
    l5.grid(row=0,column=2,sticky=W)

    e20=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var36)             # Entry field for paid tax
    e20.grid(row=0,column=3)

    l6=Label(f7,font=("Arial",14),text="\tSub Total",bg="powder blue",fg="black")     # Label for Sub total
    l6.grid(row=1,column=2,sticky=W)

    e21=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var37)                # Entry field for Sub Total
    e21.grid(row=1,column=3)

    l7=Label(f7,font=("Arial",14),text="\tTotal Cost",bg="powder blue",fg="black")             # Label for Total Cost
    l7.grid(row=2,column=2,sticky=W)

    e22=Entry(f7,font=("Arial",14),bd=7,bg="white",insertwidth=2,justify=RIGHT,textvariable=var38)               # Entry  for Total cost
    e22.grid(row=2,column=3)

    #============================================Receipt==================================================================================================================================================



    t=Text(f6,width=46,height=12,bg="white",bd=4,font=("Arial",12))   # Reciept Area (Blank)
    t.grid(row=0,column=0)


    #=============================================Button===================================================================================================================================================

    b1=Button(f4,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="Total",bg="powder blue",command=costofitem)            # Button on  Button Frame for  Total        
    b1.grid(row=0,column=0)

    b2=Button(f4,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="Receipt",bg="powder blue",command=receipt)              # Button on  Button Frame for Receipt
    b2.grid(row=0,column=1)


        
    b3=Button(f4,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="Reset",bg="powder blue",command=Reset)            # Button on  Button Frame for  Reset
    b3.grid(row=0,column=2)


    '''def Exit():
        Exit=tkinter.messagebox.askyesno("Exit Resturent System","Confirm if you want to exit")                   # This function is declear for Exit option Of Exit Button on Button frame 
        if (Exit>0):
            root.destroy()
            return'''

    b4=Button(f4,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="Exit",bg="powder blue",command=login1)                     # Button on  Button Frame for   Exit
    b4.grid(row=0,column=3)



    #===================================Calculator Display=============================================================================================================


    def show(num):
        a=x.get()+num
        x.set(a)

    def reset():
        x.set("")

    def equal():
        a=x.get()
        x.set(eval(a))
        
    #============================================Calculator Display==================================================================================================================================================


    tc=Entry(f5,width=45,bg="white",bd=4,font=("Arial",12),justify=RIGHT,textvariable=x)   # Reciept Area (Blank)
    tc.grid(row=0,column=0,columnspan=4,pady=1)
    tc.insert(0,"0")


    #=============================================Calculator Button===================================================================================================================================================

    bc1=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="7",bg="powder blue",command=lambda :show("7"))        # Caclulator  Button for  digit 7          In First row
    bc1.grid(row=2,column=0)

    bc2=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="8",bg="powder blue",command=lambda :show("8"))        # Caclulator  Button for  digit 8
    bc2.grid(row=2,column=1)

    bc3=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="9",bg="powder blue",command=lambda :show("9"))        # Caclulator  Button for  digit 9
    bc3.grid(row=2,column=2)

    bc4=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="+",bg="powder blue",command=lambda :show("+"))       # Caclulator  Button for  operator + 
    bc4.grid(row=2,column=3)

    #=========================================================================================================================

    bc5=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="6",bg="powder blue",command=lambda :show("6"))       # Caclulator  Button for  digit 6   ,     In Secind Row
    bc5.grid(row=3,column=0)

    bc6=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="5",bg="powder blue",command=lambda :show("5"))           # Caclulator  Button for  digit 5
    bc6.grid(row=3,column=1)

    bc7=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="4",bg="powder blue",command=lambda :show("4"))           # Caclulator  Button for  digit 4
    bc7.grid(row=3,column=2)

    bc8=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="-",bg="powder blue",command=lambda :show("-"))           # Caclulator  Button for  operator  -
    bc8.grid(row=3,column=3)

    #==============================================================================================================================================


    bc9=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="3",bg="powder blue",command=lambda :show("3"))           # Caclulator  Button for  digit 3      # Third Row
    bc9.grid(row=4,column=0)

    bc10=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="2",bg="powder blue",command=lambda :show("2"))          # Caclulator  Button for  digit 2
    bc10.grid(row=4,column=1)

    bc11=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="1",bg="powder blue",command=lambda :show("1"))          # Caclulator  Button for  digit 1
    bc11.grid(row=4,column=2)

    bc12=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="*",bg="powder blue",command=lambda :show("*"))          # Caclulator  Button for  opeartor *
    bc12.grid(row=4,column=3)


    #========================================================================================================================================


    bc13=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="C",bg="powder blue",command=reset)          # Caclulator  Button for   Clear          Fourth Row
    bc13.grid(row=5,column=0)

    bc14=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="0",bg="powder blue",command=lambda :show("0"))              # Caclulator  Button for  digit 0
    bc14.grid(row=5,column=1)

    bc15=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="=",bg="powder blue",command=equal)              # Caclulator  Button for  opeartor =
    bc15.grid(row=5,column=2)

    bc16=Button(f5,padx=16,pady=1,bd=7,fg="black",font=("Arial",16),width=4,text="/",bg="powder blue",command=lambda :show("/"))          # Caclulator  Button for  opeartor /
    bc16.grid(row=5,column=3)
















#================================================Login Frame===================================================================================================================================================================================
    




def login1():
    #fnew=Frame(root,bg="powder blue")
    #fnew.pack()
    fnew=Frame(root)                                                 # Setting First frame
    fnew.place(x=0,y=0,width=1550,height=850)
    fnew.configure(background="powder blue")

    fnew3=Frame(fnew,bg="sky blue",bd=20,relief=RIDGE)
    fnew3.place(x=30,y=20,width=1450,height=750)
    
    fnew2=Frame(fnew3,bg="sky blue",bd=20,relief=RIDGE)
    fnew2.place(x=20,y=20,width=1350,height=650)
    
    fnew1=Frame(fnew2,bg="sky blue",bd=20,relief=RIDGE)
    fnew1.place(x=20,y=20,width=1250,height=550)

    ln=Label(fnew1,text="Login System",font=("Algerian",100),bg="powder blue")
    #ln.grid(pady=30,padx=200)
    ln.pack(side=TOP)

    x=StringVar()
    y=StringVar()

    def pa():
        a=x.get()
        b=y.get()
        if(b=="123456" and a=="sonukumar"):
            window()
        else:
            tkinter.messagebox.askyesno("Mesage Box","Invalid Login Detail")
            x.set("")
            y.set("")
            enew.focus_set()



    def Exit():
        Exit=tkinter.messagebox.askyesno("Exit Resturent System","Confirm if you want to exit")                   # This function is declear for Exit option Of Exit Button on Button frame 
        if (Exit>0):
            root.destroy()
            return

    def re():
        x.set("")
        y.set("")
        enew.focus_set()

    time=StringVar()
    
    def display():
        curr=tm.strftime("%H:%M:%S:%p")
        Time["text"]=curr
        fnew1.after(1000,display)
    
    #time=StringVar()
    Time=Label(fnew1,text="",font=("Arial",40),bg="black",fg="red",relief=RIDGE,bd=20)
    Time.place(x=20,y=200)
    display()
    
    fnew5=Frame(fnew1,bg="sky blue",bd=20,relief=RIDGE)
    fnew5.pack(side=TOP)

    ln1=Label(fnew5,text="Username",font=("Arial",20),bg="sky blue",fg="white")
    ln1.grid(row=0,column=1,sticky=W,padx=20,pady=30)

    enew=Entry(fnew5,font=("Arila",15),textvariable=x)
    enew.grid(row=0,column=2)

    ln2=Label(fnew5,text="Password",font=("Arial",20),bg="sky blue",fg="white")
    ln2.grid(row=1,column=1,sticky=W,padx=20,pady=10)

    enew1=Entry(fnew5,show="*",font=("Arila",15),textvariable=y)
    enew1.grid(row=1,column=2)

    fnew6=Frame(fnew1,bg="sky blue",bd=20,relief=RIDGE)
    fnew6.pack()

    bnew1=Button(fnew6,text="Login",font=("Arial",20),command=pa,width=10)
    bnew1.grid(row=0,column=0,padx=10,pady=10)

    bnew1=Button(fnew6,text="Reset",font=("Arial",20),command=re,width=10)
    bnew1.grid(row=0,column=1,padx=10,pady=10)

    bnew1=Button(fnew6,text="Exit",font=("Arial",20),command=Exit,width=10)
    bnew1.grid(row=0,column=2,padx=10,pady=10)


login1()



root.mainloop()

