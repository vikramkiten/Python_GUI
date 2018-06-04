from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import *

root =tk.Tk()

def browse():
    root.filename = filedialog.askopenfilename()
    storeImage=root.filename;
    list = storeImage.split('/')
    saveImage = list[len(list) - 1]
    print(saveImage)





root.title("Image processing in PYTHON!")
ttk.Label(root,text=" ").grid()
mainlabel=ttk.Label(root,text="Welcome to Image Processing in PYTHON",font=("Courier", 30))
mainlabel.grid(row=2,column=4,padx=320,pady=20)

 #selecting  image through button
imageButton=ttk.Button(root,text="Click here to select Image",command=browse);
imageButton.grid(row=10,column=0)

root.mainloop()