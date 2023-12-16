import tkinter as tk

def display_label():
    label.configure(text= "こんにちは")

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(text = "LABEL")
button = tk.Button(text= "PUSH",command= display_label)

label.pack()
button.pack()
tk.mainloop()