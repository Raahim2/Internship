from tkinter import *
import random
root=Tk()

letter_list = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_list = [
  "+", ",", ".", "<", ">", "/", "?", "+", "_", "-", "*", "%", "@", "!", "#"
]


def easyp():
  
  for i in range(slider.get()+1):
    
    if (i == 0):
      password = ""

    temp1 = random.choice(letter_list)
    password = password + temp1

  a = random.randint(1, 2)
  if (a == 1):
    password = password.upper()
  else:
    password = password.lower() 
  generated.set(f"The password generated is :{password[1:slider.get()+1]}")



def midp():
  for i in range(slider.get()+1):
    if (i == 0):
      password = ""

    temp1 = random.choice(letter_list)
    temp2 = random.choice(number_list)
    temp3 = random.choice(letter_list)
    temp3 = temp3.upper()

    password = password + temp1 + temp2 + temp3

    generated.set(f"The password generated is :{password[1:slider.get()+1]}")
  

def hardp():
  for i in range(slider.get()+1):
    if (i == 0):
      password = "P"

    temp1 = random.choice(letter_list)
    temp2 = random.choice(number_list)
    temp3 = random.choice(letter_list)
    temp3 = temp3.upper()
    temp4 = random.choice(special_list)
    temp5 = random.choice(special_list)
    password = password + temp1 + temp3 + temp4 + temp2 + temp5

  generated.set(f"The password generated is :{password[1:slider.get()+1]}")



root.geometry("800x400")
root.minsize(600,400)
root.title("Password generator")
generated=StringVar()


Label(root,text="Password generator",font=("comicsansms",32,"bold")).pack()


f1=Frame(root)
Label(f1,text="Enter the length of the password",font=("comicsansms",16)).pack()
slider=Scale(f1,from_=0 , to=50 ,orient=HORIZONTAL )
slider.pack()
f1.pack(pady=20)

f2=Frame(root )
easy=Button(f2,text="  Easy  ",font=("comicsansms",16,"bold") , command=easyp).pack(side=LEFT ,padx=15,pady=7)
mid=Button(f2,text="Mideum",font=("comicsansms",16,"bold") , command=midp ).pack(side=LEFT,padx=15,pady=7)
hard=Button(f2,text="Difficult",font=("comicsansms",16,"bold") , command=hardp ,anchor="e").pack(side=RIGHT,padx=15,pady=7)
f2.pack()

Label(textvariable=generated,font=("comicsansms",16)).pack()






root.mainloop()