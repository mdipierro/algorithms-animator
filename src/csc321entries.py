from csc321show import *
from csc321algorithms import *
from csc321presentation import *

from math import *
from copy import *
import base64
import os
import sys
import Pmw
import pickle
import tkFileDialog
import tkMessageBox
import tkColorChooser

def EntryLocation(root, size=0, title='', label='Node location:',
                  question='Location index:'):
    dialog=Pmw.Dialog(root, buttons=('OK', 'Cancel'), title=title)
    if size<=10:
        i=1
    else:
        i=5
    w1=Pmw.Group(dialog.interior(), tag_text=question)
    w1.pack(fill=X, expand=1, padx=10, pady=5)
    location=Scale(w1.interior(),orient=HORIZONTAL, length=200, from_=0, to=size-1)
    location.pack(fill=X, padx=5, pady=2)
    location.set(0)

    if dialog.activate()!='OK':
        return None
    return location.get()

class EntryNodeObj:
    def __init__(self, root, node, title):
        self.node=deepcopy(node)
        dialog=Pmw.Dialog(root, buttons=('OK', 'Cancel'),title=title)
        value=Pmw.EntryField(dialog.interior(), value=self.node.value,
                             labelpos=W, label_text='Node value:')
        value.pack(fill=X, expand=1, padx=10, pady=5)
        tag=Pmw.EntryField(dialog.interior(), value=self.node.tag,
                            labelpos=W, label_text='Node tag:')
        tag.pack(fill=X, expand=1, padx=10, pady=5)
        data=Pmw.EntryField(dialog.interior(), value=self.node.data,
                            labelpos=W, label_text='Node data:')
        data.pack(fill=X, expand=1, padx=10, pady=5)

        Pmw.alignlabels([value,tag,data])

        w1=Pmw.Group(dialog.interior(), tag_text='Node color:')
        w1.pack(fill=X, expand=1, padx=10, pady=5)
        self.colorbutton=Button(w1.interior(),
                                text=self.node.color,
                                bg=self.node.color,
                                command=self.colorbuttonrun)
        self.colorbutton.pack(fill=X, padx=5, pady=2)

        w2=Pmw.Group(dialog.interior(), tag_text='Node image:')
        w2.pack(fill=X, expand=1, padx=10, pady=5)
        if self.node.image!=None:
            self.image=PhotoImage(format='gif', data=self.node.image)
        else:        
            self.image=None
        self.imagebutton=Button(w2.interior(),
                                image=self.image,
                                command=self.imagebuttonrun)
        self.imagebutton.pack(fill=X, padx=5, pady=2)
        self.imagebutton2=Button(w2.interior(),
                                text='Select GIF image',
                                command=self.imagebuttonrun)
        self.imagebutton2.pack(fill=X, padx=5, pady=2)
        self.imageremove=Button(w2.interior(),
                                text='Remove GIF image',
                                command=self.imagebuttonremove)
        self.imageremove.pack(fill=X, padx=5, pady=2)

        if dialog.activate()!='OK':
            self.node=None
            return
        
        try:
            value=float(value.get())
            if value == int(value): value=int(value)        
        except:
            value=value.get()

        self.node=Node(value=value,
                       tag=tag.get(), color=self.node.color,
                       data=data.get(), image=self.node.image)
        return
        
    def colorbuttonrun(self):
        self.node.color=tkColorChooser.askcolor()[1]
        self.colorbutton.configure(bg=self.node.color)
        self.colorbutton.configure(text=self.node.color)
        return

    def imagebuttonrun(self):    
        imagename=tkFileDialog.askopenfilename()
        if imagename=='': return
        try:
            tmpnodeimage=self.node.image
            tmpimage=self.image
            self.node.image=base64.encodestring(open(imagename,'rb').read())
            self.image=PhotoImage(format='gif', data=self.node.image)
        except:
            self.node.image=tmpnodeimage
            self.image=tmpimage
            tkMessageBox.showwarning(ProgramName, 'The file is not in GIF format')
        self.imagebutton.configure(image=self.image)
        return

    def imagebuttonremove(self):    
        self.imagebutton.configure(image=None)
        self.node.image=None
        self.image=None
        return

def EntryNode(root,node=Node(), title='Entry Node'):
    a=EntryNodeObj(root,node,title)
    return a.node
    
def EntryLink(root, size, link=Link(), title='Entry Link'):
    dialog=Pmw.Dialog(root, buttons=('OK', 'Cancel'),title=title)
    w1=Pmw.Group(dialog.interior(), tag_text='Source node index:')
    w1.pack(fill=X, expand=1, padx=10, pady=5, side=TOP)
    location1=Scale(w1.interior(),orient=HORIZONTAL, length=200, from_=0, to=size-1)
    location1.pack(fill=X, padx=5, pady=2)
    location1.set(0)

    w2=Pmw.Group(dialog.interior(), tag_text='Destination node index:')
    w2.pack(fill=X, expand=1, padx=10, pady=5, side=TOP)
    location2=Scale(w2.interior(),orient=HORIZONTAL, length=200, from_=0, to=size-1)
    location2.pack(fill=X, padx=5, pady=2)
    location2.set(0)
    if link:
        location1.set(link.source)
        location2.set(link.destination)
        w3=Pmw.Group(dialog.interior(), tag_text='Link length:')
        w3.pack(fill=X, expand=1, padx=10, pady=5, side=TOP)
        length=Pmw.EntryField(w3.interior(), value=repr(link.length),
                              labelpos=W, label_text='')
        length.pack(fill=X, padx=5, pady=2)
    
    """
    if link:
        w3=Pmw.Group(dialog.interior(), tag_text='Link length:')
        w3.pack(fill=X, expand=1, padx=10, pady=5, side=TOP)
        length=Scale(w3.interior(),orient=HORIZONTAL, length=200, from_=0, to=50)
        length.pack(fill=X, padx=5, pady=2)
        length.set(link.length)
    if dialog.activate()!='OK':
        return None  
    if link:
        length=length.get()
    else:
        length=1
    """
    
    if dialog.activate()!='OK':
        return None
    if link:
        try:
            length=eval(length.get())
        except:
            tkMessageBox.showwarning(ProgramName,'Link Length is not a Python epression')
            return None
    else:
        length=1
    return Link(location1.get(), location2.get(), length)
