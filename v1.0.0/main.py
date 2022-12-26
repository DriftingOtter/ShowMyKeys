# Imports
from tkinter import *
import ctypes


# Define a function to be called when a key is pressed
def key_press(event):
    def update_button_relief(button):
        if ((str(button["text"])).strip() == event.char) or (
            (str(button["text"])).strip() == event.keysym
        ) or ((str((button["text"])).lower()).strip() == event.char) or (
            (str((button["text"])).lower()).strip() == event.keysym
        ):
            button["relief"] = "sunken"

    for row in [key_row1, key_row2, key_row3, key_row4, key_row5]:
        for btn in row.winfo_children():
            if isinstance(btn, Button):
                update_button_relief(btn)

# Define a function to be called when a key is released
def key_release(event):
    def update_button_relief(button):
        if ((str(button["text"])).strip() == event.char) or (
            (str(button["text"])).strip() == event.keysym
        ) or ((str((button["text"])).lower()).strip() == event.char) or (
            (str((button["text"])).lower()).strip() == event.keysym
        ):
            button["relief"] = "raised"

    for row in [key_row1, key_row2, key_row3, key_row4, key_row5]:
        for btn in row.winfo_children():
            if isinstance(btn, Button):
                update_button_relief(btn)

# Tkinter Boiler Plate
app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")
app.config(background="#9ea3af")

# Allows Application To Render Based Upon Users Display DPI
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=app, 
    borderwidth=40, 
    bg="#050505", 
    height=500, 
    width=1000, 
    relief=GROOVE
)
keyboardCase.pack(pady=250)

# indivisual rows for key to be placed in
key_row1 = Frame(
    master=keyboardCase,
    width=1000,
    takefocus=0
)
key_row1.pack(side=TOP)

key_row2 = Frame(
    master=keyboardCase,
    width=1000,
    takefocus=0
)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(
    master=keyboardCase,
    width=1000,
    takefocus=0
)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(
    master=keyboardCase,
    width=1000,
    takefocus=0
)
key_row4.pack(anchor=CENTER)

key_row5 = Frame(
    master=keyboardCase,
    width=1000,
    takefocus=0
)
key_row5.pack(side=BOTTOM)


# Create a list of keys to display on the keyboard
keys_row1 = [
    "       `       ",
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
    "         BackSpace          ",
]

keys_row2 = [
    "                   Tab                ",
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
    "          Caps_Lock       ",
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
    "               Return               ",
]

keys_row4 = [
    "                       Shift_L                    ",
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
    "                    Shift_R                   ",
]

keys_row5 = [
    "      Control_L      ",
    "       Win_L     ",
    "     Alt_L       ",
    "                                                                         Space                                                                         ",
    "     Alt_R       ",
    "  Left  ",
    "   Up   ",
    "Down",
    "Right",
]


# Create a button for each key and add it to the keyboard frame
keys = [keys_row1, keys_row2, keys_row3, keys_row4, keys_row5]
rows = [key_row1, key_row2, key_row3, key_row4, key_row5]

for i in range(len(keys)):
    for key in keys[i]:
        btn = Button(
            rows[i],
            text=key,
            border=10,
            relief=RAISED,
            padx=5,
            height=4,
            font=("Rubik Bold", 10),
            bg="#c4c1b9",
            takefocus=0
        )
        btn.pack(side="left")


app.bind("<Key>", key_press)
app.bind("<KeyRelease>", key_release)
app.resizable(False,False)
# if name is main start point
if __name__ == "__main__":
    app.mainloop()

