from Tkinter import *
from tkFont import *
from random import *
from math import *
from types import *
from csc321algorithms import *
import time
import Pmw
import tkFileDialog
import os
#import webbrowser

default_font=('Helvetica', 10)
min_font_size=7
max_font_size=30

def createNodeRectangle(sc, i, node, x0, y0, x1, y1, balloon=None, font=default_font):
    try:
        value=node.value
        tag=node.tag
        color=node.color
    except:
        value=node
        tag=''
        color=None

    if node.image:
        try:
            sc.icon[i]=PhotoImage(format='gif', data=node.image)
            item=sc.create_image(0.5*(x0+x1),0.5*(y0+y1),image=sc.icon[i])
        except:
            item=sc.create_rectangle(x0,y0,x1,y1,fill='white')
    else:
        item=sc.create_rectangle(x0,y0,x1,y1,fill='white')
        
    if balloon:
        balloon.tagbind(sc,item, 'This is node number [%i]\n\nAttributes:\n  node.value=%s\n  node.tag=%s\n  node.color=%s\n  node.data=%s'
                        % (i, repr(node.value), repr(node.tag), repr(node.color), repr(node.data)))

    if color:
        xc=(x1-x0)/8
        sc.create_oval(x0-xc,y0-xc,x0+xc,y0+xc,fill=color)

    if font[1]<min_font_size and node.image: return

    sc.create_text(x0+0.5*(x1-x0),
                   y1-0.70*(y1-y0),
                   text=value,
                   anchor=CENTER, fill='blue', font=font)

    if tag is '' or tag is None:
        sc.create_text(x0+0.5*(x1-x0),
                       y1-0.30*(y1-y0),
                       text='[%d]' % (i),
                       anchor=CENTER, fill='black', font=font)
    else:
        sc.create_text(x0+0.25*(x1-x0),
                       y1-0.30*(y1-y0),
                       text='[%d]' % (i),
                       anchor=CENTER, fill='black', font=font)
        sc.create_rectangle(x0+0.50*(x1-x0),y1-0.50*(y1-y0),
                            x1+3,y1,fill='white')
        sc.create_text(1.5+0.25*x0+0.75*x1,
                       y1-0.30*(y1-y0),
                       text=tag,
                       anchor=CENTER, fill='black', font=font)
        pass

def nodeBoxSize(i,node, font):
    f=Font(font=font)
    a=f.measure(node.value)
    b=f.measure('[%i]' % (i))
    c=f.measure(node.tag)
    x=max([a, 2*b, 2*c])*1.25
    y=2.3*f.metrics()['linespace']
    if node.image:
        try:
            image=PhotoImage(format='gif', data=node.image)
            x=max([x, image.width()-5])
            y=max([y, image.height()-5])
        except:
            pass        
    return [x,y]

def maxListNodeSize(list,font):
    max = nodeBoxSize(0,list[0],font)
    for i in range(len(list)):
        item=nodeBoxSize(i,list[i],font)
        if item[0]>max[0]: max[0]=item[0]
        if item[1]>max[1]: max[1]=item[1]
    return max

def showList(root, A=[3,5,7], font=default_font):
    bx,by=maxListNodeSize(A,font)
    dx=bx/3
    dy=by/3

    balloon=Pmw.Balloon(root)
    deltax=dx+bx;
    sc=Pmw.ScrolledCanvas(root, borderframe=1,labelpos=N,
                          label_text='List',
                          usehullsize=1,
                          hull_width=10+deltax*len(A)+dx,
                          hull_height=10+2*by+3*dy)
    sc.icon=range(len(A))
    for i in range(len(A)):
        createNodeRectangle(sc,i, A[i],deltax*i,0,deltax*i+bx,by,
                            balloon=balloon,font=font)
        pass
    #sc.pack()
    sc.resizescrollregion()
    return sc

def showSubTree(sc,x0,y0,A, bx, by, dx, dy, counter=1, balloon=None, font=default_font):
    deltax=(bx+dx)/2
    widths=[]
    x1=x0
    y1=y0+dy
    if len(A)==0:
        return counter
    for i in range(0,len(A)):
        widths.append(treeWidth(A[i]))
        x1=x1-deltax*widths[i]
        pass
    for i in range(0,len(A)):
        x1=x1+deltax*widths[i]
        if A[i]!=[]:
            sc.create_line(x0,y0,x1,y1, fill='black')
            if type(A[i]) is ListType:
                node=A[i][0]
            else:
                node=A[i]
                pass
            createNodeRectangle(sc,counter,node,x1-bx/2,y1,x1+bx/2,y1+by,
                                balloon=balloon, font=font)
            counter=counter+1
            if node!=A[i]:
                counter=showSubTree(sc,x1,y1+by,A[i][1:],bx,by,dx,dy,
                                    counter,balloon=balloon, font=font)
                pass
            pass
        x1=x1+deltax*widths[i]
        pass
    return counter

