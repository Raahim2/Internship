from tkinter import *
root=Tk()
root.geometry("600x600")
ind=0
def next():
    ind += 1

    var_qs.set(questions[ind])
    var_opa.set(op_A[ind])
    var_opb.set(op_B[ind])
    var_opc.set(op_C[ind])
    var_opd.set(op_D[ind])
    qs.update()
    a.update()
    b.update()
    c.update()
    d.update()



questions=["How are comments written in python?","q2","q3","q4","q5"]
op_A=["// This is a acomment","o2","o3","o4","o5"]
op_B=["#  This is a acomment","o2","o3","o4","o5"]
op_C=["@  This is a acomment","o2","o3","o4","o5"]
op_D=["|| This is a acomment","o2","o3","o4","o5"]
answer=["B","A","A","A","A"]
our=["","","","",""]

var_qs=StringVar()
var_opa=StringVar()
var_opb=StringVar()
var_opc=StringVar()
var_opd=StringVar()

var_qs.set(questions[0])
var_opa.set(op_A[0])
var_opb.set(op_B[0])
var_opc.set(op_C[0])
var_opd.set(op_D[0])


Label(root,text="Python Quiz",background="green",fg="white",font=("comicsansms",24,"bold")).pack(fill=X)

qs=Label(root,textvariable=var_qs,font=("comicsansms",16,"bold"),pady=20)
qs.pack()

optionFrame=Frame(root)
a=Radiobutton(optionFrame,textvariable=var_opa,value="A",font=("comicsansms",12))
b=Radiobutton(optionFrame,textvariable=var_opb,value="B",font=("comicsansms",12))
c=Radiobutton(optionFrame,textvariable=var_opc,value="C",font=("comicsansms",12))
d=Radiobutton(optionFrame,textvariable=var_opd,value="D",font=("comicsansms",12))
a.pack()
b.pack()
c.pack()
d.pack()
Next=Button(optionFrame,text="Next",padx=12,pady=6,command=next)
Next.pack()


optionFrame.pack()




root.mainloop()