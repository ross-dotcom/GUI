import tkinter as tk

window = tk.Tk() #Create an instance of the Tkinter class.

greeting = tk.Label(text='\nMy GUI Application\n')

button = tk.Button(text='\nClick\n')

label = tk.Label(text='\nName')

entry = tk.Entry()
entry.insert(0, "Your Name Here...")

about = tk.Label(text='\nTell me about yourself')

text = tk.Text()
text.insert("1.0", "Type...")

greeting.pack() #Add widget to the window.
button.pack()
label.pack()
entry.pack()
about.pack()
text.pack()
    
frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=10)
frame.pack()
frame_label = tk.Label(master=frame, text="FRAME")
frame_label.pack()

window.mainloop() #Tells Python to run the Tkinter event loop.