
from pytube import*
from moviepy.editor import *
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import *



root = Tk()
root.geometry('820x700+400+50')
root.configure(bg='cadet blue')
root.resizable(0,0)

s = StringVar()




def mp3():

    try:

        url = s.get()    #'https://www.youtube.com/watch?v=mRH0cqVM1xU'
        '''
        b.config(text="Please Wait..")
        b.config(state=DISABLED)
        '''

        ob = YouTube(url)
        #str = ob.streams.first()
        path = askdirectory()    #'C:\\Users\\sonu roy\\Desktop'
        l2["text"] = ob.title
        l4["text"] = ob.rating
        b.config(text="Please Wait..")
        b.config(state=DISABLED)
        str = ob.streams.filter(only_audio=True).all()
        str[0].download(output_path=path)
        b.config(text="Done..")
        b.config(state=NORMAL)
        messagebox.showinfo("Title", "Downloaded Successfully")
        b.config(text="Download")
        #s.set("")
        #l2["text"] = ""
        print("Done....")

    except Exception as e:

        print(e)
        print("Error")
        messagebox.showinfo("Title", "Error")
        b.config(text="Download")
        b.config(state=NORMAL)
        s.set("")
        l2["text"] = ""
        l4["text"] = ""


def reset():
    s.set("")
    l2["text"] = "\t\t\t\t\t"
    l4["text"] = "\t\t\t\t\t"


def lowVideo():
    try:

        url = s.get()    #'https://www.youtube.com/watch?v=mRH0cqVM1xU'
        '''
        b.config(text="Please Wait..")
        b.config(state=DISABLED)
        '''

        ob = YouTube(url)
        #str = ob.streams.first()
        path = askdirectory()    #'C:\\Users\\sonu roy\\Desktop'
        l2["text"] = ob.title
        l4["text"] = ob.rating
        b1.config(text="Please Wait..")
        b1.config(state=DISABLED)
        str = ob.streams.first()
        str.download(output_path=path)
        b1.config(text="Done..")
        b1.config(state=NORMAL)
        messagebox.showinfo("Title", "Downloaded Successfully")
        b1.config(text="Video(Low)")
        #s.set("")
        #l2["text"] = ""
        print("Done....")

    except Exception as e:

        print(e)
        print("Error")
        messagebox.showinfo("Title", "Error")
        b1.config(text="Video(Low)")
        b1.config(state=NORMAL)
        s.set("")
        l2["text"] = ""
        l4["text"] = ""

def highVideo():
    try:

        url = s.get()    #'https://www.youtube.com/watch?v=mRH0cqVM1xU'
        '''
        b.config(text="Please Wait..")
        b.config(state=DISABLED)
        '''

        ob = YouTube(url)
        #str = ob.streams.first()
        path = askdirectory()    #'C:\\Users\\sonu roy\\Desktop'
        l2["text"] = ob.title
        l4["text"] = ob.rating
        b2.config(text="Please Wait..")
        b2.config(state=DISABLED)
        str = ob.streams.last()
        str.download(output_path=path)
        b2.config(text="Done..")
        b2.config(state=NORMAL)
        messagebox.showinfo("Title", "Downloaded Successfully")
        b2.config(text="Video(High)")
        #s.set("")
        #l2["text"] = ""
        print("Done....")

    except Exception as e:

        print(e)
        print("Error")
        messagebox.showinfo("Title", "Error")
        b2.config(text="Video(High)")
        b2.config(state=NORMAL)
        s.set("")
        l2["text"] = ""
        l4["text"] = ""


l = Label(root, text="YouTube Audio Video Downloader", font=("Algerian", 20), bd=10, relief=RIDGE)
l.place(x=150, y=30)

l = Label(root, text="URL :-", font=("Algerian", 20), bd=10, relief=RIDGE)
l.place(x=30, y=100)


e=Entry(root, font="Arial", justify=CENTER, bd=10, relief=RIDGE, textvariable=s, width=50)
e.place(x=180, y=100)

l1= Label(root, text="Title :-", font=("Algerian", 20), bd=10, relief=RIDGE)
l1.place(x=30, y=180)

l2=Label(root, text="\t\t\t\t\t",font=("Algerian", 20), bd=10, relief=RIDGE)
l2.place(x=150, y=180)

l3=Label(root, text="Rating",font=("Algerian", 20), bd=10, relief=RIDGE)
l3.place(x=30, y=250)

l4=Label(root, text="\t\t\t\t\t",font=("Algerian", 20), bd=10, relief=RIDGE)
l4.place(x=150, y=250)





b = Button(root, text="mp3", font=("Arial", 20), bd=20, bg="powder blue", command=mp3)
b.place(x=100, y=500)

b1 = Button(root, text="Video(Low)", font=("Arial", 20), bd=20, bg="powder blue", command=lowVideo)
b1.place(x=250, y=500)

b2 = Button(root, text="Video(High)", font=("Arial", 20), bd=20, bg="powder blue", command=highVideo)
b2.place(x=500, y=500)

b3 = Button(root, text="Reset", font=("Arial", 20), bd=20, bg="powder blue", command=reset)
b3.place(x=300, y=600)



root.mainloop()
'''
root=Tk()
root.geometry("780x500")
root.configure(bg="Powder blue")
root.resizable(0,0)

l1=Label(root,text="Youtube Audio Video Downloader", font=("Arial",20),relief=RIDGE,bd=10)
l1.place(x=150,y=10)
root.mainloop()
'''