#!/usr/bin/env python3

import tkinter as tk

window = tk.Tk()
window.title('notes')
window.geometry('250x300')

# create file if doesnt exist
file=open('notes.stk','a')
file.close()


def writefile(event):   #write method trigger by keypress
    print('event triggered: file saved')
    file = open('notes.stk', 'w')
    file.write(entry.get(1.0, tk.END))
    file.close()


def readfile():     #read contents from file to text widget on start
    print('reading file')
    with open('notes.stk') as file:
        data = file.read()
        entry.insert("1.0", data)


entry = tk.Text(window)
entry.pack(fill=tk.BOTH, expand=1)      # expand along with toplevel widget[parent window]
entry.bind('<KeyPress>', writefile)     #binder handles keypress events; triggers writefile func


readfile()
window.mainloop()