from tkinter import *


import requests
from bs4 import BeautifulSoup
import plyer
import time
import datetime



def notify_me():
    plyer.notification.notify(
        title="Covid-19 Cases of India",
        message=get_corona_detail(),
        timeout=10
    )

def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail():
    url = 'https://www.mygov.in/covid-19/'
    html_data = get_html_data(url)
    bs = BeautifulSoup(html_data.text, 'html.parser')
    ul = bs.find("div", class_='information_row').find_all("div", class_="iblock")

    all_details=""

    for block in ul:
        c = block.find('span', class_='icount').get_text()
        text = block.find('div', class_='info_label').get_text()

        all_details+=text+":"+c+'\n'
        #print(text, end=" ")
        #print(c)
        #print(c)

        # print(block)
        # print()
    # t=tbody.find_all("tr")
    # print(len(ul))
    #print(all_details)
    return all_details


def refresh():
    newdata=get_corona_detail()
    print(newdata)
    l1["text"]=newdata

#print(get_corona_detail())


root=Tk()
root.geometry("500x500+200+200")
root.configure(bg="cadet blue")
root.title("Corona Data Tracker - India")
f=("Arial", 25)
t="Corona Cases in India"
l2=Label(root,text=t,font=("Arial",20),bd=10,relief=RIDGE,bg="cadet blue")
l2.place(x=80,y=10)
l1=Label(root,text=get_corona_detail(),font=f,bd=10,relief=RIDGE,bg="powder blue")
l1.place(x=30,y=100)
b=Button(root,text="Refresh",font=f,bd=10,command=refresh,bg="powder blue")
b.place(x=150,y=350)
notify_me()
root.mainloop()