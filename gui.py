import tkinter as tk

window = tk.Tk() #Create an instance of the Tkinter class.
greeting = tk.Label(text='Hello, World!') #Create a 'Label' widget with the text "Hello, World!" and assign it to the variable 'greeting'.
greeting.pack() #Add widget to the window.

window.mainloop() #Tells Python to run the Tkinter event loop.