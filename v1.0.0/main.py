# Imports
from tkinter import *
import ctypes
import keyboard

# Define a function to be called when a key is pressed
def key_press(event):
    
    for btn in app.winfo_children():

        if isinstance(btn, Button):

            if btn['text'].strip() == event.char or (btn['text'].strip()).lower() == event.char:

                btn.config(bg="#7971EA")
                btn['relief'] = 'sunken'

# Define a function to be called when a key is released
def key_release(event):
    for btn in app.winfo_children():
        if isinstance(btn, Button):
            btn['relief'] = 'rasied'
    

# Tkinter Boiler Plate
app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")
app.config(background="#2C3333")

# Allows Application To Render Based Upon Users Display DPI
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=app, borderwidth=40, bg="#181D31", height=500, width=1000, relief=GROOVE
)
keyboardCase.pack(pady=200)

# indivisual rows for key to be placed in
key_row1 = Frame(
    master=keyboardCase,
    width=1000,
)
key_row1.pack(side=TOP)

key_row2 = Frame(
    master=keyboardCase,
    width=1000,
)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(
    master=keyboardCase,
    width=1000,
)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(
    master=keyboardCase,
    width=1000,
)
key_row4.pack(anchor=CENTER)

key_row5 = Frame(
    master=keyboardCase,
    width=1000,
)
key_row5.pack(side=BOTTOM)


# Create a list of keys to display on the keyboard
keys_row1 = [
    "        `      ",
    "       1       ",
    "       2       ",
    "       3       ",
    "       4       ",
    "       5       ",
    "       6       ",
    "       7       ",
    "       8       ",
    "       9       ",
    "       0       ",
    "       -       ",
    "       =       ",
    "         Backspace           ",
]

keys_row2 = [
    "               Tab            ",
    "       Q       ",
    "       W       ",
    "       E       ",
    "       R       ",
    "       T       ",
    "       Y       ",
    "       U       ",
    "       I       ",
    "       O       ",
    "       P       ",
    "       [       ",
    "       ]       ",
    "       \\       ",
]

keys_row3 = [
    "              Caps            ",
    "       A       ",
    "       S       ",
    "       D       ",
    "       F       ",
    "       G       ",
    "       H       ",
    "       J       ",
    "       K       ",
    "       L       ",
    "       ;       ",
    '       "       ',
    "               Enter                ",
]

keys_row4 = [
    "                      Shift                     ",
    "       Z       ",
    "       X       ",
    "       C       ",
    "       V       ",
    "       B       ",
    "       N       ",
    "       M       ",
    "       ,       ",
    "       .       ",
    "       /       ",
    "                     Shift                     ",
]

keys_row5 = [
    "       Ctrl        ",
    "       Win       ",
    "       Alt       ",
    "                                                                                   Space                                                                                   ",
    "       Alt       ",
    "   <   ",
    "   ^   ",
    "   v   ",
    "   >   ",
]


# Create a button for each key and add it to the keyboard frame
for key in keys_row1:
    btn = Button(
        key_row1,
        text=key,
        border=10,
        relief=RAISED,
        padx=5,
        height=5,
        font=("Helvetica", 10, "bold"),
    )
    btn.pack(side="left")   

for key in keys_row2:
    btn = Button(
        key_row2,
        text=key,
        border=10,
        relief=RAISED,
        padx=5,
        height=5,
        font=("Helvetica", 10, "bold"),
    )
    btn.pack(side="left")

for key in keys_row3:
    btn = Button(
        key_row3,
        text=key,
        border=10,
        relief=RAISED,
        padx=5,
        height=5,
        font=("Helvetica", 10, "bold"),
    )
    btn.pack(side="left")

for key in keys_row4:
    btn = Button(
        key_row4,
        text=key,
        border=10,
        relief=RAISED,
        padx=5,
        height=5,
        font=("Helvetica", 10, "bold"),
    )
    btn.pack(side="left")

for key in keys_row5:
    btn = Button(
        key_row5,
        text=key,
        border=10,
        relief=RAISED,
        padx=5,
        height=5,
        font=("Helvetica", 10, "bold"),
    )
    btn.pack(side="left")

app.bind("<Key>", key_press)
app.bind("<KeyRelease>", key_release)
# if name is main start point 
if __name__ == "__main__":
    app.mainloop()
