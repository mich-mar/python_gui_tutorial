
def button_click():
    #get the data drom entry
    entry_text = entry.get()
    label.config(text=entry_text)
    entry['state'] = 'disable'

# window
window = tk.Tk()
window.geometry("500x200")
window.title("gettin and setting widgets")

# widget
label = ttk.Label(window, text="label")
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="button", command=button_click)
button.pack()

def reset():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

exercise = ttk.Button(window, text="exercise button", command=reset)
exercise.pack()

# run
window.mainloop()
