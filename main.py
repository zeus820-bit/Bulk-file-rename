import tkinter
import os
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.title = ("Renamer")
root.geometry('300x150')

def browse_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All fiiles', '*.*')
    )
    choose = askopenfilename()
    inp = file_name.get(1.0, "end-1c")
    os.rename(choose, inp)

def destroy():
    root.destroy()

file_name = tkinter.Text(root, height=1, width=15)
file_name.pack()

button1 = tkinter.Button(root, text="Open a file", command=browse_file)
button1.pack()

button2 = tkinter.Button(root, text="Quit", command=destroy)
button2.pack()

root.mainloop()