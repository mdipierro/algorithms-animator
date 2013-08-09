from csc321show import *
from csc321algorithms import *
from csc321frames import *
from Pmw import *
from copy import *

##########################################################
#
# TicTacToe
#
##########################################################

class TicTacToe:

    def TicTacToeWin(self,list):
        circlelist=[]
        crosslist=[]
        i=0
        lenlist=len(list)
        while true:
            if i>=lenlist: break
            circlelist.append(list[i])
            i=i+1
            if i>=lenlist: break
            crosslist.append(list[i])
            i=i+1
            pass

        if 0 in circlelist and 1 in circlelist and 2 in circlelist: return 1
        if 3 in circlelist and 4 in circlelist and 5 in circlelist: return 1
        if 6 in circlelist and 7 in circlelist and 8 in circlelist: return 1
        if 0 in circlelist and 3 in circlelist and 6 in circlelist: return 1
        if 1 in circlelist and 4 in circlelist and 7 in circlelist: return 1
        if 2 in circlelist and 5 in circlelist and 8 in circlelist: return 1
        if 0 in circlelist and 4 in circlelist and 8 in circlelist: return 1
        if 2 in circlelist and 4 in circlelist and 6 in circlelist: return 1

        if 0 in crosslist and 1 in crosslist and 2 in crosslist: return 2
        if 3 in crosslist and 4 in crosslist and 5 in crosslist: return 2
        if 6 in crosslist and 7 in crosslist and 8 in crosslist: return 2
        if 0 in crosslist and 3 in crosslist and 6 in crosslist: return 2
        if 1 in crosslist and 4 in crosslist and 7 in crosslist: return 2
        if 2 in crosslist and 5 in crosslist and 8 in crosslist: return 2
        if 0 in crosslist and 4 in crosslist and 8 in crosslist: return 2
        if 2 in crosslist and 4 in crosslist and 6 in crosslist: return 2
        return 0

    def TicTacToeSub(self,tree,depth,n=9,sym=('X', 'O')):
        if depth>0:
            for i in range(n):
                if i not in tree[0].path:                
                    if divmod(depth,2)[1]==0:
                        node=[Node('%s %i' %(sym[0],i))]
                    else:
                        node=[Node('%s %i' %(sym[1],i))]
                        pass
                    node[0].path=[]
                    for k in tree[0].path+[i]: node[0].path.append(k)
                    node[0].data=node[0].path

                    a=self.TicTacToeWin(node[0].path)
                    
                    if a>0:
                        node[0].tag='Win'
                        node[0].winner=a
                        if a is 1:
                            node[0].color='red'
                        else:
                            node[0].color='blue'
                    else:
                        self.TicTacToeSub(node, depth-1, n, sym)
                    tree.append(node)

    def __init__(self,root,selftree=None):
        self.root=root
        self.save=selftree
        self.path=[]
        self.dialog=Toplevel(root, width=400)
        self.dialog.title('TicTacToe')
        frame9=Frame(self.dialog, borderwidth=2, relief=RIDGE)
        frame=Frame(frame9)
        frame.pack(side=TOP)
        self.b0=Button(frame,text='[0]',command=self.b0_click, width=4)
        self.b0.pack(side=LEFT, padx=2, pady=2)
        self.b1=Button(frame,text='[1]',command=self.b1_click, width=4)
        self.b1.pack(side=LEFT, padx=2, pady=2)
        self.b2=Button(frame,text='[2]',command=self.b2_click, width=4)
        self.b2.pack(side=LEFT, padx=2, pady=2)
        frame=Frame(frame9)
        frame.pack(side=TOP)
        self.b3=Button(frame,text='[3]',command=self.b3_click, width=4)
        self.b3.pack(side=LEFT, padx=2, pady=2)
        self.b4=Button(frame,text='[4]',command=self.b4_click, width=4)
        self.b4.pack(side=LEFT, padx=2, pady=2)
        self.b5=Button(frame,text='[5]',command=self.b5_click, width=4)
        self.b5.pack(side=LEFT, padx=2, pady=2)
        frame=Frame(frame9)
        frame.pack(side=TOP)
        self.b6=Button(frame,text='[6]',command=self.b6_click, width=4)
        self.b6.pack(side=LEFT, padx=2, pady=2)
        self.b7=Button(frame,text='[7]',command=self.b7_click, width=4)
        self.b7.pack(side=LEFT, padx=2, pady=2)
        self.b8=Button(frame,text='[8]',command=self.b8_click, width=4)
        self.b8.pack(side=LEFT, padx=2, pady=2)
        frame9.pack(side=TOP, padx=40, pady=10)
        Label(self.dialog,text='Game depth:').pack(side=TOP)
        self.depth=Scale(self.dialog, orient=HORIZONTAL, length=100, from_=1, to=9)
        self.depth.pack(side=TOP)
        frame=Frame(self.dialog)
        frame.pack(side=TOP)
        self.ok=Button(frame,text='OK',command=self.ok_click, width=6)
        self.ok.pack(side=LEFT)
        self.cancel=Button(frame,text='Cancel',command=self.cancel_click, width=6)
        self.cancel.pack(side=LEFT)
        self.dialog.resizable(false,false)
        
    def b0_click(self):
        if not 0 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(0)
            self.b0.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b1_click(self):
        if not 1 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(1)
            self.b1.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b2_click(self):
        if not 2 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(2)
            self.b2.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b3_click(self):
        if not 3 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(3)
            self.b3.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b4_click(self):
        if not 4 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(4)
            self.b4.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b5_click(self):
        if not 5 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(5)
            self.b5.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b6_click(self):
        if not 6 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(6)
            self.b6.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b7_click(self):
        if not 7 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(7)
            self.b7.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    def b8_click(self):
        if not 8 in self.path and not self.TicTacToeWin(self.path):
            self.path.append(8)
            self.b8.configure(text=('O','X')[divmod(len(self.path),2)[1]])
        pass
    
    def ok_click(self):
        depth=int(self.depth.get())            
        path=self.path
        if (depth-len(path))>5 or self.TicTacToeWin(self.path)>0:
            return
        tree=[Node('root', '')]
        tree[0].path=path
        tree[0].data=path
        if divmod(len(path)+depth,2)[1]==1: sym=('O', 'X')
        else: sym=('X','O')
        self.TicTacToeSub(tree, depth,9,sym)
        ShowSingle(self.root,tree,showTree,title='Tic Tac Toe',save=self.save)

    def cancel_click(self):
        self.dialog.destroy()
        pass
    
