from csc321show import *
from csc321algorithms import *
from csc321frames import *
from Pmw import *
from copy import *

##########################################################
#
# SequenceAlignment
#
##########################################################

class SequenceAlignment:
    def Array2D(self,a,b,value=0):
        x=[]
        for i in range(a):
            y=[]
            for j in range(b):
                y.append(value)
            x.append(deepcopy(y))
        return x

    def __init__(self, root, selflist=None):
        self.save=selflist
        self.root=root
        self.dialog=Toplevel(root)
        self.dialog.title('Sequence Alignment')
        frame=Frame(self.dialog)
        Label(frame, text='Insert two DNA sequences (A,T,G,C) for alignment (Needlemand and Wunsch)', wraplength=200).pack(side=TOP, padx=5, pady=2)
        self.entry1=Pmw.EntryField(frame, labelpos=W, value='', label_text='DNA sequence S1:', entry_font=('Courier', 12))
        self.entry1.pack(side=TOP, padx=5, pady=2)
        self.entry2=Pmw.EntryField(frame, labelpos=W, value='', label_text='DNA sequence S2:', entry_font=('Courier', 12))
        self.entry2.pack(side=TOP, padx=5, pady=2)
        frame.pack(side=TOP, padx=5, pady=5)
        frame=Frame(self.dialog)        
        Button(frame, text='OK', command=self.alignGo).pack(side=LEFT)
        Button(frame, text='Cancel', command=self.alignCancel).pack(side=LEFT)
        frame.pack(side=TOP)
        self.dialog.resizable(false,false)        

    def alignCancel(self):
        self.dialog.destroy()

    def alignGo(self):
        S1=self.entry1.get()
        S2=self.entry2.get()
        L1=len(S1)
        L2=len(S2)
        A=self.Array2D(L2,L1,value=0)
        LCS=''
        minj=0
        frames=[]
        list=deepcopy(A[0])
        ColorList(list, 'white')
        if frames!=0:
            for j in range(0,L1):
                list[j].tag=0
                list[j].value=S1[j]
            newframe(frames,list)
        for i in xrange(L2):
            if minj==0:
                tag=0
            elif minj<L1:
                tag=A[i][minj-1]
            else:
                break
            for j in xrange(minj,L1):
                if S1[j]==S2[i]:
                    LCS=LCS+S1[j]
                    tag=tag+1
                    for k in range(i,L2):
                        for n in range(j,L1):
                            A[k][n]=tag

                    if frames!=0:
                        for k in range(0,L1):
                            list[k].tag=A[i][k]
                        list[j].color='green'    
                        for k in range(minj,j):
                            list[k].color='gray'
                        newframe(frames,list)

                    minj=j+1
                    break
        if frames!=0:
            for j in range(minj,L1):
                list[j].color='gray'
            newframe(frames,list)
            ShowFrames(self.root,frames,showList,title='Sequence Alignment',save=self.save)
            pass
        return






