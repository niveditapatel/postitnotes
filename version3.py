import tkinter as tk
from tkinter import *
import glob
import os
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.font as tkFont

file = None

class NewWindow(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("400x400")  

def dic_imgs():
    imgs = {}
    for i in glob.glob("icons/*.png"):
        pathfile = i
        i = os.path.basename(i)
        name = i.split(".")[0]
        imgs[name] = PhotoImage(file=pathfile)
        if name == "bullet" or name == "font" or name == "add" or name=="save" or name=="color" or name=="delete" or name=="listview" or name=="insertpic":
            imgs[name] = imgs[name].subsample(22)
    return imgs

def callback():
    print("called the callback!")
    
def newnotewindow():
    b1.bind("<Button>",  
         lambda e: NewWindow(root)) 
    
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
        
def fontstyle():
    global text
    fontselection = Toplevel(root)
    fontselection.title("Select Font")
    fontselection.geometry("200x200")
    fontselection.configure(bg="aliceblue")
    lb = Label(fontselection,text="Select the font")
    lb.configure(bg="white",bd=5)
    lb.pack(pady=5)
    
    listbox = Listbox(fontselection,height = 80,selectmode = SINGLE)
    listbox.pack(padx=5,pady=5)
    for item in ["Ariel", "Courier", "Times New Roman", "Verdana"]:
        listbox.insert(END, item)
    selection = map(int, listbox.curselection())
    if selection == 0:
        text.config(font=("Helvetica"))
    elif selection == 1:
        text.config(font=("Courier"))
    elif selection == 2:
        text.config(font=("Times"))
    elif selection == 3:
        text.config(font=("Verdana"))
        

root = Tk()
root.resizable(False, False)
root.geometry("400x450")
imgs = dic_imgs()

toolbar = Frame(root)
toolbar.configure(bg = 'white')
toolbar.pack(side=TOP, fill=X)

b1 = Button(
    toolbar,
    relief=FLAT,
    compound = LEFT,
    command=newnotewindow,
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

textarea = Frame(root,width = 400, height = 380)
textarea.pack()
thisScrollBar = Scrollbar(textarea,width = 10)
thisScrollBar.pack(side=RIGHT,fill=Y) 
text = Text(textarea,yscrollcommand=thisScrollBar.set)
text.configure(font = ("Times"), bg = 'aliceblue')
text.config(font=("Helvetica"))
thisScrollBar.config(command=text.yview)
text.place(x=0,y=0,height=380,width=390)
thisScrollBar.place(x=390,y=0,height=380,width=10)

toolbar2 = Frame(root)
toolbar2.configure(bg = 'white')
toolbar2.pack(side=BOTTOM, fill=X)

c1 = Button(
    toolbar2,
    relief=FLAT,
    compound = LEFT,
    command=fontstyle,
    image=imgs["font"])
c1.pack(side=LEFT, padx=3, pady=3)

c2 = Button(
    toolbar2,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image=imgs["bullet"])
c2.pack(side=LEFT, padx=3, pady=3)

mainloop()