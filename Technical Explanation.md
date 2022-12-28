# Technical Explanation ⚙️

*The purpose of the file is for you to getting a better understanding of the code it self.*

* The code starts by importing the necessary libraries: __Tkinter__ for creating the GUI, keyboard from __pynput__ for listening to keyboard events, and __ctypes__ for setting the DPI awareness of the application.

* It defines two functions, on_key_press and on_key_release, which will be called when a key press or key release event is detected by the keyboard event listener. These functions find the button in the GUI that corresponds to the key that was pressed or released, and update its relief to "sunken" or "raised" respectively.

* It also defines a find_button_by_text function, which is used by the on_key_press and on_key_release functions to find the button in the GUI that corresponds to the key that was pressed or released. It does this by iterating through all the rows and buttons in the GUI and comparing the text of each button to the text of the key.

* Next, the code sets up the Tkinter window and its layout. It creates a frame to act as a container for the keyboard and sets its background color and size. It also creates five rows of frames to hold the buttons for the keys, and sets their size and layout.

* The code then defines the text for each key using several lists of strings. Each string in the list corresponds to a button that will be created in the GUI.

* It then creates the buttons using a loop and adds them to their respective rows. It also sets the text, background color, and other properties for each button.

* Finally, the code sets up the keyboard event listener using the keyboard library from pynput. It specifies the functions to call when a key press or key release event is detected, and starts the event listener.

With this, the application is set up and ready to display the graphical keyboard and listen for keyboard events. When a key is pressed or released, the corresponding button in the GUI will be updated to reflect the state of the key.
