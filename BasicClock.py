#!/usr/bin/env python3

# File: BasicClock.py
# Mission: Demonstrate how to create a graphically distinctive
# clock using Tkinter.

# Rev: 1.0

from tkinter import *
import time

zProgram = Tk()
zProgram.title("Basic Clock - Soft9000.com")
zClock = Label(zProgram,
               font=('ariel', 72, 'bold'),
               bg='gold',
               fg='white')

zDay = Label(zProgram,
               font=('ariel', 36, 'bold'),
               bg='gold',
               fg='green')

zDate = Label(zProgram,
               font=('ariel', 36, 'bold'),
               bg='gold',
               fg='blue')

zClock.pack(fill=BOTH, expand=1)
zDay.pack(side='left', fill=X, expand=1)
zDate.pack(side='right', fill=X, expand=1)


def zTimer():
    zClock.config(text=time.strftime('%H:%M:%S'))
    zDay.config(text=time.strftime('%a'))
    zDate.config(text=time.strftime('%m/%d/%y'))
    zClock.after(500, zTimer)


if __name__ == '__main__':
    zTimer()
    zProgram.mainloop()
    
        
