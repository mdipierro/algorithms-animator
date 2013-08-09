##########################################################
#
# Import Python libraries
#
##########################################################

from random import *
from math import *
from copy import *
from time import *
from types import *

##########################################################
#
# General definitions
#
##########################################################

Infinity = 'Infinity'
pi       = 3.14159265359
true     = 1
false    = 0

class Node:
    def __init__(self,
                 value='',
                 tag='',
                 color='white',
                 data='',
                 image=None,
                 parent=None):
        self.value=value
        self.tag=tag
        self.color=color
        self.data=data
        self.image=image
        self.parent=parent        
    
    def __cmp__(self, other):
        if self.value<other: return -1
        if self.value>other: return +1
        return 0
    def __repr__(self):
        return repr(self.value)
    pass

class Link:
    def __init__(self, source=0, destination=0, length=1, color=None):
        self.source=source
        self.destination=destination
        self.length=length
        self.color=color
    def __cmp__(self, other):
        if self.length<other: return -1
        if self.length>other: return +1
        return 0
    
##########################################################
#
# Coloring functions (determine the data structure)
#
##########################################################

def ColorList(list, color='white'):
    for i in range(len(list)):
        item=list[i]
        try:
            list[i]=Node(item.value, '', color, item.data, image=item.image)
        except:
            list[i]=Node(item, '', color)
            pass
        pass
    return

def ColorTree(tree, color='white', parent=None):
    if type(tree) is ListType:
        if len(tree)>0:
            tree[0]=ColorTree(tree[0],color,parent)
        for i in range(1,len(tree)):
            tree[i]=ColorTree(tree[i],color,tree)
            pass
        return tree
    else:
        try:
            return Node(tree.value, '', color, tree.data, parent=parent, image=tree.image)
        except:
            return Node(tree, '', color, parent)
            pass
        pass
    return

def treeHeight(A):
    if type(A) is ListType:
	if len(A) is 0: return 0
        max=0
        for item in A[1:]:
            i=treeHeight(item)
            if i>max: max=i
            pass
        return max+1
    elif A!=None:
        return 1
    else:
        return 0
    pass

def treeWidth(A , depth=-1):
    if depth==0:
        return 1
    elif depth>0:
        width=0
        for item in A[1:]:
            width=width+treeWidth(item,depth-1)
            pass
        return width
    else:
        if type(A)!=ListType:
            return 1
        if len(A)<2:
            return 1
        if A[1:]==[[],[]]:
            return 1
        max=0
        for sub in A[1:]:
            if sub==[]:
                max=max+1
            else:
                max=max+treeWidth(sub)
                pass
            pass
        return max
    pass

def delTreeNode(tree, i,counter=0):
    if type(tree)==ListType:
        if i==counter:
            tree=[]
            return
        else:
            counter=counter+1
            for j in range(1,len(tree)):
                tree_size=treeSize(tree[j])
                if i<(counter+tree_size):
                    if len(tree[j])==1 or i==counter:
                        del tree[j]
                        return
                    else:
                        delTreeNode(tree[j],i,counter)
                        return
                counter=counter+tree_size
            raise 'Tree Index Out Of Bounds'
    else:
        raise 'Tree Index Out Of Bounds'

def getTreeNode(tree, i,counter=0):
    if type(tree)==ListType:
        if i==counter:
            return tree[0]
        else:
            counter=counter+1
            for j in range(1,len(tree)):
                tree_size=treeSize(tree[j])
                if i<(counter+tree_size):
                    return getTreeNode(tree[j],i,counter)
                counter=counter+tree_size
            raise 'Tree Index Out Of Bounds'
    else:
        if i==counter:
            return tree
        else:
            raise 'Tree Index Out Of Bounds'

