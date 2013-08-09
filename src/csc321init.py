from csc321show import *
from csc321algorithms import *
from csc321frames import *
from csc321presentation import *
from csc321example_timingsort import *
from csc321example_tictactoe import *
from csc321example_huffman import *
from csc321example_alignment import *
from csc321example_allocation import *
#from csc321helptext import *
from csc321help import *
from csc321license import *
from csc321entries import *

from math import *
from copy import *
import time
import os
import sys
import Pmw
import pickle
import urllib
import tkFileDialog
import tkMessageBox
import tkColorChooser
import StringIO

helpfile=getHelpFileName()

class MainInterface:

    def Interactive(self):
        
        dialog=Pmw.TextDialog(self.root,scrolledtext_labelpos='n',
                              title='Enter Python Code',
                              label_text='program text:',
                              text_font=('Courier', 10))
        dialog.insert('end',self.interactive_text)
        dialog.activate()
        try:
            self.interactive_text=dialog.get()
            sys.stderr=sys.stdout=StringIO.StringIO()
            exec(dialog.get())
            sys.stdout.seek(0)
            output=sys.stdout.read()
            sys.stderr=sys.__stderr__
            sys.stdout=sys.__stdout__
            dialog=Pmw.TextDialog(self.root,scrolledtext_labelpos='n',
                                  title='Output',
                                  label_text='stdout+stderr:',
                                  text_font=('Courier', 10))
            dialog.insert('end',output)
            dialog.activate()
            
        except Exception, e:
            sys.stderr=sys.__stderr__
            sys.stdout=sys.__stdout__
            tkMessageBox.showwarning(ProgramName,'Error: '+str(e))
            
    def Register(self):
        pass

    def NoLicense(self):
        tkMessageBox.showinfo('Info', 'This function is disabled because this program is not registered.\nTo register visit www.phoenixcollective.org/mdp/index_csc321.html')

    def CheckUpdates(self):
        try:
            dialog=Toplevel(self.root,takefocus=1)
            label=Label(dialog,text='Connecting to website...')
            label.pack(padx=30, pady=20)
            dialog.focus_force()
            dialog.update()

            version=urllib.urlopen('http://www.phoenixcollective.org/mdp/CSC321/program_version.dat').read()
            if version!=ProgramName+'\n'+ProgramVersion+'\n':
                label.configure(text='Downloading auto update script...')
                dialog.update()
              	script=urllib.urlopen('http://www.phoenixcollective.org/mdp/CSC321/update_script.py').read()
                label.configure(text='Saving script to file...')
                dialog.update()
                file=open('csc321autoupdate.py','w')
                file.write(script)
                file.close()
                label.configure(text='Tranferring control to script...')
                dialog.update()
                execfile('csc321autoupdate.py')
                label.configure(text='Control back to CSC321!')
                dialog.update()
                time.sleep(1)                
            else:
                tkMessageBox.showinfo(ProgramName, 'No new versions of the program have been posted!')
            dialog.destroy()            
        except:
            dialog.destroy()            
            tkMessageBox.showwarning(ProgramName, 'Unable to connect to program web site.\nMissing internet connection or server down.')
            pass
        return

    def ExitProgram(self):
        ByeBye(self.root)

    def ListShow(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        ShowSingle(self.root,self.list,showList,title='self.list',
                   save=self.list,help=helpfile+'#List')
        return
    
    def ListCreate(self):
        dialog=Pmw.PromptDialog(self.root, title='Create List',
                                label_text='Input list:',
                                entryfield_labelpos='w',
                                entry_font=('Courier', 10),
                                buttons=('OK', 'Cancel'))
        if dialog.activate()!='OK': return
        try:
            list=eval(dialog.get())
            if list!=[]:
                ColorList(list)
                self.list[:]=list
                self.ListShow()
        except:
            tkMessageBox.showwarning(ProgramName, 'Invalid input list')
        return
    
    def ListLoad(self):
        filename=tkFileDialog.askopenfilename()
        if filename=='': return
        try:
            data=pickle.load(open(filename,'rb'))
            if data[0]!='csc321v2.self.list':
                raise 'Unable to open file'
            self.list[:]=data[1]
            self.ListShow()
        except:
            tkMessageBox.showwarning(ProgramName,'Unable to read: data in file is not type list')
        return

    def ListSave(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        filename=tkFileDialog.asksaveasfilename()
        if filename=='': return
        pickle.dump(['csc321v2.self.list', self.list],open(filename, 'wb'))
        return
    
    def ListAppendNode(self):
        node=EntryNode(self.root, title='Append Node to List')
        if not node: return
        self.list.append(node)
        self.ListShow()
        return

    def ListInsertNode(self):
        location=EntryLocation(self.root, len(self.list), title='Insert Node in List')
        if location is None: return
        node=EntryNode(self.root,Node())
        if node is None: return
        self.list.insert(location,node)
        self.ListShow()
        return
        
    def ListRemoveNode(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        location=EntryLocation(self.root, len(self.list), title='Remove Node from List')
        if location is None: return
        del self.list[location]
        self.ListShow()
        return

    def ListEditNode(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        location=EntryLocation(self.root, len(self.list), title='Edit List Node')
        if location is None: return
        node=deepcopy(self.list[location])
        node=EntryNode(self.root,node)
        if not node: return
        self.list[location]=node        
        self.ListShow()
        return

    def ListReset(self):
        self.list[:]=[]
        return                

    def ListSwapNodes(self):
        lmax=len(self.list)
        link=EntryLink(self.root,lmax,link=None,title='Swap Nodes')
        if not link: return
        i=link.source
        j=link.destination
        if i!=j:
            (self.list[i], self.list[j])=(self.list[j], self.list[i])
        self.ListShow()
        return

    def ListRandomize(self):
        lmax=len(self.list)
        for i in range(lmax):
            j=randint(0,lmax-1)
            if i!=j:
                (self.list[i], self.list[j])=(self.list[j], self.list[i])
        self.ListShow()
        return

    def ListStackPush(self):
        node=EntryNode(self.root, title='Push Node')
        if not node: return
        Push(self.list,node)
        self.ListShow()
        return                

    def ListStackPop(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'Stack is empty')
            return
        value=Pop(self.list).value
        tkMessageBox.showinfo('Stack Pop', 'value:' + repr(value))
        self.ListShow()
        return                

    def ListQueueEnqueue(self):
        node=EntryNode(self.root, title='Enqueue Node')
        if not node: return
        Enqueue(self.list,node)
        self.ListShow()
        return                

    def ListQueueDequeue(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'Queue is empty')
            return
        value=Dequeue(self.list).value
        tkMessageBox.showinfo('Stack Dequeue', 'value:' + repr(value))
        self.ListShow()        
        return                
    
    def ListInsertionSort(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        list=deepcopy(self.list)
        ColorList(list)
        frames=[]
        InsertionSortFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='InsertionSort',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsInsertionSort')
        return
        
    def ListMergeSort(self):        
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        list=deepcopy(self.list)
        ColorList(list)
        frames=[]
        MergeSortFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='MergeSort',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsMergeSort')
        return

    def ListMergeSortDP(self):        
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        list=deepcopy(self.list)
        ColorList(list)
        frames=[]
        MergeSortDPFrames(list,frames)
        ShowFrames(self.root, frames, showList,
                   title='MergeSortDP (non-recursive)',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsMergeSortDP')
        return

    def ListPartition(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        PartitionFrames(list,0,len(list),frames)
        ShowFrames(self.root, frames, showList, title='Partition',
                   save=self.list,
                   help=helpfile+'#ListOtherAlgorithmsPartition')
        return

    def ListQuickSort(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        QuickSortFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='QuickSort',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsQuickSort')
        return

    def ListRandomizedPartition(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        RandomizedPartitionFrames(list,0,len(list),frames)
        ShowFrames(self.root, frames, showList, title='RandomizedPartition',
                   save=self.list,
                   help=helpfile+'#ListOtherAlgorithmsRandomizedPartition')
        return

    def ListRandomizedQuickSort(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        RandomizedQuickSortFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='Randomized QuickSort',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsRandomizedQuickSort')
        return

    def ListHeapify(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        location=EntryLocation(self.root, len(self.list), title='Heapify Starting Node')
        if location is None: return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        HeapifyFrames(list,location,frames)
        ShowFrames(self.root, frames, showList, title='Heapify',
                   save=self.list,
                   help=helpfile+'#ListHeapAlgorithmsHeapify')
        return

    def ListBuildHeap(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        BuildHeapFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='BuildHeap',
                   save=self.list,
                   help=helpfile+'#ListHeapAlgorithmsBuildHeap')
        return

    def ListHeapExtractMax(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        BuildHeap(list)
        tkMessageBox.showinfo('HeapExtractMax', 'value:' + repr(list[0]))
        HeapExtractMaxFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='HeapExtractMax',
                   save=self.list,
                   help=helpfile+'#ListHeapAlgorithmsHeapExtractMax')
        return                

    def ListHeapInsert(self):
        list=deepcopy(self.list)
        BuildHeap(list)
        node=EntryNode(self.root, title='HeapInsert')
        if not node: return 
        frames=[]
        ColorList(list)
        HeapInsertFrames(list,node,frames)
        ShowFrames(self.root, frames, showList, title='HeapInsert',
                   save=self.list,
                   help=helpfile+'#ListHeapAlgorithmsHeapInsert')
        return
    
    def ListHeapSort(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        HeapSortFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='HeapSort',
                   save=self.list,
                   help=helpfile+'#ListSortAlgorithmsHeapSort')
        return

    def ListCountingSort(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        try:
            CountingSortFrames(list,frames)
            ShowFrames(self.root, frames, showTree, title='CountingSort',
                       save=None,
                       help=helpfile+'#ListSortAlgorithmsCountingSort')
        except:
            tkMessageBox.showwarning(ProgramName, 'List values are not integers or are too sparse')
        return
    
    def ListMinimum(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        i=MinimumFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='Minimum',
                   save=self.list,
                   help=helpfile+'#ListOtherAlgorithmsMinimum')
        tkMessageBox.showinfo('Minimum', 'value:' + repr(i))
        return

    def ListMaximum(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        frames=[]
        list=deepcopy(self.list)
        ColorList(list)
        i=MaximumFrames(list,frames)
        ShowFrames(self.root, frames, showList, title='Maximum',
                   save=self.list,
                   help=helpfile+'#ListOtherAlgorithmsMaximum')
        tkMessageBox.showinfo('Maximum', 'value:' + repr(i))
        return                

    def TreeReset(self):
        self.tree[:]=[]
        return                

    def TreeShow(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        ShowSingle(self.root,self.tree,showTree,title='self.tree',
                   save=self.tree,
                   help=helpfile+'#Tree')
        return

    def TreeCreate(self):
        dialog=Pmw.PromptDialog(self.root, title='Create Tree',
                                label_text='Input tree:',
                                entryfield_labelpos='w',
                                entry_font=('Courier', 10),
                                buttons=('OK', 'Cancel'))
        if dialog.activate()!='OK': return
        try:
            tree=eval(dialog.get())
            ColorTree(tree)
            self.tree[:]=tree
            self.TreeShow()
        except:
            tkMessageBox.showwarning(ProgramName, 'Invalid input tree')
        return

    def TreeLoad(self):
        filename=tkFileDialog.askopenfilename()
        if filename=='': return
        try:
            data=pickle.load(open(filename,'rb'))
            if data[0]!='csc321v2.self.tree':
                raise 'Unable to open file'
            self.tree[:]=data[1]
            self.TreeShow()
        except:
            tkMessageBox.showwarning(ProgramName,'Unable to read: data in file is not type tree')
        return

    def TreeSave(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        filename=tkFileDialog.asksaveasfilename()
        if filename=='': return
        pickle.dump(['csc321v2.self.tree', self.tree],open(filename, 'wb'))
        return

    def TreeRemoveNode(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        location=EntryLocation(self.root, treeSize(self.tree), title='Remove Node from Tree')
        if location is None: return
        delTreeNode(self.tree,location) 
        self.TreeShow()
        return

    def TreeEditNode(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        location=EntryLocation(self.root, treeSize(self.tree), title='Edit Tree Node')
        if location is None: return
        node=deepcopy(getTreeNode(self.tree, location))
        node=EntryNode(self.root,node)
        if not node: return
        setTreeNode(self.tree,location,node)
        self.TreeShow()
        return


    def TreeAppendNode(self):
        if treeSize(self.tree)>0:
            location=EntryLocation(self.root, treeSize(self.tree), title='Append Node to Tree')
            if location is None: return        
            node=EntryNode(self.root,Node())
            if not node: return
            appendTreeNode(self.tree,location,node)
        else:
            node=EntryNode(self.root,Node())
            if not node: return
            self.tree=BinaryTree(node)
        self.TreeShow()
        return

    def TreeHeapify(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        list=Heap2List(self.tree)
        location=EntryLocation(self.root, len(list), title='Starting Node (list index)')
        if location is None: return
        frames=[]
        ColorList(list)
        HeapifyFrames(list,location,frames)
        for i in range(len(frames)):
            frames[i]=List2Heap(frames[i])
            pass
        ShowFrames(self.root, frames, showTree, title='Heapify',
                   save=self.tree,
                   help=helpfile+'#ListHeapAlgorithmsHeapify')
        return

    def TreeBuildHeap(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        frames=[]
        list=Heap2List(self.tree)
        ColorList(list)
        BuildHeapFrames(list,frames)
        for i in range(len(frames)):
            frames[i]=List2Heap(frames[i])
            pass
        ShowFrames(self.root, frames, showTree, title='BuildHeap',
                   save=self.tree,
                   help=helpfile+'#TreeHeapAlgorithms')
        return

    def TreeHeapExtractMax(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        frames=[]
        list=Heap2List(self.tree)
        ColorList(list)
        BuildHeap(list)
        tkMessageBox.showinfo('HeapExtractMax', 'value:' + repr(list[0]))
        HeapExtractMaxFrames(list,frames)
        for i in range(len(frames)):
            frames[i]=List2Heap(frames[i])
            pass
        ShowFrames(self.root, frames, showTree, title='HeapExtractMax',
                   save=self.tree,
                   help=helpfile+'#TreeHeapAlgorithms')
        return                

    def TreeHeapInsert(self):
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        node=EntryNode(self.root, title='HeapInsert')
        if not node: return
        if len(self.tree)==0:
            frames=[List2Heap([node])]
        else:
            frames=[]
            list=Heap2List(self.tree)
            ColorList(list)
            HeapInsertFrames(list,node,frames)
            for i in range(len(frames)):
                frames[i]=List2Heap(frames[i])
                pass
        ShowFrames(self.root, frames, showTree, title='HeapInsert',
                   save=self.tree,
                   help=helpfile+'#TreeHeapAlgorithms')
        return                

    def TreeHeapSort(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        frames=[]
        list=Heap2List(self.tree)
        ColorList(list)
        HeapSortFrames(list,frames)
        for i in range(len(frames)):
            frames[i]=List2Heap(frames[i])
            pass
        ShowFrames(self.root, frames, showTree, title='HeapSort',
                   save=self.tree,
                   help=helpfile+'#ListSortAlgorithmsHeapSort')
        return

    def ConvertList2BinaryTree(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        list=deepcopy(self.list)
        self.tree[:]=List2BinaryTree(list)
        self.TreeShow()
        return

    def TreeBSTInorderWalk(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        frames=[]
        list=BSTInorderWalkFrames(tree,[],frames,fulltree=None)
        ShowFrames(self.root,frames,showTree, title='BST-InorderWalk',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsInorderTreeWalk')

    def TreeBSTSearch(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        dialog1=Pmw.PromptDialog(self.root,
                                 title='BST-Search',
                                 label_text='Node value:',
                                 entryfield_labelpos='w',
                                 entry_font=('Courier', 10),
                                 buttons=('OK', 'Cancel'))
        if dialog1.activate()!='OK': return
        try:
            i=eval(dialog1.get())
        except:
            i=dialog1.get()
        frames=[]
        BSTSearchFrames(tree,i,frames,fulltree=None)
        ShowFrames(self.root,frames,showTree, title='TreeSearch',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsTreeSearch')

    def TreeBSTMinimum(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        frames=[]
        t=BSTMinimum(tree)
        BSTSearchFrames(tree,t[rootnode],frames,fulltree=None)
        ShowFrames(self.root,frames,showTree, title='BST-Minimum',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsTreeMinimum')
        
    def TreeBSTMaximum(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        frames=[]
        t=BSTMaximum(tree)
        BSTSearchFrames(tree,t[rootnode],frames,None)
        ShowFrames(self.root,frames,showTree, title='BST-Maximum',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsTreeMaximum')

    def TreeBSTInsert(self):
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        node=EntryNode(self.root, title='BST-Insert')
        if not node: return
        frames=[]
        BSTInsertFrames(tree,node,frames)
        ShowFrames(self.root,frames,showTree, title='BST-Insert',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsTreeInsert')
        return

    def TreeBSTDelete(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        location=EntryLocation(self.root, treeSize(self.tree), title='Tree Delete Node')
        if location is None: return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        BSTDeleteIndex(tree,location)
        ShowSingle(self.root,tree,showTree,title='BST-Delete',
                   save=self.tree,
                   help=helpfile+'#TreeBinaryTreeAlgorithmsTreeDelete')


    def ConvertList2AVLTree(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        list=deepcopy(self.list)
        self.tree[:]=List2AVLTree(list)
        self.TreeShow()
        return

    def TreeAVLRebalanceNode(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        location=EntryLocation(self.root, treeSize(self.tree), title='AVL-RebalanceNode')
        if location is None: return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        AVLRebalanceNodeIndex(tree,location)
        ShowSingle(self.root,tree,showTree,title='AVL-RebalanceNode',
                   save=self.tree,
                   help=helpfile+'#TreeAVLTreeAlgorithmsRebalanceNode')
        pass

    def TreeAVLInsert(self):
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        node=EntryNode(self.root, title='AVL-TreeInsert')
        if not node: return
        frames=[]
        BSTInsertFrames(tree,node,frames)
        frames.append(deepcopy(frames[-1]))
        AVLRebalanceTree(frames[-1])        
        ShowFrames(self.root,frames,showTree, title='BST-Insert',
                   save=self.tree,
                   help=helpfile+'#TreeAVLTreeAlgorithmsAVL-TreeInsert')
        return

    def TreeAVLDelete(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isBinaryTree(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Binary Tree')
            return
        location=EntryLocation(self.root, treeSize(self.tree), title='AVL-TreeDelete')
        if location is None: return
        tree=deepcopy(self.tree)
        ColorTree(tree)
        BSTDeleteIndex(tree,location)
        AVLRebalanceTree(tree)        
        ShowSingle(self.root,tree,showTree,title='BST-Delete',
                   save=self.tree,
                   help=helpfile+'#TreeAVLTreeAlgorithmsAVL-TreeDelete')

    def TreeHeigth(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        i=treeHeight(self.tree)
        tkMessageBox.showinfo(ProgramName, 'Tree Heigth: %i' % (i))

    def GraphReset(self):
        self.graph[:]=[[], []]
        return                

    def GraphShow(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        ShowSingle(self.root,self.graph,showGraph,title='self.graph',
                   save=self.graph,
                   help=helpfile+'#Graph')
        return
    
    def GraphCreate(self):
        dialog=Pmw.PromptDialog(self.root, title='Create Graph',
                                label_text='Input graph:',
                                entryfield_labelpos='w',
                                entry_font=('Courier', 10),
                                buttons=('OK', 'Cancel'))
        if dialog.activate()!='OK': return
        try:
            graph=eval(dialog.get())
            ColorGraph(graph)
            self.graph[:]=graph
            self.GraphShow()
        except:
            tkMessageBox.showwarning(ProgramName, 'Invalid input graph')
        return

    def GraphLoad(self):
        filename=tkFileDialog.askopenfilename()
        if filename=='': return
        try:
            data=pickle.load(open(filename,'rb'))
            if data[0]!='csc321v2.self.graph':
                raise 'Unable to open file'
            self.graph[:]=data[1]
            self.GraphShow()
        except:
            tkMessageBox.showwarning(ProgramName,'Unable to read: data in file is not type graph')
        return

    def GraphSave(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        filename=tkFileDialog.asksaveasfilename()
        if filename=='': return
        pickle.dump(['csc321v2.self.graph',self.graph],open(filename, 'wb'))
        return

    def GraphAppendVertex(self):
        node=EntryNode(self.root,title='Append Vertex to Graph')
        if not node: return
        self.graph[0].append(node)                
        self.GraphShow()
        return

    def GraphAppendLink(self):
        l=len(self.graph[0])
        if l is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        link=EntryLink(self.root,l,Link(),title='Append Link to Graph')
        if link:
            self.graph[1].append(link)
            self.GraphShow()
        return

    def GraphRemoveVertex(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        i=EntryLocation(self.root, len(vertices), title='Remove Vertex from Graph')
        if i is None: return
        links=self.graph[1]
        del vertices[i]
        k=0
        while k<len(links):
            link=links[k]
            if link.source==i or link.destination==i:
                del links[k]
            else:
                k=k+1
            pass
        for link in links:
            if link.source>i: link.source=link.source-1
            if link.destination>i: link.destination=link.destination-1
        self.GraphShow()
        return

    def GraphRemoveLink(self):
        l=len(self.graph[0])
        if l is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        link=EntryLink(self.root,l,title='Remove Link from Graph')
        if not link: return
        links=self.graph[1]
        for k in range(len(links)):
            if link.source==links[k].source and link.destination==links[k].destination:
                del links[k]
                break
        self.GraphShow()
        return

    def GraphEditVertex(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        location=EntryLocation(self.root, len(vertices),
                               title='Edit Graph Vertex')
        if location is None: return
        node=deepcopy(vertices[location])
        node=EntryNode(self.root,node)
        if not node: return
        vertices[location]=node        
        self.GraphShow()
        return

    def GraphEditLink(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        l=len(self.graph[0])
        link=EntryLink(self.root,l,None,title='Edit Graph Link')
        if not link: return
        links=self.graph[1]
        for k in range(len(links)):
            if link.source==links[k].source and link.destination==links[k].destination:
                link=EntryLink(self.root,l,links[k],title='Edit Graph Link')
                if link:
                    links[k]=link
                    self.GraphShow()
                return
        tkMessageBox.showwarning(ProgramName, 'No such link')
        return

    def GraphShowMatrix(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        ShowSingle(self.root,self.graph,showGraphAsMatrix,
                   title='graph->matrix')
        return

    def GraphSymmetrize(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        SymmetrizeGraph(self.graph)
        self.GraphShow()
        return

    def ConvertHeap2List(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        if not isHeap(self.tree):
            tkMessageBox.showwarning(ProgramName, 'This Tree is not a Heap')
            return
        self.list[:]=Heap2List(self.tree)
        ColorList(self.list)
        self.ListShow()
        return

    def ConvertList2Tree(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        self.tree[:]=List2Tree(deepcopy(self.list))
        self.TreeShow()
        return

    def ConvertList2Heap(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')            
            return
        self.tree[:]=List2Heap(deepcopy(self.list))
        self.TreeShow()
        return

    def ConvertList2Graph(self):
        if len(self.list) is 0:
            tkMessageBox.showwarning(ProgramName, 'List is empty')
            return
        self.graph[:]=List2Graph(deepcopy(self.list))
        self.GraphShow()
        return

    def ConvertTree2Graph(self):
        if len(self.tree) is 0:
            tkMessageBox.showwarning(ProgramName, 'Tree is empty')
            return
        self.graph[:]=Tree2Graph(deepcopy(self.tree),0)
        self.GraphShow()
        return

    def GraphBreadthFirstSearch(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'Breadth First Search')
        if start is None: return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        BreadthFirstSearchFrames(graph, start,frames)
        ShowFrames(self.root, frames, showGraph, title='Breadth First Search',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsBreadthFirstSearch')
        return

    def GraphDepthFirstSearch(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'Depth First Search')
        if start is None: return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        DepthFirstSearchFrames(graph, start,frames)
        ShowFrames(self.root, frames, showGraph, title='Depth First Search',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsDepthFirstSearch')
        return

    def GraphBFSTopologicalSort(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'BFS Topological Sort')
        if start is None: return
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        list=TopologicalSort(graph,start,BreadthFirstSearch)
        ShowSingle(self.root,list,showList,
                   title='BFS Topological Sort -> list',
                   save=self.list,
                   help=helpfile+'#GraphAlgorithmsBFS-TopologicalSort')
        return

    def GraphDFSTopologicalSort(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'DFS Topological Sort')
        if start is None: return
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        list=TopologicalSort(graph,start,DepthFirstSearch)
        ShowSingle(self.root,list,showList,
                   title='DFS Topological Sort -> list',
                   save=self.list,
                   help=helpfile+'#GraphAlgorithmsDFS-TopologicalSort')
        return

    def GraphMSTKruskal(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        MSTKruskalFrames(graph,frames)
        ShowFrames(self.root, frames, showGraph, title='MSTKruskal',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsMST-Kruskal')
        return

    def GraphMSTPrim(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'MSTPrim')
        if start is None: return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        MSTPrimFrames(graph, start,frames)
        ShowFrames(self.root, frames, showGraph, title='MSTPrim',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsMST-Prim')
        return

    def GraphDijkstra(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'Dijkstra')
        if start is None: return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        DijkstraFrames(graph, start,frames)
        ShowFrames(self.root, frames, showGraph, title='Dijkstra',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsDijkstra')
        return

    def GraphBellmanFord(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        vertices=self.graph[0]
        start=EntryLocation(self.root, len(vertices), 'BellmanFord')
        if start is None: return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        ret=BellmanFordFrames(graph, start,frames)
        ShowFrames(self.root, frames, showGraph, title='BellmanFord',
                   save=self.graph,
                   help=helpfile+'#GraphAlgorithmsBellman-Ford')
        if not ret:
            tkMessageBox.showwarning(ProgramName, 'BellmanFord did not find the cycle')
        return
    
    def CreateRandomList(self):        
        size=EntryLocation(self.root,21,title='Random List',
                           label='Size:',
                           question='List size:')
        if size:
            self.list[:]=[]
            for i in range(size): self.list.append(Node(randint(0,999)))
            self.ListShow()

    def ListTimingSort(self):
        TimingSort(self.root)
    
    def ExampleTicTacToe(self):
        TicTacToe(self.root)
        return

    def ExampleHuffmanEncoding(self):
        HuffmanEncoding(self.root)
        return
    
    def ExampleSequenceAlignment(self):
        SequenceAlignment(self.root)
        return
    
    def ExampleResourceAllocation(self):
        ResourceAllocation(self.root)
        return

    def GraphFiniteStateMachine(self):
        if len(self.graph[0]) is 0:
            tkMessageBox.showwarning(ProgramName, 'Graph is empty')
            return
        for link in self.graph[1]:
            if type(link.length)!=type({}):
                tkMessageBox.showwarning(ProgramName, 'Graph is not a Finite State Machine')
                return
        dialog=Pmw.TextDialog(self.root,scrolledtext_labelpos='n',
                              title='Enter Input for the Finite State Machine',
                              label_text='input:',
                              text_font=('Courier', 10))
        dialog.activate()
        s=dialog.get()
        if s is '': return
        frames=[]
        graph=deepcopy(self.graph)
        ColorGraph(graph)
        history, output=RunFiniteStateMachineFrames(graph,s[:-1],frames)
        dialog = Pmw.TextDialog(self.root, scrolledtext_labelpos = 'n',
                                title ='Finite State Machine',
                                defaultbutton = 0,
                                label_text = ProgramName+'Input/Output')
        dialog.insert('end', 'INPUT:\n%s\n\nHISTORY:\n%s\n\nOUTPUT:\n%s' %(s,history,output))
        dialog.configure(text_state = 'disabled')
        ShowFrames(self.root, frames, showGraph, title='Running Finite State Machine',
                   save=self.graph,
                   help=helpfile+'#GraphFiniteStateMachine')
        return

    def HelpSearch(self):
        try:
            os.system('explorer.exe '+helpfile)
        except:
            tkMessageBox.showwarning(ProgramName, 'Problem connecting to Explorer')
            
    def HelpLicense(self):        
        dialog = Pmw.TextDialog(self.root, scrolledtext_labelpos = 'n',
                                title = ProgramName+' License Agreement',
                                defaultbutton = 0,
                                label_text = ProgramName+' License Agreement')
        dialog.insert('end', License)
        dialog.configure(text_state = 'disabled')  

    def HelpAbout(self):
        tkMessageBox.showinfo('About '+ProgramName, 
                              ProgramName+'\n\n'+
                              'Created by Massimo Di Pierro\n'+
                              ProgramVersion + '\n\n'+
                              'Massimo Di Pierro \n'+
                              'DePaul CTI\n'+
                              '243 S. Wabash Av. \n'+
                              'Chicago, IL 60604 \n'+
                              'Email: mdipierro@cs.depaul.edu')

    def Sorry(self):
        tkMessageBox.showinfo('CSC321', 'Sorry, not implemented')

    def __init__(self):
        self.interactive_text="print 'hello Animator'"
        self.active=CheckLicense()
        self.root=Tk()
        self.balloon=Pmw.Balloon(self.root)
        self.root.title(ProgramName)
        
        self.list=[]
        ColorList(self.list)
        self.tree=[]
        ColorTree(self.tree)
        self.graph=[[], []]
        ColorGraph(self.graph)

        mBar=Frame(self.root, relief=RAISED, borderwidth=2)
        mBar.pack(fill=X, expand=false)

        FileMenu=Menubutton(mBar, text='File', underline=0)
        FileMenu.pack(side=LEFT,padx='2m')
        FileMenu.menu=Menu(FileMenu)
        
        FileMenu.menu.add_command(label='Interactive',
                                  command=self.Interactive)
        #FileMenu.menu.add_command(label='Register',
        #                          command=self.Register)
        #FileMenu.menu.add_command(label='Check updates',
        #                          command=self.CheckUpdates)
        FileMenu.menu.add_command(label='Exit',
                                  command=self.ExitProgram)
        FileMenu['menu']=FileMenu.menu

        ListMenu=Menubutton(mBar, text='List', underline=0)
        ListMenu.pack(side=LEFT,padx='2m')
        ListMenu.menu=Menu(ListMenu)
        ListMenu.menu.add_command(label='Show', command=self.ListShow)
        ListMenu.menu.add_command(label='Create', command=self.ListCreate)
        ListMenu.menu.add_command(label='Create Random List',
                                  command=self.CreateRandomList)        
        ListMenu.menu.add_command(label='Load', command=self.ListLoad)
        if self.active:
            ListMenu.menu.add_command(label='Save As', command=self.ListSave)
        else:
            ListMenu.menu.add_command(label='Save As', command=self.NoLicense)
        ListMenu.menu.add_command(label='Reset',
                                  command=self.ListReset)
        ListMenu.menu.add_command(label='Append Node',
                                  command=self.ListAppendNode)
        ListMenu.menu.add_command(label='Insert Node',
                                  command=self.ListInsertNode)
        ListMenu.menu.add_command(label='Remove Node',
                                  command=self.ListRemoveNode)
        ListMenu.menu.add_command(label='Edit Node',
                                  command=self.ListEditNode)

        ListMenu.menu.order=Menu(ListMenu.menu)
        ListMenu.menu.order.add_command(label='Swap',
                                       command=self.ListSwapNodes)
        ListMenu.menu.order.add_command(label='Randomize',
                                       command=self.ListRandomize)
        ListMenu.menu.add_cascade(label='Reordering Algorithms',
                                  menu=ListMenu.menu.order)


        ListMenu.menu.stack=Menu(ListMenu.menu)
        ListMenu.menu.stack.add_command(label='Push',
                                       command=self.ListStackPush)
        ListMenu.menu.stack.add_command(label='Pop',
                                       command=self.ListStackPop)
        ListMenu.menu.add_cascade(label='Stack Algorithms',
                                  menu=ListMenu.menu.stack)

        ListMenu.menu.queue=Menu(ListMenu.menu)
        ListMenu.menu.queue.add_command(label='Enqueue',
                                       command=self.ListQueueEnqueue)
        ListMenu.menu.queue.add_command(label='Dequeue',
                                       command=self.ListQueueDequeue)
        ListMenu.menu.add_cascade(label='Queue Algorithms',
                                  menu=ListMenu.menu.queue)

        ListMenu.menu.heap=Menu(ListMenu.menu)
        ListMenu.menu.heap.add_command(label='Heapify',
                                             command=self.ListHeapify)
        ListMenu.menu.heap.add_command(label='BuildHeap',
                                             command=self.ListBuildHeap)
        ListMenu.menu.heap.add_command(label='HeapExtractMax',
                                             command=self.ListHeapExtractMax)
        ListMenu.menu.heap.add_command(label='HeapInsert',
                                             command=self.ListHeapInsert)
        ListMenu.menu.heap.add_command(label='HeapSort',
                                             command=self.ListHeapSort)
        ListMenu.menu.heap.add_command(label='tree(heap)->list',
                                       command=self.ConvertHeap2List)
        ListMenu.menu.add_cascade(label='Heap Algorithms',
                                  menu=ListMenu.menu.heap)


        ListMenu.menu.sortalgorithms=Menu(ListMenu.menu)
        ListMenu.menu.sortalgorithms.add_command(label='InsertionSort',
                                             command=self.ListInsertionSort)
        ListMenu.menu.sortalgorithms.add_command(label='MergeSort',
                                             command=self.ListMergeSort)
        ListMenu.menu.sortalgorithms.add_command(label='MergeSortDP',
                                             command=self.ListMergeSortDP)
        ListMenu.menu.sortalgorithms.add_command(label='QuickSort',
                                             command=self.ListQuickSort)
        ListMenu.menu.sortalgorithms.add_command(label='Randomized QuickSort',
                                             command=self.ListRandomizedQuickSort)
        ListMenu.menu.sortalgorithms.add_command(label='HeapSort',
                                             command=self.ListHeapSort)
        ListMenu.menu.sortalgorithms.add_command(label='CountingSort',
                                             command=self.ListCountingSort)
        
        ListMenu.menu.add_cascade(label='Sort Algorithms',
                                  menu=ListMenu.menu.sortalgorithms)
        ListMenu['menu']=ListMenu.menu
        
        ListMenu.menu.other=Menu(ListMenu.menu)
        ListMenu.menu.other.add_command(label='Partition',
                                        command=self.ListPartition)
        ListMenu.menu.other.add_command(label='Randomized Partition',
                                        command=self.ListRandomizedPartition)
        ListMenu.menu.other.add_command(label='Minimum',
                                        command=self.ListMinimum)
        ListMenu.menu.other.add_command(label='Maximum',
                                        command=self.ListMaximum)
        ListMenu.menu.add_cascade(label='Other Algorithms',
                                  menu=ListMenu.menu.other)
        ListMenu['menu']=ListMenu.menu


        TreeMenu=Menubutton(mBar, text='Tree', underline=0)
        TreeMenu.pack(side=LEFT,padx='2m')
        TreeMenu.menu=Menu(TreeMenu)
        TreeMenu.menu.add_command(label='Show', command=self.TreeShow)
        TreeMenu.menu.add_command(label='Create', command=self.TreeCreate)
        TreeMenu.menu.add_command(label='Load', command=self.TreeLoad)
        if self.active:
            TreeMenu.menu.add_command(label='Save As', command=self.TreeSave)
        else:
            TreeMenu.menu.add_command(label='Save As', command=self.NoLicense)
        TreeMenu.menu.add_command(label='Reset',
                                  command=self.TreeReset)
        TreeMenu.menu.add_command(label='Append Node',
                                  command=self.TreeAppendNode)
        TreeMenu.menu.add_command(label='Remove Node',
                                  command=self.TreeRemoveNode)
        TreeMenu.menu.add_command(label='Edit Node',
                                  command=self.TreeEditNode)
        TreeMenu.menu.heap=Menu(TreeMenu.menu)
        TreeMenu.menu.heap.add_command(label='list->tree(heap)',
                                       command=self.ConvertList2Heap)
        TreeMenu.menu.heap.add_command(label='Heapify',
                                       command=self.TreeHeapify)
        TreeMenu.menu.heap.add_command(label='BuildHeap',
                                       command=self.TreeBuildHeap)
        TreeMenu.menu.heap.add_command(label='HeapExtractMax',
                                             command=self.TreeHeapExtractMax)
        TreeMenu.menu.heap.add_command(label='HeapInsert',
                                             command=self.TreeHeapInsert)
        TreeMenu.menu.heap.add_command(label='HeapSort',
                                       command=self.TreeHeapSort)
        TreeMenu.menu.add_cascade(label='Heap Algorithms',
                                  menu=TreeMenu.menu.heap)
        TreeMenu.menu.binary=Menu(TreeMenu.menu)
        TreeMenu.menu.binary.add_command(label='list->tree(binary)',
                                         command=self.ConvertList2BinaryTree)
        TreeMenu.menu.binary.add_command(label='BST-InorderWalk',
                                         command=self.TreeBSTInorderWalk)
        TreeMenu.menu.binary.add_command(label='BST-Search',
                                         command=self.TreeBSTSearch)
        TreeMenu.menu.binary.add_command(label='BST-Minimum',
                                         command=self.TreeBSTMinimum)
        TreeMenu.menu.binary.add_command(label='BST-Maximum',
                                         command=self.TreeBSTMaximum)
        TreeMenu.menu.binary.add_command(label='BST-Insert',
                                         command=self.TreeBSTInsert)
        TreeMenu.menu.binary.add_command(label='BST-Delete',
                                         command=self.TreeBSTDelete)
        TreeMenu.menu.add_cascade(label='Binary Search Tree Algorithms',
                                  menu=TreeMenu.menu.binary)

        TreeMenu.menu.avl=Menu(TreeMenu.menu)
        TreeMenu.menu.avl.add_command(label='list->tree(AVL)',
                                      command=self.ConvertList2AVLTree)
        TreeMenu.menu.avl.add_command(label='AVL-RebalanceNode',
                                      command=self.TreeAVLRebalanceNode)
        TreeMenu.menu.avl.add_command(label='AVL-Insert',
                                      command=self.TreeAVLInsert)
        TreeMenu.menu.avl.add_command(label='AVL-Delete',
                                      command=self.TreeAVLDelete)
        TreeMenu.menu.add_cascade(label='AVL Tree Algorithms',
                                  menu=TreeMenu.menu.avl)

        TreeMenu.menu.other=Menu(TreeMenu.menu)
        TreeMenu.menu.other.add_command(label='Measure Tree Heigth',
                                        command=self.TreeHeigth)
        TreeMenu.menu.add_cascade(label='Other Algorithms',
                                  menu=TreeMenu.menu.other)

        TreeMenu.menu.add_command(label='list->tree',
                                  command=self.ConvertList2Tree)
        TreeMenu['menu']=TreeMenu.menu

        GraphMenu=Menubutton(mBar, text='Graph', underline=0)
        GraphMenu.pack(side=LEFT,padx='2m')
        GraphMenu.menu=Menu(GraphMenu)
        GraphMenu.menu.add_command(label='Show', command=self.GraphShow)
        GraphMenu.menu.add_command(label='Create', command=self.GraphCreate)
        GraphMenu.menu.add_command(label='Load', command=self.GraphLoad)
        if self.active:
            GraphMenu.menu.add_command(label='Save As', command=self.GraphSave)
        else:
            GraphMenu.menu.add_command(label='Save As', command=self.NoLicense)
        GraphMenu.menu.add_command(label='Reset',
                                  command=self.GraphReset)
        GraphMenu.menu.add_command(label='Append Vertex',
                                   command=self.GraphAppendVertex)
        GraphMenu.menu.add_command(label='Append Link',
                                   command=self.GraphAppendLink)
        GraphMenu.menu.add_command(label='Remove Vertex',
                                   command=self.GraphRemoveVertex)
        GraphMenu.menu.add_command(label='Remove Link',
                                   command=self.GraphRemoveLink)
        GraphMenu.menu.add_command(label='Edit Vertex',
                                   command=self.GraphEditVertex)
        GraphMenu.menu.add_command(label='Edit Link',
                                   command=self.GraphEditLink)
        GraphMenu.menu.add_command(label='Show Matrix',
                                   command=self.GraphShowMatrix)
        GraphMenu.menu.algorithms=Menu(GraphMenu.menu)
        GraphMenu.menu.algorithms.add_command(label='Symmetrize',
                                              command=self.GraphSymmetrize)
        GraphMenu.menu.algorithms.add_command(label='BreadthFirstSearch',
                                              command=self.GraphBreadthFirstSearch)
        #GraphMenu.menu.algorithms.add_command(label='BFSTopologicalSort',
        #                                      command=self.GraphBFSTopologicalSort)
        GraphMenu.menu.algorithms.add_command(label='DepthFirstSearch',
                                              command=self.GraphDepthFirstSearch)
        #GraphMenu.menu.algorithms.add_command(label='DFSTopologicalSort',
        #                                      command=self.GraphDFSTopologicalSort)
        GraphMenu.menu.algorithms.add_command(label='MSTKruskal',
                                              command=self.GraphMSTKruskal)
        GraphMenu.menu.algorithms.add_command(label='MSTPrim',
                                              command=self.GraphMSTPrim)
        GraphMenu.menu.algorithms.add_command(label='Dijkstra',
                                              command=self.GraphDijkstra)
        GraphMenu.menu.algorithms.add_command(label='BellmanFord',
                                              command=self.GraphBellmanFord)
        GraphMenu.menu.add_cascade(label='Algorithms',
                                   menu=GraphMenu.menu.algorithms)        
        GraphMenu.menu.add_command(label='Run as Finite State Machine',
                                   command=self.GraphFiniteStateMachine)        
        GraphMenu.menu.add_command(label='list->graph',
                                   command=self.ConvertList2Graph)
        GraphMenu.menu.add_command(label='tree->graph',
                                   command=self.ConvertTree2Graph)
        GraphMenu['menu']=GraphMenu.menu

        ExamplesMenu=Menubutton(mBar, text='Examples', underline=0)
        ExamplesMenu.pack(side=LEFT,padx='2m')
        ExamplesMenu.menu=Menu(ExamplesMenu)
        ExamplesMenu.menu.add_command(label='Timing Sort Algorithms',
                                      command=self.ListTimingSort)        
        
        ExamplesMenu.menu.add_command(label='TicTacToe',
                                      command=self.ExampleTicTacToe)
        ExamplesMenu.menu.add_command(label='Huffman Encoding',
                                      command=self.ExampleHuffmanEncoding)
        ExamplesMenu.menu.add_command(label='Sequence Alignment',
                                      command=self.ExampleSequenceAlignment)
        #ExamplesMenu.menu.add_command(label='Fractional Knapsack (*)',
        #                              command=self.Sorry)
        #ExamplesMenu.menu.add_command(label='Discrete Knapsack (*)',
        #                              command=self.Sorry)
        #ExamplesMenu.menu.add_command(label='Resource Allocation',
        #                              command=self.ExampleResourceAllocation)

        ExamplesMenu['menu']=ExamplesMenu.menu

        HelpMenu=Menubutton(mBar, text='Help', underline=0)
        HelpMenu.pack(side=RIGHT,padx='2m')
        HelpMenu.menu=Menu(HelpMenu)

        HelpMenu.menu.add_command(label='Index', command=self.HelpSearch)
        HelpMenu.menu.add_command(label='License', command=self.HelpLicense)
        HelpMenu.menu.add_command(label='About', command=self.HelpAbout)
        HelpMenu['menu']=HelpMenu.menu

        #self.canvas=Canvas(self.root, width=400, height=20, background='black')
        #self.canvas.pack()
        #self.balloon.bind(self.canvas, 'Buzz off! I am thinking of something.')

        #self.randomsquare()
        self.root.resizable(false,false)

        Presentation(self.root)

        #if len(sys.argv)>1:
        #    self.Open(sys.argv[1])
        
        self.root.mainloop()

    def randomsquare(self):
        i=5*randint(0,79)+1
        j=5*randint(0,3)+1
        if randint(0,1) is 0:
            color='black'
        else:
            color='red'
        self.canvas.create_rectangle(i,j,i+5,j+5,fill=color)
        self.root.after(50,self.randomsquare)
        pass

if __name__=='__main__':
    MainInterface()
