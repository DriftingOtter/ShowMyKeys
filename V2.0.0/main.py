# Imports
from tkinter import (
    Tk,
    Frame,
    Button,
    Toplevel,
    Label,
    FLAT,
    LEFT,
    RAISED,
    GROOVE,
    CENTER,
    TOP,
    BOTTOM,
    RIGHT,
    S,
    W,
    X,
    messagebox,
)


# Other Imports
from pynput import keyboard
from tkinter import colorchooser
import threading
import yaml
import sys


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

# Keyboard Color & Config Variable Intermediate Storage
windowColor = str()
caseColor = str()
keyColor = str()
highlightColor = str()

# YAML Config Loader
def load_KBD_config():
    
    global windowColor, caseColor, keyColor, highlightColor


    # Check if the YAML file exists
    try:
        with open('kbdConfig.yaml', 'r') as file:
            config_data = yaml.safe_load(file)

    except FileNotFoundError:
        messagebox.showerror("Error", "KBD Config File Not Found !")

    # Get the color values from the config_data dictionary
    caseColor = config_data.get('caseColor')
    keyColor = config_data.get('keyColor')
    windowColor = config_data.get('windowColor')
    highlightColor = config_data.get('highlightColor')


def refactorSpecialChar(text):

    global specialChar_mapping

    # Look up the corresponding character in the char_mapping dictionary
    # If the text is not in the mapping, use the original text
    return specialChar_mapping.get(text, text)


def on_key_press(key):

    global currentBtnColorHex, highlightColorHex
    # Find the button with the text corresponding to the pressed key
    button = find_button_by_text(key)

    # If the button was found, change its relief to "sunken"
    if button:
        button.configure(relief="sunken")
        button.configure(bg=highlightColorHex)


def on_key_release(key):
    # Find the button with the text corresponding to the released key
    button = find_button_by_text(key)

    # If the button was found, change its relief to "raised"
    if button:
        button.configure(relief="raised")
        button.configure(bg=currentBtnColorHex)


def find_button_by_text(key):

    # Get the text of the key press/release
    text = str(key.char) if hasattr(key, "char") else str(key.name)

    # Checks if the code is in special char list and give acording value to 
    # allow for display, else returns original value
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


