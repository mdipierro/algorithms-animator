from Tkinter import *
import os
import time

ProgramName='Algorithms Animator'
ProgramVersion='Version 2.7b Copyright 2003 (all rights reserved)'

def CheckLicense():
    return 1

class Presentation:
    def __init__(self, root):
        self.root=root
        self.root.iconify()
        dx=root.winfo_screenwidth()
        dy=root.winfo_screenheight()
        self.dialog=Toplevel(root)
        self.dialog.geometry('%ix%i+%i+%i' % (400,300,dx/2-200, dy/2-150))
        self.dialog.overrideredirect(1)
        self.counter=0
        self.canvas=Canvas(self.dialog, background='white', width=400, height=300)
        self.canvas.pack()        
        self.step()

    def step(self):
        self.dialog.focus_force()
        if self.counter is 0:
            self.canvas.create_text(200,50, text='Welcome to ...',
                                    font=('Helvetica',12),
                                    anchor=CENTER, fill='black')
            self.dialog.after(1000,self.step)
        elif self.counter is 1:
            self.canvas.create_text(200,130, text=ProgramName,
                                    font=('Helvetica',28),
                                    anchor=CENTER, fill='#257797')
            self.dialog.after(500,self.step)
        
        elif self.counter is 2:
            self.canvas.create_text(200,170, text='created by Massimo Di Pierro',
                                    font=('Helvetica',16),
                                    anchor=CENTER, fill='#257797')
            self.dialog.after(500,self.step)

        elif self.counter is 3:
            self.canvas.create_text(200,250, text=ProgramVersion,
                                    font=('Helvetica',12),
                                    anchor=CENTER, fill='black')
            self.dialog.after(2000,self.step)
        else:
            self.dialog.destroy()
            self.root.deiconify()
            self.root.focus_force()
            return
        self.counter=self.counter+1


class ByeBye:
    def __init__(self, root):
        self.root=root
        self.root.iconify()
        dx=root.winfo_screenwidth()
        dy=root.winfo_screenheight()
        self.dialog=Toplevel(root)
        self.dialog.geometry('%ix%i+%i+%i' % (400,300,dx/2-200, dy/2-150))
        self.dialog.overrideredirect(1)
        self.counter=0
        self.canvas=Canvas(self.dialog, background='white', width=400, height=300)
        self.canvas.pack()        
        self.step()

    def step(self):
        self.dialog.focus_force()
        if self.counter is 0:
            self.canvas.create_text(200,50, text='Thank you for using...',
                                    font=('Helvetica',12),
                                    anchor=CENTER, fill='black') 
            self.dialog.after(1000,self.step)
        elif self.counter is 1:
            self.canvas.create_text(200,130, text=ProgramName,
                                    font=('Helvetica',28),
                                    anchor=CENTER, fill='#257797')
            self.dialog.after(500,self.step)
        
        elif self.counter is 2:
            self.canvas.create_text(200,170, text='created by Massimo Di Pierro',
                                    font=('Helvetica',16),
                                    anchor=CENTER, fill='#257797')
            self.dialog.after(500,self.step)

        elif self.counter is 3:
            self.canvas.create_text(200,250, text='Hope to see you again soon!',
                                    font=('Helvetica',12),
                                    anchor=CENTER, fill='black')
            self.dialog.after(2000,self.step)
        else:
            self.dialog.destroy()
            self.root.deiconify()
            self.root.destroy()
            return
        self.counter=self.counter+1
