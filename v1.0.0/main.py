# ShowMyKeys
# Ott6r

from tkinter import *

app = Tk()
app.geometry("1920x1080")
app.title("ShowMyKeys")
app.config(background="#222831")


KeyboardCase = Frame(

        master = app,

        bd=5,

        bg="black",

        height=500,

        width=1000

)
KeyboardCase.pack(pady=300)

key_row1 = Frame(

        master=KeyboardCase,

        width=1000,
   
)
key_row1.pack(side=TOP)

key_row2 = Frame(

        master=KeyboardCase,

        width=1000,
   
)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(

        master=KeyboardCase,

        width=1000,
   
)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(

        master=KeyboardCase,

        width=1000,
   
)
key_row4.pack(side=BOTTOM)

# Create a list of keys to display on the keyboard
keys_row1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',]
keys_row2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
keys_row3 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'']
keys_row4 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

# Create a button for each key and add it to the keyboard frame
for key in keys_row1:
    Button(key_row1, text=key, border=10, relief=RAISED, padx=2, width=10, height=5).pack(side='left')
for key in keys_row2:
    Button(key_row2, text=key, border=10, relief=RAISED, padx=2, width=10, height=5).pack(side='left')
for key in keys_row3:
    Button(key_row3, text=key, border=10, relief=RAISED, padx=2, width=10, height=5).pack(side='left')
for key in keys_row4:
    Button(key_row4, text=key, border=10, relief=RAISED, padx=2, width=10, height=5).pack(side='left')


if __name__ == "__main__":
    app.mainloop()

