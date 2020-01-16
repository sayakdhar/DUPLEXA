from tkinter import *
from PIL import Image,ImageTk
from gtts import gTTS
from pygame import mixer

li1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
li2=["1","2","3","4","5","6","7","8","9","0"]
li3=["family","goodbye","learn"]

rw=0
col=0

def prt():
    global rw
    global col
    txt=text.get().strip().split()
    voice=" ".join(txt)
    myobj = gTTS(text=voice, lang='en', slow=True)
    myobj.save("welcome.mp3")
    mixer.init()
    mixer.music.load("welcome.mp3")
    mixer.music.play()
    for i in txt:
        i=i.lower()
        if(i in li1):
            img=ImageTk.PhotoImage(Image.open("English Alphabet/"+i.upper()+".jpg"))
            panel=Label(fr1,image=img)
            panel.grid(row=rw,column=col)
            col+=1
            panel.photo=img
        elif(i in li2):
            img=ImageTk.PhotoImage(Image.open("Numbers/"+i.upper()+".jpg"))
            panel=Label(fr1,image=img)
            panel.grid(row=rw,column=col)
            col+=1
            panel.photo=img
        else:
            for j in i:
                if(j in li1):
                    img=ImageTk.PhotoImage(Image.open("English Alphabet/"+j.upper()+".jpg"))
                    panel=Label(fr1,image=img)
                    panel.grid(row=rw,column=col)
                    col+=1
                    panel.photo=img
                else:
                    img=ImageTk.PhotoImage(Image.open("Numbers/"+j.upper()+".jpg"))
                    panel=Label(fr1,image=img)
                    panel.grid(row=rw,column=col)
                    col+=1
                    panel.photo=img 
        '''elif (i in li3):
            img=Image.open("English Alphabet/"+i[0:2].upper()+".jpeg")
            panel=Label(fr1,image=img)
            panel.grid(row=rw,column=col)
            col+=1
            panel.photo=img
        '''
                   
            
gui=Tk()
gui.config(bg="alice blue")
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

but=Button(fr2,text="Press me to Translate",command=prt)
but.grid(row=18,column=6,columnspan=6)

fr2.grid(row=1)

gui.mainloop()