def setTreeNode(tree, i, node, subtree=0, counter=0):
    if type(tree)==ListType:
        if i==counter:
            tree[0]=node
            return
        else:
            counter=counter+1
            for j in range(1,len(tree)):
                tree_size=treeSize(tree[j])
                if i<(counter+tree_size):
                    if len(tree[j])==1:
                        tree[j]=[node]                        
                    elif i==counter:
                        tree[j][0]=node
                        if subtree!=0:
                            raise 'Not Implemented'
                    else:
                        setTreeNode(tree[j],i,node,subtree,counter)
                    return
                counter=counter+tree_size
            raise 'Tree Index Out Of Bounds'
    else:
        raise 'Tree Index Out Of Bounds'

def appendTreeNode(tree, i, node, counter=0):
    if type(tree)==ListType:
        if i==counter:
            tree.append([node])
            return
        else:
            counter=counter+1
            for j in range(1,len(tree)):
                tree_size=treeSize(tree[j])
                if i<(counter+tree_size):
                    appendTreeNode(tree[j],i,node,counter)
                    return
                counter=counter+tree_size
            raise 'Tree Index Out Of Bounds'
    else:
        raise 'Tree Index Out Of Bounds'

def ColorGraph(graph, color='white'):
    vertices=graph[0]
    links=graph[1]
    for i in range(len(vertices)):
        try:
            vertices[i]=Node(vertices[i].value, '', color,
                             vertices[i].data, image=vertices[i].image)
        except:
            vertices[i]=Node(vertices[i], '', color)
            pass
        pass
    for i in range(len(links)):
        link=links[i]
        try:
            if link.source<0 or link.source>=len(vertices):
                raise 'Incorrect link'
            elif link.destination<0 or link.destination>=len(vertices):
                raise 'Incorrect link'
            links[i].color=None
        except:            
            if link[0]<0 or link[0]>=len(vertices):
                raise 'Incorrect link'
            elif link[1]<0 or link[1]>=len(vertices):
                raise 'Incorrect link'
            try:
                links[i]=Link(source=link[0], destination=link[1], length=eval(repr(link[2])))
            except:
                links[i]=Link(source=link[0], destination=link[1])
    return

def islist(A):
    if type(A)==ListType:
        return true
    else:
        return false

##########################################################
#
# Factorial
#
##########################################################

def FactorialRecursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*FactorialRecursive(n-1)

def FactorialIterative(n):
    factorial=1
    while n>0:
        factorial=factorial*n
        n=n-1
    return factorial

def Factorial(n):
    return FactorialIterative(n)

##########################################################
#
# BinomialTree
#
##########################################################

def BinomialTree(n,k):
    return Factorial(n)/(Factorial(k)*Factorial(n-k))

##########################################################
#
# Probability
#
##########################################################

def Gaussian(mean, sigma):
    x=sqrt(-2.0*log(random()))
    y=2.0*Pi*random()
    return sigma*x*sin(y)+mean

##########################################################
#
# Conversion Functions
#
##########################################################

def Tree2List(tree):
    list=[]
    if type(tree) is ListType:
        list.append(tree[0])
        for item in tree[1:]:
            list=list+Tree2List(item)
    else:
        list.append(tree)
    return list

def List2Heap(list, i=0):
    try:
        tree=[list[i], List2Heap(list, 2*i+1), List2Heap(list,2*i+2)]
    except:
        try:
            tree=[list[i], List2Heap(list, 2*i+1)]
        except:
            tree=[list[i]]
        pass
    tree[0].tag='[%i]' %(i)
    return tree


def HeapSlice2List(tree, depth=0):
    if depth is 0:
        return [tree[0]]
    else:
        list=[]
        for item in tree[1:]:
            list=list+HeapSlice2List(item,depth-1)
            pass
        return list
    pass

def Heap2List(tree):
    list=[]
    depth=0
    while(1):
        sublist=HeapSlice2List(tree,depth)
        if len(sublist) is 0: return list
        list=list+sublist
        depth=depth+1
        pass
    return list
    
def List2Tree(list):    
    tree=[list[0]]
    if len(list)>1:
        tree.append(List2Tree(list[1:]))
    return tree

