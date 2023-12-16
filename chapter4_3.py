import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def display_photo(path):
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300),resample=0)
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData


def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        display_photo(fpath)

root = tk.Tk()
root.geometry("400x350")

button = tk.Button(text="ファイルを開く",command=openFile)
imageLabel = tk.Label()

button.pack()
imageLabel.pack()
tk.mainloop()