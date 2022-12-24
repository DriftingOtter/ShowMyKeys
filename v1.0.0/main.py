# ShowMyKeys
# Ott6r

from tkinter import *

app = Tk()
app.geometry("1000x1000")
app.title("ShowMyKeys")
app.config(background="#222831")

KeyboardDisplay = Frame(

        master = app,

        bd=5,

        bg="black",

)
KeyboardDisplay.pack(anchor=CENTER, )

class fullSizeKeyboard():
        
        qKey = Button(

                master=KeyboardDisplay,

                width=10,

                height=5,

                bg="White",

                relief=RAISED,

                borderwidth=5,

                text="1"
        )
        qKey.pack(side=LEFT)

        wKey = Button(

                master=KeyboardDisplay,

                width=10,

                height=5,

                bg="Whitr",

                relief=RAISED,

                borderwidth=5,

                text="2",

        )
        wKey.pack(side=RIGHT)


if __name__ == "__main__":
    app.mainloop()

