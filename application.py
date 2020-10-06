
import tkinter as tk
r = tk.Tk() # creating main window object, where r is the name of the main window object
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack() # pack() organizes the widgets in blocks before placing in the parent widget.
r.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur.
