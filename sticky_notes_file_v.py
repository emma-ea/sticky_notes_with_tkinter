#!/usr/bin/env python3

import tkinter as tk

window = tk.Tk()
window.title('notes')
window.geometry('250x300')


file=open('notes.stk','a')
file.close()

def writefile(event):
    print('event triggered: file saved')
    file = open('notes.stk', 'w')
    file.write(entry.get(1.0, tk.END))
    file.close()


def readfile():
    print('reading file')
    with open('notes.stk') as file:
        data = file.read()
        entry.insert("1.0", data)


entry = tk.Text(window)
entry.pack()
entry.bind('<KeyPress>', writefile)


readfile()
window.mainloop()