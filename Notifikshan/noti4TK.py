import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!").grid(row=0, column=0)
label2 = tk.Label(root, text="Hello, Tqlha Baho!").grid(row=3, column=0)
# Pack widgets into root window
t1 = tk.Entry()
t1.grid(row=5, column=1)

# Pack the label into the window
label.pack()
label2.pack()

# Start the main loop
root.mainloop()
