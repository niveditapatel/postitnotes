'''
Created on 27-Aug-2020

@author: User
'''
import tkinter as tk
from tkinter import *
import glob
import os
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.font as tkFont
from tkinter.colorchooser import *
from tkinter import Label
from PIL import ImageTk, Image
from tkinter import filedialog

class NewWindow(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("500x500")  

def dic_imgs():
    imgs = {}
    for i in glob.glob("icons/*.png"):
        pathfile = i
        i = os.path.basename(i)
        name = i.split(".")[0]
        imgs[name] = PhotoImage(file=pathfile)
        if name=="strikethrough" or name=="underline" or name=="italics" or name=="bold" or name == "bullet" or name == "font" or name == "add" or name=="save" or name=="color" or name=="delete" or name=="listview" or name=="insertpic":
            imgs[name] = imgs[name].subsample(22)
    return imgs

def callback():
    print("called the callback!")
    
def newnotewindow():
    NewWindow=Toplevel(root)
    #b1.bind("<Button>",  
     #    lambda e: NewWindow)
    NewWindow.resizable(False, False)
    NewWindow.geometry("520x550")
    #imgs = dic_imgs()

    toolbar = Frame(NewWindow)
    toolbar.configure(bg = 'white')
    toolbar.pack(side=TOP, fill=X)

    b1 = Button(
        toolbar,
        relief=FLAT,
        compound = LEFT,
        command=newnotewindow,
        image = imgs["add"]
       )
    b1.pack(side=LEFT, padx=0, pady=3)

    b3 = Button(
        toolbar,
        compound = LEFT,
        command=savenote,
        relief=FLAT,
        image = imgs["save"]
        )
    b3.pack(side=LEFT, padx=3, pady=3)

    b4 = Button(
        toolbar,
        compound = LEFT,
        command=deletion,
        relief=FLAT,
        image = imgs["delete"]
        )
    b4.pack(side=LEFT, padx=3, pady=3)

    b5 = Button(
        toolbar,
        compound = LEFT,
        command=addimage,
        relief=FLAT,
        image = imgs["insertpic"]
        )
    b5.pack(side=RIGHT, padx=3, pady=3)

    textarea = Frame(NewWindow,width = 500, height = 480,background='white')

    textarea.pack()
    thisScrollBar = Scrollbar(textarea,width = 10)
    thisScrollBar.pack(side=RIGHT,fill=Y) 
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    text = Text(textarea,yscrollcommand=thisScrollBar.set,font=fontStyle)

    text.configure(font = ("Times"), bg = 'aliceblue')
    text.config(font=fontStyle)
    thisScrollBar.config(command=text.yview)
    text.place(x=0,y=0,height=480,width=490)
    thisScrollBar.place(x=490,y=0,height=480,width=10)

    toolbar2 = Frame(NewWindow)
    toolbar2.configure(background = 'white')
    toolbar2.pack(side=BOTTOM, fill=X)

    c1 = Button(
        toolbar2,
        relief=FLAT,
        compound = LEFT,
        command=fontstyle,
        image = imgs["font"]
        )
    c1.pack(side=LEFT, padx=3, pady=3)

    c2 = Button(
        toolbar2,
        compound = LEFT,
        command=colorback,
        relief=FLAT,
        image = imgs["color"]
       )
    c2.pack(side=LEFT, padx=3, pady=3)
    c3 = Button(
        toolbar2,
        relief=FLAT,
        compound = LEFT,
        command=strikethrough,
        image = imgs["strikethrough"]
        )
    c3.pack(side=RIGHT, padx=3, pady=3)

    c4 = Button(
        toolbar2,
        compound = LEFT,
        command=make_underline,
        relief=FLAT,
        image = imgs["underline"]
       )
    c4.pack(side=RIGHT, padx=3, pady=3)
    c5 = Button(
        toolbar2,
        relief=FLAT,
        compound = LEFT,
        command=make_italics,
        image = imgs["italics"]
        )
    c5.pack(side=RIGHT, padx=3, pady=3)

    c6 = Button(
        toolbar2,
        compound = LEFT,
        command=make_bold,
        relief=FLAT,
        image = imgs["bold"]
       )
    c6.pack(side=RIGHT, padx=3, pady=3)

    
    
def newnote():
    root.title("Untitled - Sticky Note") 
    global file 
    file = None
    text.delete(1.0,END)

def addimage():
    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(text,image = tkimage)
    myvar.image = tkimage
    myvar.place(relx=1.0,rely=0.0,anchor='ne')
    myvar.pack()
    
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
def colorback():
    color = askcolor()
    text.configure(background=color[1])
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
        
def deletion():
    root.title("Untitled - Sticky Note") 
    global file 
    file = None
    text.delete(1.0,END)
    
def make_bold():
    fontStyle = tkFont.Font(weight='bold', size=20)
    text.focus()
    text.tag_configure("BOLD",font=fontStyle)
        # tk.TclError exception is raised if not text is selected
    try:
        text.tag_add("BOLD", "sel.first", "sel.last")        
    except tk.TclError:
        pass
def make_italics():
    fontStyle = tkFont.Font(slant="italic", size=20)
    text.focus()
    text.tag_configure("ITALICS",font=fontStyle)
        # tk.TclError exception is raised if not text is selected
    try:
        text.tag_add("ITALICS", "sel.first", "sel.last")        
    except tk.TclError:
        pass
def make_underline():
    fontStyle = tkFont.Font(underline= 1, size=20)
    text.focus()
    text.tag_configure("UNDERLINE",font=fontStyle)
        # tk.TclError exception is raised if not text is selected
    try:
        text.tag_add("UNDERLINE", "sel.first", "sel.last")        
    except tk.TclError:
        pass
def strikethrough():
    fontStyle = tkFont.Font(overstrike=1, size=20)
    text.focus()
    text.tag_configure("STRIKETHROUGH",font=fontStyle)
        # tk.TclError exception is raised if not text is selected
    try:
        text.tag_add("STRIKETHROUGH", "sel.first", "sel.last")        
    except tk.TclError:
        pass
def OnDouble(event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print ("selection:", selection[0], ": '%s'" % value) 
        if selection[0] == 0:
            fontStyle = tkFont.Font(family="Helvetica", size=20)
            text.config(font=fontStyle)
            
        elif selection[0] == 1:
            fontStyle = tkFont.Font(family="Arial", size=20)
            text.config(font=fontStyle)
            
        elif selection[0] == 2:
            fontStyle = tkFont.Font(family="Times", size=20)
            text.config(font=fontStyle)
            
        elif selection[0] == 3:
            fontStyle = tkFont.Font(family="Verdana", size=20)
            text.config(font=fontStyle)
            
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
    listbox.bind("<Double-Button-1>", OnDouble)
    selection = map(int, listbox.curselection())
    abc=set(selection)
    print(abc)
    print(listbox)
    
      
   
        

root = Tk()
root.resizable(False, False)
root.geometry("520x550")
imgs = dic_imgs()

toolbar = Frame(root)
toolbar.configure(bg = 'white')
toolbar.pack(side=TOP, fill=X)

b1 = Button(
    toolbar,
    relief=FLAT,
    compound = LEFT,
    command=newnotewindow,
    image = imgs["add"]
    )
b1.pack(side=LEFT, padx=0, pady=3)

b3 = Button(
    toolbar,
    compound = LEFT,
    command=savenote,
    relief=FLAT,
    image = imgs["save"]
    )
b3.pack(side=LEFT, padx=3, pady=3)

b4 = Button(
    toolbar,
    compound = LEFT,
    command=deletion,
    relief=FLAT,
    image = imgs["delete"]
    )
b4.pack(side=LEFT, padx=3, pady=3)

b5 = Button(
    toolbar,
    compound = LEFT,
    command=addimage,
    relief=FLAT,
    image = imgs["insertpic"]
    )
    
b5.pack(side=RIGHT, padx=3, pady=3)

b6 = Button(
    toolbar,
    compound = LEFT,
    command=callback,
    relief=FLAT,
    image = imgs["listview"]
    )
b6.pack(side=RIGHT, padx=3, pady=3)

textarea = Frame(root,width = 500, height = 480,background='white')

textarea.pack()
thisScrollBar = Scrollbar(textarea,width = 10)
thisScrollBar.pack(side=RIGHT,fill=Y) 
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
text = Text(textarea,yscrollcommand=thisScrollBar.set,font=fontStyle)

text.configure(font = ("Times"), bg = 'aliceblue')
text.config(font=fontStyle)
thisScrollBar.config(command=text.yview)
text.place(x=0,y=0,height=480,width=490)
thisScrollBar.place(x=490,y=0,height=480,width=10)

toolbar2 = Frame(root)
toolbar2.configure(background = 'white')
toolbar2.pack(side=BOTTOM, fill=X)

c1 = Button(
    toolbar2,
    relief=FLAT,
    compound = LEFT,
    command=fontstyle,
    image = imgs["font"]
    )
c1.pack(side=LEFT, padx=3, pady=3)
c2 = Button(
    toolbar2,
    compound = LEFT,
    command=colorback,
    relief=FLAT,
    image = imgs["color"]
    )
c2.pack(side=LEFT, padx=3, pady=3)
c3 = Button(
    toolbar2,
    relief=FLAT,
    compound = LEFT,
    command=strikethrough,
    image = imgs["strikethrough"]
    )
c3.pack(side=RIGHT, padx=3, pady=3)

c4 = Button(
    toolbar2,
    compound = LEFT,
    command=make_underline,
    relief=FLAT,
    image = imgs["underline"]
    )
c4.pack(side=RIGHT, padx=3, pady=3)
c5 = Button(
    toolbar2,
    relief=FLAT,
    compound = LEFT,
    command=make_italics,
    image = imgs["italics"]
    )
c5.pack(side=RIGHT, padx=3, pady=3)

c6 = Button(
    toolbar2,
    compound = LEFT,
    command=make_bold,
    relief=FLAT,
    image = imgs["bold"]
    )
c6.pack(side=RIGHT, padx=3, pady=3)

root.mainloop()