# Imports
from tkinter import *
from pynput import keyboard
import ctypes

specialChar_mapping = {
    "~": "`",
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
    "_": "-",
    "+": "=",
    "{": "[",
    "}": "]",
    "|": "\\",
    ":": ";",
    '''"''': "'",
    "<": ",",
    ">": ".",
    "?": "/",
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
}


def refactorSpecialChar(text):

    global specialChar_mapping

    # Look up the corresponding character in the char_mapping dictionary
    # If the text is not in the mapping, use the original text
    return specialChar_mapping.get(text, text)


def on_key_press(key):
    # Find the button with the text corresponding to the pressed key
    button = find_button_by_text(key)

    # If the button was found, change its relief to "sunken"
    if button:
        button.configure(relief="sunken")


def on_key_release(key):
    # Find the button with the text corresponding to the released key
    button = find_button_by_text(key)

    # If the button was found, change its relief to "raised"
    if button:
        button.configure(relief="raised")


def find_button_by_text(key):

    # Get the text of the key press/release
    text = str(key.char) if hasattr(key, "char") else str(key.name)

    # Checks if the code is in special char list and give acording value to allow for display, else returns original value
    if text in specialChar_mapping:
        text = refactorSpecialChar(text)
    else:
        pass

    # Iterate through all rows and buttons to find the button with the matching text
    for row in rows:
        for button in row.children.values():
            if button.cget("text").strip().lower() == text:
                return button
    return None


# 'On Close' logic for mainloop
def win_onClose():

    global listener, app

    listener.stop()
    app.destroy()


# Tkinter Boiler Plate
app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")
app.config(background="#222831")

# Allows Application To Render Based Upon Users Display DPI
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Disables resizing of window
app.resizable(False, False)

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=app, borderwidth=40, bg="#789395", height=500, width=1000, relief=GROOVE
)
keyboardCase.pack(anchor=CENTER, pady=250)

# indivisual rows for key to be placed in
key_row1 = Frame(master=keyboardCase, width=1000, takefocus=0)
key_row1.pack(side=TOP)

key_row2 = Frame(master=keyboardCase, width=1000, takefocus=0)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(master=keyboardCase, width=1000, takefocus=0)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(master=keyboardCase, width=1000, takefocus=0)
key_row4.pack(anchor=CENTER)

key_row5 = Frame(master=keyboardCase, width=1000, takefocus=0)
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
    """       '       """,
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
            bg="#EEEEEE",
            takefocus=0,
        )
        btn.pack(side="left")

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
# Start threading
listener.start()

# Calls 'on_close' logic func on window closing
app.protocol("WM_DELETE_WINDOW", win_onClose)

# if name is main start point
if __name__ == "__main__":
    app.mainloop()