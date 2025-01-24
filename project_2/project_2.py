import tkinter as tk
from tkinter import ttk

def button_fun():
    print("button was clicked")

# create a window
window = tk.Tk()
window.title("window and widgets")
window.geometry("1000x1000")

# ttk label
label = ttk.Label(master=window, text="This is a label")
label.pack()

# tk.text
text_box = tk.Text(master=window)
text_box.pack()

# tk entry
entry = ttk.Entry(master=window)
entry.pack()

# TTK button
button = ttk.Button(master=window, text="Button", command=lambda: print("button was clicked"))
button.pack()

# exercise


# run
window.mainloop()