def maxTreeNodeSize(tree,font):
    max=nodeBoxSize(0,getTreeNode(tree,0),font)
    for i in range(treeSize(tree)):
        item=nodeBoxSize(i,getTreeNode(tree,i),font)
        if item[0]>max[0]: max[0]=item[0]
        if item[1]>max[1]: max[1]=item[1]
    return max

def showTree(root,A,font=default_font):
    bx, by=maxTreeNodeSize(A,font)
    dx=bx/3
    dy=by
    balloon=Pmw.Balloon(root)
    deltax=(bx+dx)
    width=deltax*treeWidth(A)+dx
    height=by+(by+dy)*treeHeight(A)
    sc=Pmw.ScrolledCanvas(root, borderframe=1,labelpos=N, label_text='Tree',
                          usehullsize=1, hull_width=width, hull_height=height)
    sc.icon=range(treeSize(A))

    x1=width/2
    y1=by/2
    node=A[0]
    createNodeRectangle(sc,0,node,x1-bx/2,y1,x1+bx/2,y1+by,
                        balloon=balloon, font=font)
    showSubTree(sc,x1,y1+by,A[1:],bx,by,dx,dy,counter=1,balloon=balloon, font=font)
    #sc.pack()
    sc.resizescrollregion()
    return sc

def draw_connection(sc, xc, yc, theta0, theta1, link, dr, br,
                    balloon=None, font=default_font):

    length=str(link.length)
    if len(length)>4:
        try:
            length='%.2f...' % (self.length)
        except:
            length=length[0:4]+'...'

    steps=15
    if link.color:
        line_color=link.color
        line_width=3
    else:
        line_color=None
        line_width=None
        
    dt=(theta1-theta0)/2
    tc=(theta1+theta0)/2
    if theta1==theta0:        
        angle_start=pi+tc
        delta_angle=2*pi
        x0=xc+(dr+1.2*br)*cos(tc)
        y0=yc-(dr+1.2*br)*sin(tc)
        radius=0.5*br
    elif abs(abs(dt)-pi/2)<1e-3:
        x0=xc+dr*cos(theta0)
        y0=yc-dr*sin(theta0)
        x2=xc+dr*cos(theta1)
        y2=yc-dr*sin(theta1)
        x1=x0+(x2-x0)/2.2
        y1=y0+(y2-y0)/2.2
        if line_color:
            sc.create_line(x0,y0,x1,y1, fill=line_color, width=line_width)
            sc.create_line(x1,y1,x2,y2, fill=line_color, width=line_width)
        
        sc.create_line(x0,y0,x1,y1, arrow='last', fill='black')
        sc.create_line(x1,y1,x2,y2, fill='black')
        item=sc.create_text(x1+4,y1+5, text=length, fill='red', font=font)
        if balloon:
            balloon.tagbind(sc,item, 'link.source=[%i]\nlink.destination=[%i]\nlink.length=%s' %
                            (link.source, link.destination, str(link.length)))
        return
    else:
        rc=dr/cos(dt)
        if rc<0:
            rc=-rc
            tc=pi+tc
            dt=2.0*pi-dt
            pass
        radius=rc*sin(dt)        
        x0=xc+rc*cos(tc)
        y0=yc-rc*sin(tc)

        if sin(theta0)>0:
            angle_start=(3.0*pi/2+theta0)
        else:
            angle_start=(3.0*pi/2+theta0)
            pass
        if sin(theta1)>0:
            angle_stop=(pi/2+theta1)
        else:
            angle_stop=(pi/2+theta1)
            pass    
        delta_angle=angle_stop-angle_start    
        if theta1<theta0:
            delta_angle=2.0*pi+delta_angle
            pass
        pass

    if line_color:
        angle=angle_start
        x1=x0+radius*cos(angle)
        y1=y0-radius*sin(angle)
        for i in range(steps):
            angle=angle+delta_angle/steps
            x2=x1
            y2=y1
            x1=x0+radius*cos(angle)
            y1=y0-radius*sin(angle)
            sc.create_line(x1,y1,x2,y2,fill=line_color, width=line_width)
            pass
    angle=angle_start
    x1=x0+radius*cos(angle)
    y1=y0-radius*sin(angle)
    for i in range(steps):
        angle=angle+delta_angle/steps
        x2=x1
        y2=y1
        x1=x0+radius*cos(angle)
        y1=y0-radius*sin(angle)
        if i==int(steps/2.2):
            sc.create_line(x1,y1,x2,y2, arrow='first', fill='black')
            item=sc.create_text(x2+4,y2+5, text=length, fill='red', font=font)
            if balloon:
                balloon.tagbind(sc,item, 'link.source=[%i]\nlink.destination=[%i]\nlink.length=%s' % (link.source, link.destination, str(link.length)))
        else:
            sc.create_line(x1,y1,x2,y2,fill='black')
            pass
        pass
    return

