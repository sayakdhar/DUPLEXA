from tkinter import *
from PIL import Image,ImageTk

pre=""

li1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
li2=["1","2","3","4","5","6","7","8","9","0"]
li3=["family","hello","hi","thank you","thankyou"]

pht=[]

def prt(event):
    global pre
    present=text.get()[:-1]
    if(len(present) and pre!=present):
        if(present.lower() in li1):
            pht.append("English Alphabet/"+present.upper()+".jpg")
        elif(present in li2):
            pht.append("Numbers/"+present+".jpg")
        elif(present.lower() in li3):
            pht.append("Common Words/"+present+".jpg")
        else:
            for i in present:
                i=i.lower()
                if(i in li1):
                    pht.append("English Alphabet/"+present.upper()+".jpg")
                elif(i in li2):
                    pht.append("Numbers/"+present+".jpg")
        pre=text.get()
    

gui=Tk()
gui.config(bg="alice blue")
gui.bind("<space>",prt)
gui.minsize(700,1350)



fr1=Frame(gui,highlightcolor="white",bg="white",width=1350,height=600)
fr1.grid(row=0,columnspan=1350)


fr2=Frame(gui)
fr2.config(bg="alice blue")

l1=Label(fr2,text="Enter the sentence",bg="alice blue")
l1.config(font=("Times New Roman",25))
l1.grid(row=15,column=0,padx=(250,10))

text=StringVar()

w=Entry(fr2,textvariable=text)
w.config(width=100)
w.grid(row=15,column=11,ipady=4)



fr2.grid(row=1)

gui.mainloop()
