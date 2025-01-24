import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk



def convert():
    maile_input = entry_int.get()
    km_output = maile_input * 1.61
    output_string.set(km_output)


# window
window = ttk.Window(themename='darkly')
window.title("Demo")
window.geometry("700x500")

# title
title_label = ttk.Label(master=window, text="Text as widget", font=("Calibri", 20, 'bold'))
title_label.pack()

# input field
inout_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(inout_frame, textvariable=entry_int)
button = ttk.Button(inout_frame, text='convert', command=convert)
entry.pack(side='left', padx=5)
button.pack(side='right')
inout_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font=("Calibri", 10, 'bold'), textvariable=output_string)
output_frame = output_label.pack()

# run
window.mainloop()