def List2Graph(list):
    vertices=[]
    links=[]
    graph=[vertices, links]
    lenlist=len(list)-1
    for i in range(0,lenlist):
        vertices.append(list[i])
        links.append(Link(i, i+1))
    vertices.append(list[lenlist])
    return graph


def Tree2Graph(tree,graph=0,parent=-1):
    if graph==0:
        graph=[[], []]
    vertices=graph[0]
    links=graph[1]
    if len(vertices)==0:
        if type(tree) is ListType:
            vertices.append(tree[0])
        else:
            vertices.append(tree)
        parent=0
    else:
        if tree!=[]:
            if type(tree) is ListType:
                vertices.append(tree[0])
            else:
                vertices.append(tree)
            links.append(Link(parent,len(vertices)-1))
            parent=len(vertices)-1
    if type(tree)==ListType:
        for item in tree[1:]:            
            Tree2Graph(item,graph,parent)            
    return graph

##########################################################
#
# Minimum
#
##########################################################

def Minimum(A):
    j=0
    for i in range(1,len(A)):
        if A[i]<A[j]:
            j=i
    return  A[j]

##########################################################
#
# Maximum
#
##########################################################

def Maximum(A):
    j=0
    for i in range(1,len(A)):
        if A[i]>A[j]:
            j=i
    return  A[j]

##########################################################
#
# Stack
#
##########################################################

def Push(A,node):
    A.insert(0,node)

def Pop(A):
    if len(A)==0:
        raise 'Empty Stack'
    node=A[0]
    del A[0]
    return node

##########################################################
#
# Queues
#
##########################################################

def Enqueue(A,node):
    A.append(node)

def Dequeue(A):
    if len(A)==0:
        raise 'Empty Queue'
    node=A[0]
    del A[0]
    return node
        
##########################################################
#
# InsertionSort
#
##########################################################

def InsertionSort(A):
    for i in range(1,len(A)):
        j=i-1
        while(j>=0):
            if A[j]>A[j+1]:
                (A[j], A[j+1]) = (A[j+1], A[j]) 
                j=j-1
            else:
                break
            pass

##########################################################
#
# MergeSort
#
##########################################################

def Merge(A,p,q,r):
    B=[]
    i=p
    j=q
    while true:
        if A[i]<=A[j]:
            B.append(A[i])
            i=i+1
        else:
            B.append(A[j])
            j=j+1
        if i==q:
            while j<r:
                B.append(A[j])
                j=j+1
            break
        if j==r:
            while i<q:
                B.append(A[i])
                i=i+1
            break
    A[p:r]=B

        
def MergeSort(A, p=0, r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q,r)
        Merge(A,p,q,r)

##########################################################
#
# MergeSortDP
#
##########################################################

def MergeSortDP(A):
    blocksize=1
    listsize=len(A)
    while blocksize<listsize:
        for p in range(0, listsize, 2*blocksize):
            q=p+blocksize
            r=min(q+blocksize, listsize)
            if r>q:
                Merge(A,p,q,r)
        blocksize=2*blocksize


##########################################################
#
# QuickSort
#
##########################################################

def Partition(A,i,j):
    x=A[i]
    h=i
    for k in range(i+1,j):
        if A[k]<x:
            h=h+1
            A[h],A[k]=A[k],A[h]
    A[h],A[i]=A[i],A[h]    
    return h
        