def showGraph(root, graph, font=default_font):
    bx, by = maxListNodeSize(graph[0],font)
    balloon=Pmw.Balloon(root)

    br=0.6*max(bx,by)
    vertices=graph[0]
    links=graph[1]
    
    number_elements=len(vertices)
    if number_elements>7:
        dr=br*number_elements*0.55
    elif number_elements>6:
        dr=br*number_elements*0.6
    elif number_elements>5:
        dr=br*number_elements*0.7
    elif number_elements>4:
        dr=br*number_elements*0.8
    else:
        dr=br*number_elements*0.9
        
    width=height=2*dr+4*br;
    sc=Pmw.ScrolledCanvas(root, borderframe=1,labelpos=N, label_text='Graph',
                          usehullsize=1, hull_width=width, hull_height=height)
    sc.icon=range(len(vertices))
    for link in links:
        i=link.source
        j=link.destination
        theta0=2*pi/number_elements*i
        x=dr*cos(theta0)+2*br+dr
        y=-dr*sin(theta0)+2*br+dr
        xc=2*br+dr
        yc=2*br+dr
        k=j
        theta1=2*pi/number_elements*k
        draw_connection(sc, xc, yc, theta0, theta1, link, dr, br,
                        balloon=balloon, font=font)

    for i in range(len(vertices)):
        theta0=2*pi/number_elements*i
        x=dr*cos(theta0)+2*br+dr
        y=-dr*sin(theta0)+2*br+dr
        node=vertices[i]
        createNodeRectangle(sc,i,node,x-bx/2,y-by/2,x+bx/2,y+by/2,
                            balloon=balloon, font=font)
    
    #sc.pack()
    sc.resizescrollregion()
    return sc

def showGraphAsMatrix(root,graph,font=default_font):
    #ignore font rescaling
    font=default_font
    vertices=graph[0]
    links=graph[1]
    w=30*len(vertices)+100
    h=50+20*len(vertices)
    sc=Pmw.ScrolledCanvas(root, borderframe=1,labelpos=N, label_text='Graph',
                          usehullsize=1, hull_width=w, hull_height=h)
    for i in range(len(vertices)):
        sc.create_text(0, 20+20*i, text='%s [%i]' % (repr(vertices[i]), i),
                       anchor='e', fill='black', font=font)
        sc.create_text(30+30*i, 0, text='[%i]' % (i),
                       anchor=CENTER, fill='black', font=font)
        for j in range(len(vertices)):
            distance=Infinity
            for link in links:
                if link.source==i and link.destination==j:
                    distance=link.length
                    sc.create_text(30+30*j, 20+20*i,
                                   text=distance,
                                   anchor=CENTER, fill='blue', font=font)
                    pass
                pass
            if distance==Infinity:
                sc.create_text(30+30*j, 20+20*i, text='Inf.',
                               anchor=CENTER, fill='red', font=font)
        pass
    #sc.pack(fill='both', expand=1)
    sc.resizescrollregion()
    return sc

def TestPaginate(root, obj, f):
    nb=NoteBook(root)
    for i in range(0,10):
        label='%i' % i
        nb.add(label)
        p=nb.page(label)
        f(p,obj)
        pass
    nb.pack(fill='both', expand=1)
    return

