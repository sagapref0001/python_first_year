import tkinter as tk
import tkinter.filedialog as fd
import sklearn.datasets
import sklearn.svm
import PIL.Image
import PIL.ImageTk
import numpy

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize(((8,8)),PIL.Image.Resampling.LANCZOS)

    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300),resample=0))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage

    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = 16- numpy.floor(17 * numImage / 256)
    numImage = numImage.flatten()
    return numImage


def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    textLabel.configure(text="この画像は"+str(n)+"です！")


def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        data = imageToData(fpath)
        predictDigits(data)

root = tk.Tk()
root.geometry("400x400")

button = tk.Button(root,text="ファイルを開く",command=openFile)
imageLabel = tk.Label()
button.pack()
imageLabel.pack()

textLabel = tk.Label(text="手書きの数字を認識します！")
textLabel.pack()

tk.mainloop()