def QuickSort(A,p=0,r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=Partition(A,p,r)
        QuickSort(A,p,q)
        QuickSort(A,q+1,r)

##########################################################
#
# RandomizedQuickSort
#
##########################################################

def RandomizedPartition(A,p,r):
    i=randint(p,r-1)
    (A[p],A[i])=(A[i],A[p])
    return Partition(A,p,r)


def RandomizedQuickSort(A,p=0,r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=RandomizedPartition(A,p,r)
        RandomizedQuickSort(A,p,q)
        RandomizedQuickSort(A,q+1,r)

##########################################################
#
# HeapSort
#
##########################################################

def Parent(i):
    return int((i-1)/2)

def Left(i):
    return 2*i+1

def Right(i):
    return 2*i+2

def Heapify(A,i,heapsize=-1):
    if heapsize<0:
        heapsize=len(A)
    left=2*i+1
    right=2*i+2
    if left<heapsize and A[left]>A[i]:
        largest=left
    else:
        largest=i
    if right<heapsize and A[right]>A[largest]:
        largest=right
    if largest!=i:
        (A[i], A[largest])=(A[largest], A[i])
        Heapify(A,largest,heapsize)

def BuildHeap(A):
    heapsize=len(A)
    i=int(heapsize/2)
    while i>0:
        i=i-1
        Heapify(A,i)

def HeapSort(A):
    BuildHeap(A)
    heapsize=len(A)
    i=heapsize
    while i>1:
        i=i-1
        (A[0],A[i])=(A[i],A[0])
        heapsize=heapsize-1
        Heapify(A,0,heapsize)

def HeapExtractMax(A):
    if len(A)<1:
        raise 'Heap Underflow'
    max=A[0]
    A[0]=A[len(A)-1]
    del A[len(A)-1]
    Heapify(A,0)
    return max

def HeapInsert(A,node):
    A.append(node)
    i=len(A)-1
    while i>0 and A[Parent(i)]<A[i]:
        (A[i],A[Parent(i)])=(A[Parent(i)],A[i])
        i=Parent(i)

##########################################################
#
# CountingSort
#
##########################################################

def CountingSortSmall(A):
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    n=len(A)
    C=[]
    k=Maximum(A)+1
    for j in range(k):
        C.append(0)
    for j in range(n):
        C[A[j]]=C[A[j]]+1
    i=0        
    for j in range(k):
        while C[j]>0:
            A[i]=j
            C[j]=C[j]-1
            i=i+1

def CountingSort(A):
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    B=[]
    C=[]
    k=Maximum(A)+1
    for j in range(k):
        C.append(0)
    for j in range(len(A)):
        B.append(0)
        C[A[j]]=C[A[j]]+1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    j=len(A)-1
    while j>=0:
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
        j=j-1
    return B

##########################################################
#
# Timing
#
##########################################################

def Timing(f, mode='ORDERED', size=10, repeat=5):
    t=[]
    i=4
    while i*size<900:
        x=0
        for j in range(repeat):
            A=[]
            if mode=='REVERSED':
                A=range(i*size)
                A.reverse()
            elif mode=='RANDOM':
                for k in range(i*size):
                    A.append(randint(0, i*size))
            elif mode=='ORDERED':
                A=range(i*size)
            b=clock()
            B=deepcopy(A)
            f(B)
            B=deepcopy(A)
            f(A)
            B=deepcopy(A)
            f(A)
            B=deepcopy(A)
            f(A)
            x=x+(clock()-b)
        t.append((i*size, '%.2f' % (10.0*x)))
        i=2*i
    return t

##########################################################
#
# Tree Heap Functions
#
##########################################################

def countLeafs(tree):
    if tree is []: return 0
    if len(tree) is 1: return 1
    leafs=0
    for item in tree[1:]:
        leafs=leafs+countLeafs(tree)
    return leafs

def isHeap(tree):
    if len(tree)==0:
        return true
    try:
        list=Heap2List(tree)
        return true
    except:
        return false

##########################################################
#
# Binary Trees Functions
#
##########################################################

def treeSize(tree):
    if tree==[]:
        return 0
    if type(tree)!=ListType:
        return 1
    else:
        size=0
        for i in tree:
            size=size+treeSize(i)    
        return size

def ParentTree(tree):
    if type(tree) is ListType:
        return tree[0].parent
    else:
        return tree.parent    

def isNullTree(tree):
    if tree is None: return true
    if len(tree)==0: return true
    return false

rootnode=0
leftchild=1
rightchild=2

def BinaryTree(node,left=[],right=[]):
    list=[node,left,right]
    if not isNullTree(left):
        left[rootnode].parent=list
    if not isNullTree(right):
        right[rootnode].parent=list
    return list
    
def LeftChild(x):
    if type(x)==ListType:
        return x[leftchild]
    else:
        return None

def RightChild(x):
    if type(x)==ListType:
        return x[rightchild]
    else:
        return None

def isBinaryTree(tree):
    try:
        if isNullTree(tree): return true
        left=tree[leftchild]
        right=tree[rightchild]
        if not isBinaryTree(left): return false
        if not isBinaryTree(right): return false
        if not isNullTree(left):
            if left[rootnode]>=tree[rootnode]: return false
        if not isNullTree(right):
            if right[rootnode]<=tree[rootnode]: return false
        return true
    except:
        return false
    
##########################################################
#
# BST-InorderWalk
#
##########################################################

def BSTInorderWalk(tree,list=[]):
    if isNullTree(tree):
        return
    BSTInorderWalk(tree[leftchild],list)
    list.append(tree[rootnode])
    BSTInorderWalk(tree[rightchild],list)
    return list

##########################################################
#
# BST-Search
#
##########################################################

def BSTSearch(tree, k):
    if isNullTree(tree):
        return 
    if k < tree[rootnode]:
        return BSTSearch(tree[leftchild],k)
    elif k > tree[rootnode]:
        return BSTSearch(tree[rightchild],k)
    else:
        return tree[rootnode]

##########################################################
#
# BST-IterativeSearch
#
##########################################################

def BSTIterativeSearch(tree, k):
    while not isNullTree(tree):
        if k < tree[rootnode]:
            tree=tree[leftchild]            
        elif k > tree[rootnode]:
            tree=tree[rightchild]
        else:
            return tree[rootnode]

##########################################################
#
# BST-Minimum
#
##########################################################

def BSTMinimum(tree):
    while not isNullTree(tree[leftchild]):
        tree=tree[leftchild]
    return tree

##########################################################
#
# BST-Maximum
#
##########################################################

def BSTMaximum(tree):
    while not isNullTree(tree[rightchild]):
        tree=tree[rightchild]
    return tree

##########################################################
#
# BST-Insert
#
##########################################################

def BSTInsertLeaf(x, k):
    if isNullTree(x):
        k.parent=None
        x[:]=BinaryTree(k)
    else:
        k.parent=x
        if k<x[rootnode]:
            x[leftchild]=BinaryTree(k)
        else:
            x[rightchild]=BinaryTree(k)

def BSTInsert(tree, k):
    if isNullTree(tree):        
        BSTInsertLeaf(tree,k)
        return tree    
    x=tree
    while not isNullTree(x):
        y=x
        if k < x[rootnode]:
            x=x[leftchild]            
        elif k > x[rootnode]:
            x=x[rightchild]
        else:
            return tree
    x=y
    BSTInsertLeaf(x, k)
    return tree

def List2BinaryTree(list):
    tree=[]
    for node in list:
        tree=BSTInsert(tree,node)
    return tree
    
##########################################################
#
# BSTDelete
#
##########################################################

def BSTLeafDelete(x):
    y=x[rootnode].parent
    if y is None:
        x[:]=[]
    elif x is y[leftchild]:
        y[leftchild]=[]
    else:
        y[rightchild]=[]

def BSTNodeReplaceWithChildren(z,x):
    y=z[rootnode].parent
    z[:]=x[:]
    if not isNullTree(z):
        z[rootnode].parent=y

def BSTNodeReplaceWithoutChildren(z,x):
    q=z[rootnode].parent
    p=x[rightchild]
    if x is x[rootnode].parent[leftchild]:
        x[rootnode].parent[leftchild]=p
        if not isNullTree(p):
            p[rootnode].parent=x[rootnode].parent
    elif x is x[rootnode].parent[rightchild]:
        x[rootnode].parent[rightchild]=p
        if not isNullTree(p):
            p[rootnode].parent=x[rootnode].parent
    z[rootnode]=x[rootnode]
    z[rootnode].parent=q
    
def BSTDelete(z):
    if isNullTree(z[leftchild]) and isNullTree(z[rightchild]):
        BSTLeafDelete(z)
    elif isNullTree(z[leftchild]):
        x=z[rightchild]
        BSTNodeReplaceWithChildren(z,x) 
    elif isNullTree(z[rightchild]):
        x=z[leftchild]
        BSTNodeReplaceWithChildren(z,x) 
    else:
        x=BSTMinimum(z[rightchild])
        BSTNodeReplaceWithoutChildren(z,x) 

def AVLRebalanceNode(z):
    if isNullTree(z):
        return
    parent=z[rootnode].parent
    # single rotation anti-clock-wise
    T0=z[leftchild]
    y=z[rightchild]
    if not isNullTree(y):
        T1=y[leftchild]
        x=y[rightchild]
        if not isNullTree(x):
            T2=x[leftchild]
            T3=x[rightchild]
            if treeHeight(T2)>=treeHeight(T0):
                z[:]=BinaryTree(y[rootnode],
                                BinaryTree(z[rootnode],T0,T1),
                                BinaryTree(x[rootnode],T2,T3))
                z[rootnode].parent=parent
    # double rotation anti-clock-wise
    T0=z[leftchild]
    y=z[rightchild]
    if not isNullTree(y):
        T3=y[rightchild]
        x=y[leftchild]
        if not isNullTree(x):
            T1=x[leftchild]
            T2=x[rightchild]
            if treeHeight(T1)>=treeHeight(T0):
                z[:]=BinaryTree(x[rootnode],
                                BinaryTree(z[rootnode],T0,T1),
                                BinaryTree(y[rootnode],T2,T3))
                z[rootnode].parent=parent
    # single rotation clock-wise
    T3=z[rightchild]
    y=z[leftchild]
    if not isNullTree(y):
        T2=y[rightchild]
        x=y[leftchild]
        if not isNullTree(x):
            T0=x[leftchild]
            T1=x[rightchild]
            if treeHeight(T1)>=treeHeight(T3):
                z[:]=BinaryTree(y[rootnode],
                                BinaryTree(x[rootnode],T0,T1),
                                BinaryTree(z[rootnode],T2,T3))
                z[rootnode].parent=parent
    # double rotation clock-wise
    T3=z[rightchild]
    y=z[leftchild]
    if not isNullTree(y):
        T0=y[leftchild]
        x=y[rightchild]
        if not isNullTree(x):
            T1=x[leftchild]
            T2=x[rightchild]
            if treeHeight(T2)>=treeHeight(T3):
                z[:]=BinaryTree(x[rootnode],
                                BinaryTree(y[rootnode],T0,T1),
                                BinaryTree(z[rootnode],T2,T3))
                z[rootnode].parent=parent


def ApplyToSubTreeIndex(tree, i,func,counter=0):
    if type(tree)==ListType:
        if i==counter:
            func(tree)
            return
        else:
            counter=counter+1
            for j in range(1,len(tree)):
                tree_size=treeSize(tree[j])
                if i<(counter+tree_size):
                    if len(tree[j])==1 or i==counter:
                        func(tree[j])
                        return
                    else:
                        ApplyToSubTreeIndex(tree[j],i,func,counter)
                        return
                counter=counter+tree_size
            raise 'Tree Index Out Of Bounds'
    else:
        raise 'Tree Index Out Of Bounds'

def BSTDeleteIndex(tree, i):
    ApplyToSubTreeIndex(tree, i, BSTDelete)

def AVLRebalanceNodeIndex(tree,i):
    ApplyToSubTreeIndex(tree, i, AVLRebalanceNode)

def AVLRebalanceTree(tree):
    for j in range(treeSize(tree)):
        i=treeSize(tree)-1
        while i>=0:
            AVLRebalanceNodeIndex(tree,i)
            i=i-1

def List2AVLTree(list):
    tree=[]
    for node in list:
        tree=BSTInsert(tree,node)
        AVLRebalanceTree(tree)
    return tree


##########################################################
#
# Adjiacents
#
##########################################################

def Adjacents(u,graph):
    vertices=graph[0]
    links=graph[1]
    a=[]
    for link in links:
        if vertices[link.source] is u:
            a.append(link)
    return a

##########################################################
#
# SymmetrizeGraph
#
##########################################################
        
def SymmetrizeGraph(graph):
    vertices=graph[0]
    links=graph[1]
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i!=j:
                for link_ij in links:
                    distance_ij=Infinity
                    distance_ji=Infinity
                    if link_ij.source==i and link_ij.destination==j:
                        distance_ij=link_ij.length

                for link_ji in links:
                    if link_ji.source==j and link_ji.destination==i:
                        distance_ji=link_ji.length
                        if distance_ij==Infinity:
                            links.append(Link(i,j,distance_ji))
                        elif distance_ji>distance_ij:
                            link_ji.length=distance_ij
                        elif distance_ji<distance_ij:
                            link_ij.length=distance_ji
                        break

                if distance_ji==Infinity and distance_ij!=Infinity:
                    links.append(Link(j,i,distance_ij))

##########################################################
#
# BreadthFirstSearch
#
##########################################################

def BreadthFirstSearch(graph,start):
    vertices=graph[0]
    links=graph[1]
    blacknodes=[]
    graynodes=[start]
    t=0
    vertices[start].time_discovered=t
    while len(graynodes)>0:
        k=Dequeue(graynodes)
        for link in Adjacents(vertices[k],graph):
            j=link.destination
            if not j in blacknodes and not j in graynodes:
                Enqueue(graynodes,j)
                vertices[j].time_discovered=t
        blacknodes.append(k)
        vertices[k].time_found=t
        t=t+1
    return blacknodes
    
##########################################################
#
# DepthFirstSearch
#
##########################################################

def DepthFirstSearch(graph,start):
    vertices=graph[0]
    links=graph[1]
    blacknodes=[]
    graynodes=[start]
    t=0
    vertices[start].time_discovered=t
    while len(graynodes)>0:
        k=Pop(graynodes)
        for link in Adjacents(vertices[k],graph):
            j=link.destination
            if not j in blacknodes and not j in graynodes:
                Push(graynodes,j)
                vertices[j].time_discovered=t
        blacknodes.append(k)
        vertices[k].time_found=t
        t=t+1
    return blacknodes

##########################################################
#
# TopologicalSort
#
##########################################################

def TopologicalSort(graph,start,searchAlgorithm):
    blacknodes=searchAlgorithm(graph,start)
    vertices=graph[0]
    list=[]
    for i in blacknodes:
        list.append(vertices[i])
    for node in list:
        node.tag=repr(node.time_discovered)+'/'+repr(node.time_found)
    return list

##########################################################
#
# Minimum Spanning Tree Kruskal
#
##########################################################

def FindSet(S,i):
    for j in range(len(S)):
        if i in S[j]:
            return j
    return None

def UnionSets(S,i,j):
    for k in range(len(S)):
        if i in S[k]:
            A=S[k]
            break
    del S[k]
    for k in range(len(S)):
        if j in S[k]:
            S[k]=S[k]+A
            break
    return

def MSTKruskal(graph):
    vertices=graph[0]
    links=graph[1]
    A=[]
    S=[]
    for i in range(len(vertices)):
        S.append([i])
    links.sort()
    for link in links:
        i=link.source
        j=link.destination
        if FindSet(S,i)!=FindSet(S,j):
            A=A+[(i,j)]
            UnionSets(S,i,j)
    return A

##########################################################
#
# Minimum Spanning Tree Prim
#
##########################################################

def ExtractMin(Q):
    i=0
    for j in range(1,len(Q)):
        if Q[j].d<Q[i].d or Q[i].d==Infinity:
            i=j
    u=Q[i]
    del Q[i]
    return u

def MSTPrim(graph, r):
    vertices=graph[0]
    links=graph[1]
    Q=[]
    for i in range(len(vertices)):
        vertices[i].d=Infinity
        Q.append(vertices[i])
    Q[r].parent=None
    Q[r].d=0
    
    while len(Q)>0:
        u=ExtractMin(Q)
        for link in Adjacents(u,graph):
            v=vertices[link.destination] 
            w=link.length
            if v in Q and w<v.d:
                v.parent=u
                v.d=w

##########################################################
#
# Single Source Shrotest Path - Dijkstra
#
##########################################################

def Dijkstra(graph, r):
    vertices=graph[0]
    links=graph[1]
    Q=[]
    for i in range(len(vertices)):
        vertices[i].d=Infinity
        Q.append(vertices[i])
    Q[r].parent=None
    Q[r].d=0
    
    while len(Q)>0:
        u=ExtractMin(Q)
        for link in Adjacents(u,graph):
            v=vertices[link.destination] 
            w=link.length
            if v in Q and w+u.d<v.d:
                v.parent=u
                v.d=w+u.d

##########################################################
#
# Single Source Shrotest Path - BellmanFord
#
##########################################################

def InitializeSingleSource(graph,s):
    vertices=graph[0]
    for vertex in vertices:
        vertex.d=Infinity
        vertex.parent=None
    vertices[s].d=0

def Relax(u,v,graph):
    vertices=graph[0]
    links=graph[1]
    for link in Adjacents(u,graph):
        if v is vertices[link.destination]:
            w=link.length
            if not u.d is Infinity:
                if v.d>u.d+w:
                    v.d=u.d+w
                    v.parent=u
            return
        
def BellmanFord(graph, s):
    vertices=graph[0]
    links=graph[1]
    InitializeSingleSource(graph,s)
    for i in range(1,len(vertices)-1):
        for link in links:
            u=vertices[link.source]
            v=vertices[link.destination]
            Relax(u,v,graph)
                    
    for link in links:
        u=vertices[link.source]
        v=vertices[link.destination]
        w=link.length
        if u.d is Infinity:
            d=1e10
        else:
            d=u.d+w
        if v.d>d:
            return false
    return true

##########################################################
#
# Fibonacci and Memoization
#
##########################################################

def FibonacciRecursive(n):
    print 'calling FibonacciRecursive(%i)' % (n)
    if n is 0 or n is 1:
        return 1
    return FibonacciRecursive(n-1)+FibonacciRecursive(n-2)
    
def FibonacciDynamicProgramming(n):
    print 'calling FibonacciDynamicProgramming(%i)' % (n)
    if n is 0 or n is 1:
        return 1
    a=1
    b=1;
    for i in range(1,n):
        (a,b) = (b, a+b)
        print '    fibonacci(',i+1,')=', b
    return b

def FibonacciMemoize(n, table={0:1, 1:1}):
    print 'calling FibonacciMemoize(%i)' % (n)
    if table.has_key(n):
        print '    value is in table'
        return table[n]
    b=FibonacciMemoize(n-1,table)+FibonacciMemoize(n-2,table)
    table[n]=b
    print '    computing fibonacci(',n,')=', b, ' and storing in table'
    return b

##########################################################
#
# LCS
#
##########################################################

def LCS(X,Y):
    m=len(X)
    n=len(Y)
    c=[]
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append(0)
            if X[i]==Y[j]:
                if i==0 or j==0:
                    c[i][j]=1
                else:
                    c[i][j]=c[i-1][j-1]+1
            else:
                if i==0 or j==0:
                    c[i][j]=0
                else:
                    c[i][j]=max(c[i-1][j],c[i][j-1])
    return c[m-1][n-1]

##########################################################
#
# ContinuumKnapsack
#
##########################################################
    
def ContinuumKnapsack(a,b,c):
    n=len(a)
    if len(b)!=n: raise Exception
    table=[]
    f=0.0
    for i in range(n):
        y=float(a[i])/float(b[i])
        table.append((y,i))
        table.sort()
        table.reverse()
        for (y,i) in table:
            q=min(float(c)/float(b[i]),1)
            x.append((i,q))
            c=c-b[i]*q
            f=f+a[i]*q
    return (f,x)

##########################################################
#
# DiscereteKnapsack
#
##########################################################

