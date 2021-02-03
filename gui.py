import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Farenheit to Celsuis and insert the result into lbl_result.
    """
    fahrenheit = ent_temp.get() #assign ent_temperature value to fahrenheit.
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = "%s \N{DEGREE CELSIUS}" % (round(celsius, 2))
    
def km_to_miles():
    """Convert the value for kilometers to miles and insert the result into lbl2_result.
    """
    km = ent_km.get()
    miles = 0.6214 * float(km)
    lbl2_result["text"] = "%s Miles" % (round(miles, 2))

window = tk.Tk() #Create an instance of the Tkinter class.
window.title("Converter") #Sets the title of the window.

frame_entry = tk.Frame(master=window) #ent_temp and lbl_temp assigned to this frame.
ent_temp = tk.Entry(master=frame_entry, width=10) #Entry field for temperature.
lbl_temp = tk.Label(master=frame_entry, text='\N{DEGREE FAHRENHEIT}') #Fahrenheit label.

#Lay out in frame_entry using .grid() geometry manager.
ent_temp.grid(row=0, column=0, sticky='e')
lbl_temp.grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(master=window, text='\N{RIGHTWARDS BLACK ARROW}', command=fahrenheit_to_celsius) #Convert button.
lbl_result = tk.Label(master=window, text='\N{DEGREE CELSIUS}') #Degrees Celsius label.

#Lay out frame_entry, btn_convert and lbl_result in window.
frame_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

frame2_entry = tk.Frame(master=window) 
ent_km = tk.Entry(master=frame2_entry, width=10) 
lbl_km = tk.Label(master=frame2_entry, text='KM') 

ent_km.grid(row=0, column=0, sticky='e')
lbl_km.grid(row=0, column=1, sticky='w')

btn2_convert = tk.Button(master=window, text='\N{RIGHTWARDS BLACK ARROW}', command=km_to_miles)
lbl2_result = tk.Label(master=window, text='Miles') 

frame2_entry.grid(row=1, column=0, padx=10)
btn2_convert.grid(row=1, column=1, pady=10)
lbl2_result.grid(row=1, column=2, padx=10)

window.mainloop()