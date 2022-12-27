# ShowMyKeys ⌨️

A Customizable and Clean Keyboard Input Displayer.

## Description 📜

This Python application uses the Tkinter package to produce a graphical user interface (GUI). 
The GUI shows a keyboard layout and indicates the user's current key presses. 
To do this, it binds functions to key press and key release events using the keyboard library.

key_press and key_release are two functions that will be called when a key is pushed or released, respectively. 
The programme starts by importing the required libraries. 
The key press function loops over every Tkinter window's child to determine whether any of them are buttons. 
If they do, it determines if the button's text corresponds to the character of the 
key press event and, if it does, modifies the button's look to show that it is being pushed. 
Similar to this, the key release method loops over each button and changes how they seem to show that 
they are not being pushed.

The software then builds a grid of frames, inserts them into the Tkinter window, and configures the keyboard layout. 
After that, it makes lists of the important labels and buttons for each list. Finally, it uses the keyboard library 
to tie the key press and key release functions to the key press and key release events.

## Getting Started ✅

### Dependencies ⚙️

* tkinter
* ctypes
* Rubik (font family)

### Installing 📂

Go to the link and download the font family.

https://fonts.google.com/specimen/Rubik?query=Rubik

* Download __.ZIP__ file
* Extract file in your desired location
* install all fonts
* dowload __.exe__ for application

### Executing program 👟

* Finally, run the __.exe__ for the software !

## Authors 👤

DriftingOtter (aka. me 😉 )

## License ⚖️

This project is licensed under the GNU General Public License v3.0 License - see the LICENSE.md file for details

## Acknowledgments 📣

Inspiration, code snippets, etc.
* [plus2net](https://www.plus2net.com/python/tkinter-events-typing.php)
