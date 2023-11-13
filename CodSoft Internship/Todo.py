from tkinter import *
root=Tk()
root.title("Todo List")
root.geometry("700x500")

def add():
    
    global taskframe
    taskframe=Frame(f2,relief=SUNKEN,borderwidth=1)

    tname=Label(taskframe,text=task.get(),anchor="w",width=50)
    tname.pack(side=LEFT)

    dele=Button(taskframe,text="Delete",command=deltask,padx=3,pady=3)
    dele.pack(side=RIGHT,padx=5,pady=3)

    edit=Button(taskframe,text="Edit",command=edittask,padx=3,pady=3)
    edit.pack(side=RIGHT,padx=5,pady=3)
    

    taskframe.pack()

def deltask():
    taskframe.destroy()

def edittask():
    pass


Label(root,text="Task manager", font=("comicsansms",20,"bold")).pack()

f1=Frame(root,pady=3)
task=Entry(f1 ,font=("comicsansms",16),width=35)
task.pack(side=LEFT)
b1=Button(f1,text="ADD",fg="white",background="black", command=add)
b1.pack(side=RIGHT)
f1.pack()



f2=Frame(root)



f2.pack()



root.mainloop()