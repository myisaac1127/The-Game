import Tkinter
import random
from Tkinter import *

root = Tkinter.Tk()
root.wm_title('Bad Draw')

###These are all the values that you need to set at the begining
#you can guess if you want but if you need it the values will be in the read me on the Github

#This is where we create a Interager Variable, Meaning that it will change over time. In this case it is the enemys HP
hp = IntVar()
#This is where we set a defualt value, in this case the base value for the enemys hp is 100
hp.set(100)
ohp = IntVar()
ohp.set(100)
sce = IntVar()
sce.set(0)
#This is a String variable Just like the Interager variable it changes over time
choice1 = StringVar()
#Set to choice one starting off
choice1.set("Choice1")
choice2 = StringVar()
choice2.set("Choice2")

#Evertime you click the left button this command activates
def press1():
    #This is getting the sce (Check ReadMe for details) and storing it into S 
    #You can not make it the same thing Ex: s = s.get() This will create errors
    s = sce.get()
    #This checks the S but im sure you can figure that out
    if s == 0:
        s = 1
        #This is storing the S into the Sce in this case s is 1 so the sce will be 1
        sce.set(s)
        #This activates a command
        scene()
    elif s == 1:
        s = 3
        sce.set(s)
        scene()
    elif s == 2:
        s = 5
        sce.set(s)
        scene()
    elif s == 3:
        s = 5
        sce.set(s)
        scene()
    elif s == 4:
        s = 5
        sce.set(s)
        scene()
    elif s == 5:
        s = 7
        sce.set(s)
        scene()
    elif s == 6:
        s = 5
        sce.set(s)
        scene()
def press2():
    s = sce.get()
    
    if s == 0:
        s = 2
        sce.set(s)
        scene()
    elif s == 1:
        s = 4
        sce.set(s)
        scene()
    elif s == 2:
        s = 6
        sce.set(s)
        scene()
    elif s == 3:
        s = 4
        sce.set(s)
        scene()
    elif s == 4:
        s = 6
        sce.set(s)
        scene()
    elif s == 5:
        s = 4
        sce.set(s)
        scene()
    elif s == 6:
        s = 7
        sce.set(s)
        scene()
    
def scene():
    s = sce.get()
    #This is checking what the S is and playing a scene based off of it
    if s == 1:
        #This deletes what is currently on the editor window, This is to avoid clutter MUST ALWAYS HAVE END
        editor.delete("1.0",END)
        #This is if you want to put something in the edditor MUST ALWAYS HAVE Tkinter.END
        editor.insert(Tkinter.END, "This is choice one ")
        #These two are for if you want to change what is on the buttons
        choice1.set("choice1")
        choice2.set("choice2")
    elif s == 2:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "This is choice two ")
    elif s == 3:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "This is choice one after you picked 1")
        choice1.set("choice1")
        choice2.set("choice2")
    elif s == 4:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "This is choice two after you picked 1")
        choice1.set("choice1")
        choice2.set("choice2")
    elif s == 5:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "This is choice one after you picked 2")
        choice1.set("Fight")
        choice2.set("Choice2")
    elif s == 6:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "This is choice two after you picked 2")
        choice1.set("Choice1")
        choice2.set("Fight")
    elif s == 7:
         editor.delete("1.0",END)
         editor.insert(Tkinter.END, "It is time to fight")
         buttons()
         
         
def enturn():
    ####Inside of all this make diffrent fight things Ex:
    # If s == 7:
    #   Battle math here
    # Elif s == 15:
    #    Battle Math here but changed to be more chalenging    
    #
    hp2 = hp.get()
    hpr = ohp.get()
    #This selects a random number from 1 to 20 and stores it into a variable, Im sure you already knew that
    r1 = random.randint(1, 20)
    #Checks to see if you ran out of health
    if hpr == 0:
        editor.delete("1.0",END)
        editor.insert(Tkinter.END, "You ded")
    else:
        #Main battle phase, based on what you rolled abouve it will execute these three commands
        if r1 <= 10:
            editor.insert(Tkinter.END, "He Miss ")
        elif r1 >= 18:
            editor.insert(Tkinter.END, "He Crit  ")
            hpr -= 10
        else:
            editor.insert(Tkinter.END, "He Hit  ")
            hpr -= 5
        ohp.set(hpr)
        #At the end of his turn the Hp is updated here
        if hpr <= 0 or hp2 <= 0:
            #Editor two is displayed above the battle buttons
            editor2.delete("1.0",END)
        else:
            editor2.delete("1.0",END)
            editor2.insert(Tkinter.END, "Your Hp " + str(hpr) + "His Hp " + str(hp2))
#Activated by pressing the Melee button        
def Melee():
    #Same as above but this is your turn
    hp2 = hp.get()
    hpr = ohp.get()
    r = random.randint(1, 20)
    if hp2 <= 0:
        editor.delete("1.0",END)
        editor2.delete("1.0",END)
        editor.insert(Tkinter.END, "Killed It")
        #After you kill the monsters these make the buttons disapear, to make them come bakck use buttons()
        Melee.grid_forget()
        Item.grid_forget()
        Dodge.grid_forget()
    elif hpr <= 0:
        editor.delete("1.0",END)
        editor2.delete("1.0",END)
        editor.insert(Tkinter.END, "You died")
    else:
        if r <= 10:
            editor.delete("1.0",END)
            editor.insert(Tkinter.END, "You Miss  ")
            enturn()
        elif r >= 18:
            editor.delete("1.0",END)
            editor.insert(Tkinter.END, "You Crit  ")
            hp2 -= 10
            enturn()
        else:
            editor.delete("1.0",END)
            editor.insert(Tkinter.END, "You Hit  ")
            hp2 -= 5
            enturn()
    hp.set(hp2)
#This is where we create the buttons

#This is where we update what will be on the buttons
choice1.get()
choice2.get()
s = sce.get()
#These are how we actually create the buttons
Melee = Button(root, text="Melee",command=Melee)
Item = Button(root, text='Item')
Dodge = Button(root, text="Dodge")
button2 = Button(root, textvariable=choice1,width=25,command=press1)
button3 = Button(root, textvariable=choice2,width=25,command=press2)
###button4 = Button(root, text=choice3,width=25)

#This command makes the fight buttons re apear
def buttons():
    Melee.grid(row=1, column=0)
    Item.grid(row=2, column=0)
    Dodge.grid(row=3, column=0)

#This places the bottom choice buttons experement if you wish
button2.grid(sticky="w",row=26, column=1)
button3.grid(sticky="e",row=26, column=1)
###button4.grid(sticky="e",row=26, column=1)
    
#This is how we create and size the windows on the screen
editor = Tkinter.Text(root, height=25, width=80)
#This is where we place it
editor.grid(column=1, row=0, rowspan=10)

editor2 = Tkinter.Text(root, height=2.5, width=10)
editor2.grid(column=0, row=0, rowspan=1)


root.mainloop()