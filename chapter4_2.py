import tkinter as tk
import random




def display_label():
    kuji = ["大吉", "中吉", "小吉","凶"]
    result = random.choice(kuji)
    label.configure(text= result)

root = tk.Tk()
root.geometry("200x200")

label = tk.Label(text = "LABEL")
button = tk.Button(text= "PUSH",command= display_label)

label.pack()
button.pack()
tk.mainloop()