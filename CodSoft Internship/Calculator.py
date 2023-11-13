from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("500x650")
root.minsize(500,640)

def calc(event):
    text=event.widget.cget("text")
    if(text=="="):
        ans=eval(screen.get())
        screen.set(ans)
        main.update()

    elif(text=="AC"):
        screen.set("")
        main.update()

    elif(text=="C"):
        t1=screen.get()
        t2=(len(screen.get()))-1
        t3=t1[0:t2]
        screen.set(t3)
        main.update()

    else:
        screen.set(screen.get()+text)
        main.update()
    



screen=StringVar()
screen.set("")

main =Label(root,textvariable=screen,font=("comicsansms",32,"bold"),background="#3A3939",fg="white",width=18,borderwidth=7,relief=RIDGE,pady=30,anchor="e")
main.pack()

f1=Frame(root)
b1=Button(f1,text="AC",font=("comicsansms",32),background="#949494", width=4,height=1,padx=6,pady=10)
b1.pack(side=LEFT)
b2=Button(f1,text="C",font=("comicsansms",32),background="#949494",width=4,height=1 ,padx=6,pady=10)
b2.pack(side=LEFT)
b3=Button(f1,text="^",font=("comicsansms",32),background="#949494", width=4,height=1 ,padx=6,pady=10)
b3.pack(side=LEFT)
b4=Button(f1,text="/",font=("comicsansms",32),background="#949494", width=4,height=1 ,padx=6,pady=10)
b4.pack(side=LEFT)
b1.bind("<Button-1>",calc)
b2.bind("<Button-1>",calc)
b3.bind("<Button-1>",calc)
b4.bind("<Button-1>",calc)
f1.pack()

f1=Frame(root)
b1=Button(f1,text="7",font=("comicsansms",32),background="#D1CECE", width=4,height=1,padx=6,pady=10)
b1.pack(side=LEFT)
b2=Button(f1,text="8",font=("comicsansms",32),background="#D1CECE",width=4,height=1 ,padx=6,pady=10)
b2.pack(side=LEFT)
b3=Button(f1,text="9",font=("comicsansms",32),background="#D1CECE", width=4,height=1 ,padx=6,pady=10)
b3.pack(side=LEFT)
b4=Button(f1,text="*",font=("comicsansms",32),background="#949494", width=4,height=1 ,padx=6,pady=10)
b4.pack(side=LEFT)
b1.bind("<Button-1>",calc)
b2.bind("<Button-1>",calc)
b3.bind("<Button-1>",calc)
b4.bind("<Button-1>",calc)

f1.pack()

f1=Frame(root)
b1=Button(f1,text="4",font=("comicsansms",32),background="#D1CECE", width=4,height=1,padx=6,pady=10)
b1.pack(side=LEFT)
b2=Button(f1,text="5",font=("comicsansms",32),background="#D1CECE",width=4,height=1 ,padx=6,pady=10)
b2.pack(side=LEFT)
b3=Button(f1,text="6",font=("comicsansms",32),background="#D1CECE", width=4,height=1 ,padx=6,pady=10)
b3.pack(side=LEFT)
b4=Button(f1,text="-",font=("comicsansms",32),background="#949494", width=4,height=1 ,padx=6,pady=10)
b4.pack(side=LEFT)
b1.bind("<Button-1>",calc)
b2.bind("<Button-1>",calc)
b3.bind("<Button-1>",calc)
b4.bind("<Button-1>",calc)
f1.pack()

f1=Frame(root)
b1=Button(f1,text="1",font=("comicsansms",32),background="#D1CECE", width=4,height=1,padx=6,pady=10)
b1.pack(side=LEFT)
b2=Button(f1,text="2",font=("comicsansms",32),background="#D1CECE",width=4,height=1 ,padx=6,pady=10)
b2.pack(side=LEFT)
b3=Button(f1,text="3",font=("comicsansms",32),background="#D1CECE", width=4,height=1 ,padx=6,pady=10)
b3.pack(side=LEFT)
b4=Button(f1,text="+",font=("comicsansms",32),background="#949494", width=4,height=1 ,padx=6,pady=10)
b4.pack(side=LEFT)
b1.bind("<Button-1>",calc)
b2.bind("<Button-1>",calc)
b3.bind("<Button-1>",calc)
b4.bind("<Button-1>",calc)
f1.pack()

f1=Frame(root)
b1=Button(f1,text="%",font=("comicsansms",32),background="#D1CECE", width=4,height=1,padx=6,pady=10)
b1.pack(side=LEFT)
b2=Button(f1,text="0",font=("comicsansms",32),background="#D1CECE",width=4,height=1 ,padx=6,pady=10)
b2.pack(side=LEFT)
b3=Button(f1,text=".",font=("comicsansms",32),background="#D1CECE", width=4,height=1 ,padx=6,pady=10)
b3.pack(side=LEFT)
b4=Button(f1,text="=",font=("comicsansms",32),background="#616161", width=4,height=1 ,padx=6,pady=10)
b4.pack(side=LEFT)
b1.bind("<Button-1>",calc)
b2.bind("<Button-1>",calc)
b3.bind("<Button-1>",calc)
b4.bind("<Button-1>",calc)
f1.pack()

root.mainloop()