class ShowFrames:
    def close(self):
        self.dialog.destroy()
        
    def __init__(self, root, frames, f=showGraph, title='', save=None, font=default_font, help=None):
        self.frames=deepcopy(frames)
        self.f=f
        self.counter=0
        self.root=root
        self.after=None
        self.dialog=Toplevel(root)
        self.dialog.title(title)
        self.save=save
        self.font=font
        self.help=None # help
        self.sc=0
        self.balloon=Pmw.Balloon(root)
        bottomframe=Frame(self.dialog)
        lmax=len(frames)-1
        if lmax>0:
            self.label=Label(bottomframe,text='Frame: 0')
            self.label.pack(side=LEFT)
            self.scale=Scale(bottomframe, orient=HORIZONTAL, length=150, showvalue=0, from_=0, to=lmax, command=self.move)
            self.scale.pack(side=LEFT, fill=X, padx=5, pady=5)
            self.balloon.bind(self.scale, 'Move to a different frame')

            button=Button(bottomframe,text='Play',
                          command=self.playanimate, width=2)
            button.pack(side=LEFT, fill=Y, padx=5, pady=5)
            self.balloon.bind(button, 'Play animation')

            button=Button(bottomframe,text='Stop',
                          command=self.stopanimate, width=2)
            button.pack(side=LEFT, fill=Y, padx=5, pady=5)
            self.balloon.bind(button, 'Stop animation')


        button=Button(bottomframe,text='In', command=self.zoomin, width=2)
        button.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.balloon.bind(button, 'Enlarge font size')
        
        button=Button(bottomframe,text='Out', command=self.zoomout, width=2)
        button.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.balloon.bind(button, 'Contract font size')

        button=Button(bottomframe,text='EPS',command=self.printcanvas, width=2)
        button.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.balloon.bind(button, 'Save image in PostScript')

        if not self.save is None:
            button=Button(bottomframe,text='Store', command=self.store, width=4)
            button.pack(side=LEFT, fill=Y, padx=5, pady=5)
            self.balloon.bind(button, 'Store present object in memory')
            pass

        button=Button(bottomframe,text='Close', command=self.close, width=4)
        button.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.balloon.bind(button, 'Close this windows')

        if self.help:
            button=Button(bottomframe,text='?', command=self.showhelp, width=2)
            button.pack(side=RIGHT, fill=Y)
            self.balloon.bind(button, 'Description of the algorithm/data structure')
            pass
        bottomframe.pack(side=BOTTOM)
        self.frame=0
        self.drawframe()
        pass

    def showhelp(self):
        #webbrowser.open(self.help)
        try:
            os.system("explorer.exe "+self.help)
        except:
            tkMessageBox.showwarning(ProgramName, 'Problem connecting to Explorer')

    def store(self):
        if not self.save is None:
            self.save[:]=deepcopy(self.frames[self.counter])

    def zoomin(self):
        if self.font[1]<max_font_size:
            self.font=(self.font[0], self.font[1]+1)
        self.drawframe()
        
    def zoomout(self):
        if self.font[1]>=min_font_size:
            self.font=(self.font[0], self.font[1]-1)
        self.drawframe()

    def printcanvas(self):
        if self.sc:
            filename=tkFileDialog.asksaveasfilename()
            if filename:
                x0, y0, x1, y1=self.sc._canvas.bbox(ALL)
                ps=self.sc._canvas.postscript(x=x0, y=y0, width=x1, height=y1)
                file=open(filename, 'w')
                file.write(ps)
                file.close()

    def move(self,h):
        self.counter=self.scale.get()
        self.label.configure(text='Frame: %i' % (self.counter))
        self.drawframe()

    def nextframe(self):
        try:
            i=self.scale.get()+1
            if i<len(self.frames):
                self.scale.set(i)
                self.move(i)
                if self.after: self.root.after_cancel(self.after)
                self.after=self.root.after(1000,self.nextframe)
        except:
            pass
        
    def playanimate(self):
        self.after=self.root.after(1000,self.nextframe)

    def stopanimate(self):
        if self.after: self.root.after_cancel(self.after)
            
    def first(self):
        self.counter=0
        self.entry.setvalue(self.counter)
        self.drawframe()
        
    def drawframe(self):
        oldsc=self.sc
        self.sc=self.f(self.dialog,  self.frames[self.counter], font=self.font)
        if oldsc!=0:
            oldsc.destroy()
        self.sc.pack(side=TOP, fill='both', expand=1)
        
    def redraw_prev(self):
        if self.counter>0:
            self.counter=self.counter-1
            self.entry.setvalue(self.counter)
            self.drawframe()

    def redraw_next(self):
        if self.counter<len(self.frames)-1:
            self.counter=self.counter+1
            self.entry.setvalue(self.counter)
            self.drawframe()

    def last(self):
        self.counter=len(self.frames)-1
        self.entry.setvalue(self.counter)
        self.drawframe()

def ShowSingle(root, frame, f=showGraph, title='', save=None, font=default_font, help=None):
    ShowFrames(root,[frame], f, title, save, font, help)
    