def cfgFileCallBack():


    global highlightColorChange, bgColorChange, keyColorChange, caseColorChange
    global windowColor, caseColor, keyColor, highlightColor, backgroundButton 
    global keyButton, highlightButton, caseButton, currentBtnColorHex


    def bgColorChange():

        global windowColor, backgroundButton

        windowColor = colorchooser.askcolor()


        # Check if the YAML file exists
        try:
            with open('kbdConfig.yaml', 'r') as file:
                config_data = yaml.safe_load(file)

        except FileNotFoundError:
            messagebox.showerror("Error", "KBD Config File Not Found !")


        # Stores change in YAML config file
        config_data['windowColor'] = windowColor[1] 
        

        # Write the updated YAML data back to the file
        with open('kbdConfig.yaml', 'w') as file:
            yaml.dump(config_data, file)


        # Updates BG value
        app.configure(bg=windowColor[1])


        backgroundButton.config(bg=windowColor[1])


        # Changes The CFG menu button color to match the background
        cfgBtn.config(bg=windowColor[1])

        # Reload The All Config Values Form YAML file
        load_KBD_config()

        # Tells TK to update changes in main loop
        app.update_idletasks()


    def caseColorChange():

        global caseColor, caseButton

        caseColor = colorchooser.askcolor()


        # Check if the YAML file exists
        try:
            with open('kbdConfig.yaml', 'r') as file:
                config_data = yaml.safe_load(file)

        except FileNotFoundError:
            messagebox.showerror("Error", "KBD Config File Not Found !")

        
        # Stores change in YAML config file
        config_data['caseColor'] = caseColor[1] 
        

        # Write the updated YAML data back to the file
        with open('kbdConfig.yaml', 'w') as file:
            yaml.dump(config_data, file)


        keyboardCase.config(bg=caseColor[1])

        caseButton.config(bg=caseColor[1])

        
        # Reload The All Config Values Form YAML file
        load_KBD_config()

        app.update_idletasks()


    def keyColorChange():

        global keyColor, keyButton, row, rows, btn, currentBtnColorHex

        keyColor = colorchooser.askcolor()
 

        # Check if the YAML file exists
        try:
            with open('kbdConfig.yaml', 'r') as file:
                config_data = yaml.safe_load(file)

        except FileNotFoundError:
            messagebox.showerror("Error", "KBD Config File Not Found !")

        
        # Stores change in YAML config file
        config_data['keyColor'] = keyColor[1] 
        

        # Write the updated YAML data back to the file
        with open('kbdConfig.yaml', 'w') as file:
            yaml.dump(config_data, file)


        currentBtnColorHex = keyColor[1]

        btn.config(bg=keyColor[1])

        # Iterate through all rows and buttons to add changes in color too
        for row in rows:
            for button in row.children.values():
                button.configure(bg=keyColor[1])

        keyButton.config(bg=keyColor[1])

        
        # Reload The All Config Values Form YAML file
        load_KBD_config()

        app.update_idletasks()


    def highlightColorChange():

        global highlightColor, highlightColorHex, highlightButton

        highlightColor = colorchooser.askcolor()

        
        # Check if the YAML file exists
        try:
            with open('kbdConfig.yaml', 'r') as file:
                config_data = yaml.safe_load(file)

        except FileNotFoundError:
            messagebox.showerror("Error", "KBD Config File Not Found !")

        
        # Stores change in YAML config file
        config_data['highlightColor'] = highlightColor[1] 
        

        # Write the updated YAML data back to the file
        with open('kbdConfig.yaml', 'w') as file:
            yaml.dump(config_data, file)


        highlightColorHex = highlightColor[1]

        highlightButton.config(bg=highlightColor[1])

        
        # Reload The All Config Values Form YAML file
        load_KBD_config()

        app.update_idletasks()


    root = Toplevel()
    root.geometry("500x500")
    root.title("Settings")
    root.config(bg="#1A1A1A")
    root.resizable(True, True)
    root.attributes("-topmost", "true")

    titleFrame = Frame(master=root, width=600, height=100, bg="#1A1A1A")
    titleFrame.pack(fill=X)

    title = Label(
        master=titleFrame,
        font=("Rubik Bold", 40),
        text="Settings",
        bg="#1A1A1A",
        fg="#EEEEEE",
    )
    title.pack(side=LEFT, padx=10)

    backgroundFrame = Frame(master=root, width=600, height=100, bg="#1A1A1A")
    backgroundFrame.pack(fill=X)

    backgroundTitle = Label(
        master=backgroundFrame,
        font=("Rubik Bold", 20),
        text="  Background Color",
        bg="#1A1A1A",
        fg="#EEEEEE",
    )
    backgroundTitle.pack(side=LEFT, padx=10, pady=30)

    backgroundButton = Button(
        master=root,
        command=bgColorChange,
        width=5,
        height=2,
        relief=FLAT,
        borderwidth=5,
        bg=windowColor,
    )
    backgroundButton.pack(anchor=W, padx=50)

    caseFrame = Frame(master=root, width=600, height=100, bg="#1A1A1A")
    caseFrame.pack(fill=X)

    caseTitle = Label(
        master=caseFrame,
        font=("Rubik Bold", 20),
        text="  Case Color",
        bg="#1A1A1A",
        fg="#EEEEEE",
    )
    caseTitle.pack(side=LEFT, padx=10, pady=30)

    caseButton = Button(
        master=root,
        command=caseColorChange,
        width=5,
        height=2,
        relief=FLAT,
        borderwidth=5,
        bg=caseColor,
    )
    caseButton.pack(anchor=W, padx=50)

    keyFrame = Frame(master=root, width=600, height=100, bg="#1A1A1A")
    keyFrame.pack(fill=X)

    keyTitle = Label(
        master=keyFrame,
        font=("Rubik Bold", 20),
        text="  Keycap Color",
        bg="#1A1A1A",
        fg="#EEEEEE",
    )
    keyTitle.pack(side=LEFT, padx=10, pady=30)

    keyButton = Button(
        master=root,
        command=keyColorChange,
        width=5,
        height=2,
        relief=FLAT,
        borderwidth=5,
        bg=keyColor,
    )
    keyButton.pack(anchor=W, padx=50)

    highlightFrame = Frame(master=root, width=600, height=100, bg="#1A1A1A")
    highlightFrame.pack(fill=X)

    highlightTitle = Label(
        master=highlightFrame,
        font=("Rubik Bold", 20),
        text="  Highlight Color",
        bg="#1A1A1A",
        fg="#EEEEEE",
    )
    highlightTitle.pack(side=LEFT, padx=10, pady=30)

    highlightButton = Button(
        master=root,
        command=highlightColorChange,
        width=5,
        height=2,
        relief=FLAT,
        borderwidth=5,
        bg=highlightColor,
    )
    highlightButton.pack(anchor=W, padx=50)


# 'On Close' logic for mainloop window
def win_onClose():

    global listener, app

    listener.stop()
    app.destroy()


# Tkinter Boiler Plate
app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")

# Loads Keyboard Customization Values
try:
    load_KBD_config()
except FileNotFoundError:
    sys.exit(1)

app.config(background=windowColor)

# Disables resizing of window
app.resizable(False, False)

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=app, borderwidth=40, bg=caseColor, height=500, width=1000, relief=GROOVE
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
            height=3,
            font=("Rubik Bold", 10),
            bg=keyColor,
            takefocus=0,
        )
        btn.pack(side="left")

# Stores Button Color In Var For Use During Highlight Process
currentBtnColorHex = keyColor
highlightColorHex = highlightColor

# Creates Button For cfgMenu.py to be called from
cfgBtn = Button(
    master=app,
    font=("Rubik Bold", 30),
    text="#",
    command=cfgFileCallBack,
    fg="#FFFFFF",
    bg=app["bg"],
    activebackground=app["bg"],
    relief=FLAT,
    borderwidth=0
)
cfgBtn.pack(side=RIGHT, anchor=S, pady=5, padx=5)

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
# Start threading
listener.start()

# Calls 'on_close' logic func on window closing
app.protocol("WM_DELETE_WINDOW", win_onClose)

mainrunner = threading.Thread(target=app.mainloop())

# if name is main start point
if __name__ == "__main__":
    mainrunner.start()
