from tkinter import *
from tkinter import colorchooser
import ctypes
import config


# Main Color Values
windowColor = str("#2F2831")
caseColor = str("#789395")
keyColor = str("#FFFFFF")
highlightColor = str("#AED1D4")


def bgColorChange():

    global windowColor

    windowColor = colorchooser.askcolor()

    windowColor = windowColor[1]

    backgroundButton.config(bg=windowColor)

def caseColorChange():

    global caseColor

    caseColor = colorchooser.askcolor()

    caseColor = caseColor[1]

    caseButton.config(bg=caseColor)

def keyColorChange():

    global keyColor

    keyColor = colorchooser.askcolor()

    keyColor = keyColor[1]

    keyButton.config(bg=keyColor)

def highlightColorChange():

    global highlightColor

    highlightColor = colorchooser.askcolor()

    highlightColor = highlightColor[1]

    highlightButton.config(bg=highlightColor)


app = Tk()
app.geometry("600x800")
app.title("Settings")
app.config(bg="#222831")
app.resizable(False, False)
app.iconbitmap(None)
ctypes.windll.shcore.SetProcessDpiAwareness(True)


titleFrame = Frame(

    master=app,

    width=600,

    height=100,

    bg="#222831"

)
titleFrame.pack(fill=X)

title = Label(

    master=titleFrame,

    font=("Rubik Bold", 40),

    text="Settings",

    bg="#222831",

    fg="#EEEEEE"    
)
title.pack(side=LEFT, padx=10, pady=10)


backgroundFrame = Frame(

    master=app,

    width=600,

    height=100,

    bg="#222831"

)
backgroundFrame.pack(fill=X)

backgroundTitle = Label(

    master=backgroundFrame,

    font=("Rubik Bold", 20,),

    text="  Background Color",

    bg="#222831",

    fg="#EEEEEE"    
)
backgroundTitle.pack(side=LEFT, padx=10, pady=40)

backgroundButton = Button(

    master=app,

    command=bgColorChange,

    width=5,

    height=2,

    relief=FLAT,

    borderwidth=5,

    bg=windowColor
)
backgroundButton.pack(anchor=W, padx=50)

caseFrame = Frame(

    master=app,

    width=600,

    height=100,

    bg="#222831"


)
caseFrame.pack(fill=X)

caseTitle = Label(

    master=caseFrame,

    font=("Rubik Bold", 20,),

    text="  Case Color",

    bg="#222831",

    fg="#EEEEEE"

)
caseTitle.pack(side=LEFT, padx=10, pady=40)

caseButton = Button(

    master=app,

    command=caseColorChange,

    width=5,

    height=2,

    relief=FLAT,

    borderwidth=5,

    bg=caseColor
)
caseButton.pack(anchor=W, padx=50)


keyFrame = Frame(

    master=app,

    width=600,

    height=100,

    bg="#222831"


)
keyFrame.pack(fill=X)

keyTitle = Label(

    master=keyFrame,

    font=("Rubik Bold", 20,),

    text="  Keycap Color",

    bg="#222831",

    fg="#EEEEEE"

)
keyTitle.pack(side=LEFT, padx=10, pady=40)

keyButton = Button(

    master=app,

    command=keyColorChange,

    width=5,

    height=2,

    relief=FLAT,

    borderwidth=5,

    bg=keyColor
)
keyButton.pack(anchor=W, padx=50)


highlightFrame = Frame(

    master=app,

    width=600,

    height=100,

    bg="#222831"


)
highlightFrame.pack(fill=X)

highlightTitle = Label(

    master=highlightFrame,

    font=("Rubik Bold", 20,),

    text="  Highlight Color",

    bg="#222831",

    fg="#EEEEEE"

)
highlightTitle.pack(side=LEFT, padx=10, pady=40)

highlightButton = Button(

    master=app,

    command=highlightColorChange,

    width=5,

    height=2,

    relief=FLAT,

    borderwidth=5,

    bg=highlightColor
)
highlightButton.pack(anchor=W, padx=50)


if __name__ == "__main__":
    app.mainloop()
