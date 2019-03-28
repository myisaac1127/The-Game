import Tkinter
import random
from Tkinter import *

root = Tkinter.Tk()
root.wm_title('Bad Draw')

def press1():
    global s
    if s == 1:
        s = 4
        start() 

hp = IntVar()
hp.set(100)
ohp = IntVar()
ohp.set(100)
def enturn():
    hp2 = hp.get()
    hpr = ohp.get()
    r1 = random.randint(1, 20)
    if hp == 0:
        editor.insert(Tkinter.END, "You ded")
    else:
        if r1 <= 10:
            editor.insert(Tkinter.END, "He Miss ")
        elif r1 >= 18:
            editor.insert(Tkinter.END, "He Crit  ")
            hpr -= 10
        else:
            editor.insert(Tkinter.END, "He Hit  ")
            hpr -= 5
        ohp.set(hpr)
        if hpr <= 0 or hp2 <= 0:
            editor2.delete("1.0",END)
        else:
            editor2.delete("1.0",END)
            editor2.insert(Tkinter.END, "Your Hp " + str(hpr) + "His Hp " + str(hp2))
        
def swor():
    ###editor.insert(Tkinter.END, "Give me bacon, ")
    ###editor.see(Tkinter.END)
    hp2 = hp.get()
    hpr = ohp.get()
    r = random.randint(1, 20)
    if hp2 <= 0:
        editor.insert(Tkinter.END, "Killed It")
        editor2.delete("1.0",END)
    elif hpr <= 0:
        editor.insert(Tkinter.END, "Rip")
        editor2.delete("1.0",END)
    else:
        if r <= 10:
            editor.insert(Tkinter.END, "Miss  ")
            enturn()
        elif r >= 18:
            editor.insert(Tkinter.END, "Crit  ")
            hp2 -= 10
            enturn()
        else:
            editor.insert(Tkinter.END, "Hit  ")
            hp2 -= 5
            enturn()
    hp.set(hp2)
choice1 = "Chee"
choice2 = "Bree"

Melee = Button(root, text="Melee",command=swor)
Item = Button(root, text='Item')
Dodge = Button(root, text="Dodge")
button2 = Button(root, text=choice2,width=25)
button3 = Button(root, text=choice1,width=25)
button4 = Button(root, text=choice2,width=25)



Melee.grid(row=0, column=0)
Item.grid(row=1, column=0)
Dodge.grid(row=2, column=0)
button2.grid(sticky="s",row=26, column=1,command=sc)
button3.grid(sticky="w",row=26, column=1,command=sc1)
button4.grid(sticky="e",row=26, column=1,command=sc2)
    
editor = Tkinter.Text(root, height=25, width=80)
editor.grid(column=1, row=0, rowspan=10)

editor2 = Tkinter.Text(root, height=2.5, width=10)
editor2.grid(column=2, row=0, rowspan=1)


root.mainloop()