import tkinter as tk
from tkinter import *
import glob
import os
from tkinter.messagebox import *
from tkinter.filedialog import *

file = None

def dic_imgs():
    imgs = {}
    for i in glob.glob("icons/*.png"):
        pathfile = i
        i = os.path.basename(i)
        name = i.split(".")[0]
        imgs[name] = PhotoImage(file=pathfile)
        if name == "add" or name=="save" or name=="color" or name=="delete" or name=="listview" or name=="insertpic":
            imgs[name] = imgs[name].subsample(22)
    return imgs

def callback():
    print("called the callback!")
    
def newnote():
    root.title("Untitled - Sticky Note") 
    global file 
    file = None
    text.delete(1.0,END)
    
def savenote():
    global file
    if file == None: 
            # Save as new file 
            file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 

            if file == "": 
                file = None
            else: 
                
                # Try to save the file 
                file = open(file,"w") 
                file.write(text.get(1.0,END)) 
                file.close() 
                
                # Change the window title 
                root.title(os.path.basename(file) + " - note") 
                
            
    else: 
        file = open(file,"w") 
        file.write(text.get(1.0,END)) 
        file.close() 
        
def open():
    global file
    file = askopenfilename(defaultextension=".txt", 
                                    filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 

    if file == "": 
            
            # no file to open 
        file = None
    else: 
        root.title(os.path.basename(file) + " - Sticky note") 
        text.delete(1.0,END) 
        file = open(file,"r") 
        text.insert(1.0,file.read()) 
        file.close() 

root = Tk()
root.resizable(False, False)
root.geometry("400x400")
imgs = dic_imgs()

toolbar = Frame(root)
toolbar.configure(bg = 'white')
toolbar.pack(side=TOP, fill=X)

b1 = Button(
    toolbar,
    relief=FLAT,
    compound = LEFT,
    command=newnote,
    image=imgs["add"])
b1.pack(side=LEFT, padx=0, pady=3)

b2 = Button(
    toolbar,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image=imgs["color"])
b2.pack(side=LEFT, padx=3, pady=3)

b3 = Button(
    toolbar,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image=imgs["insertpic"])
b3.pack(side=LEFT, padx=3, pady=3)

b4 = Button(
    toolbar,
    compound = LEFT,
    command=savenote,
    relief=FLAT,
    image=imgs["save"])
b4.pack(side=LEFT, padx=3, pady=3)

b5 = Button(
    toolbar,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image=imgs["delete"])
b5.pack(side=RIGHT, padx=3, pady=3)

b6 = Button(
    toolbar,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image=imgs["listview"])
b6.pack(side=RIGHT, padx=3, pady=3)

thisScrollBar = Scrollbar(root,width = 10)
thisScrollBar.pack(side=RIGHT,fill=Y) 
thisScrollBar.configure(bg = 'blue')
text = Text(root,yscrollcommand=thisScrollBar.set)
text.configure(bg = 'aliceblue')
thisScrollBar.config(command=text.yview)
text.pack()


mainloop()