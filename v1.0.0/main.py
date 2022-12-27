# Imports
from tkinter import *
from pynput import *
import ctypes

def on_press(key):
    # Find the button with the same text as the key pressed
    if hasattr(key, "char"):
        button = find_button_by_text(str(key.char))
    else:
        # If it's a special key, print the key name
        button = find_button_by_text(str(key.name))
    
    if button:
        # Change the relief of the button to 'sunken'
        button.configure(relief='sunken')

def on_release(key):
     # Find the button with the same text as the key pressed
    if hasattr(key, "char"):
        button = find_button_by_text(str(key.char))
    else:
        # If it's a special key, print the key name
        button = find_button_by_text(str(key.name))

    if button:
        # Change the relief of the button to 'raised'
        button.configure(relief='raised')

def find_button_by_text(text):
    for row in rows:
        # Find all buttons in the row
        buttons = row.children.values()
        # Find the button with the matching text
        for button in buttons:
            if ((str(button.cget('text'))).strip()).lower() == text:
                return button
    # Return None if no button was found
    return None

# Tkinter Boiler Plate
app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")
app.config(background="#9ea3af")

# Gives application an icon
appIcon = PhotoImage(file='v1.0.0/ShowMyKeys_Icon.png') 
app.iconphoto(True, appIcon) 

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
    "          BackSpace          ",
]

keys_row2 = [
    "                    Tab                ",
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
    "            Caps_Lock           ",
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
    '''       '       ''',
    "               Enter              ",
]

keys_row4 = [
    "                           Shift                       ",
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
    "          Ctrl_L         ",
    "       CMD     ",
    "     Alt_L       ",
    "                                                                            Space                                                                            ",
    "     Alt_Gr      ",
    "  Left  ",
    "   Up   ",
    "Down",
    "Right",
]


# Create a button for each key and add it to rows var
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

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# Start threading
listener.start()

# Disables resizing of window
app.resizable(False,False)

# if name is main start point
if __name__ == "__main__":
    app.mainloop()
    