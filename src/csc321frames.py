from math import *
from copy import *
from random import *
from csc321algorithms import *
from csc321show import *

def newframe(frames,frame):
    if frames!=None:
        frames.append(deepcopy(frame))
        
##########################################################
#
# MinimumFrames
#
##########################################################

def MinimumFrames(A,frames=None):
    j=0
    if frames!=None:
        A[0].color='yellow'
    for i in range(1,len(A)):
        if frames!=None:
            A[i].color='blue'
            newframe(frames,A)
            A[i].color='white'
        if A[i]<A[j]:
            if frames!=None:
                A[j].color='white'
            j=i
            if frames!=None:
                A[j].color='yellow'
                newframe(frames,A)
        else:
            if frames!=None:
                A[i].color='white'
                newframe(frames,A)            
    return  A[j]

##########################################################
#
# MaximumFrames
#
##########################################################

def MaximumFrames(A,frames=None):
    j=0
    if frames!=None:
        A[0].color='yellow'
    for i in range(1,len(A)):
        if frames!=None:
            A[i].color='blue'
            newframe(frames,A)
            A[i].color='white'
        if A[i]>A[j]:
            if frames!=None:
                A[j].color='white'
            j=i
            if frames!=None:
                A[j].color='yellow'
                newframe(frames,A)
        else:
            if frames!=None:
                A[i].color='white'
                newframe(frames,A)
    return  A[j]

##########################################################
#
# InsertionSortFrames
#
##########################################################

def InsertionSortFrames(A, frames):
    newframe(frames,A)
    A[0].color='green'    
    for i in range(1,len(A)):
        A[i].color='blue'
        j=i-1
        while(j>=0):
            if A[j]>A[j+1]:
                newframe(frames,A)
                (A[j], A[j+1]) = (A[j+1], A[j])
                j=j-1
            else:
                A[j].color='green'                
                break
            pass
        
        A[j+1].color='green'        
        newframe(frames,A)
        pass
    return

##########################################################
#
# MergeFrames
#
##########################################################

def MergeFrames(A,p,q,r,frames):
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
            pass
        if i==q:
            while j<r:
                B.append(A[j])
                j=j+1
                pass
            break
        if j==r:
            while i<q:
                B.append(A[i])
                i=i+1
                pass
            break
        pass
    A[p:r]=B
    return

##########################################################
#
# MergeSortFrames
#
##########################################################
        
def MergeSortFrames(A, frames, p=0, r=-1, level=0):
    if r is -1:
        r=len(A)
        newframe(frames,A)
        pass

    if frames!=None:
        for i in range(len(A)):
            if i in range(p,r):
                A[i].color='blue'
            else:
                A[i].color='gray'                                
        newframe(frames,A)

    if p<r-1:
        q=int((p+r)/2)

        MergeSortFrames(A,frames,p,q,level+1)
        MergeSortFrames(A,frames,q,r,level+1)
        MergeFrames(A,p,q,r,frames)

        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)

    return

##########################################################
#
# MergeSortDPFrames
#
##########################################################

def MergeSortDPFrames(A,frames=None):
    newframe(frames,A)
    blocksize=1
    listsize=len(A)
    while blocksize<listsize:
        for p in range(0, listsize, 2*blocksize):
            q=min(p+blocksize, listsize)
            r=min(q+blocksize, listsize)

            if frames!=None:
                for i in range(0,p): A[i].color='white'
                for i in range(p,q): A[i].color='yellow'
                for i in range(q,r): A[i].color='blue'
                for i in range(r,listsize): A[i].color='white'
                newframe(frames,A)

            if r>q:
                Merge(A,p,q,r)
                
            if frames!=None:
                for i in range(0,p): A[i].color='white'
                for i in range(p,r): A[i].color='green'
                for i in range(r,listsize): A[i].color='white'
                newframe(frames,A)

        blocksize=2*blocksize

##########################################################
#
# QuickSortFrames
#
##########################################################

def PartitionFrames(A,i,j,frames=None):
    if frames!=None:
        for k in range(i,j): A[k].color='white'
        A[i].color='yellow'
        A[i].tag='x'
        newframe(frames,A)        
        pass

    x=A[i]
    h=i
    for k in range(i+1,j):
        if frames!=None:
            for kk in range(i,j): A[kk].color='white'
            A[i].color='yellow'
            A[i].tag='x'
            A[h].color='green'
            A[k].color='blue'
            newframe(frames,A)        
            pass
        print 'x=',x, ' A[k]=',A[k]
        if A[k]<x:
            print A[k], A[k]
            h=h+1
            A[h],A[k]=A[k],A[h]
    A[h],A[i]=A[i],A[h]
    if frames!=None:
        for k in range(i,j): A[k].color='white'
        A[h].color='yellow'
        A[h].tag='x'
        newframe(frames,A)
        pass        
    return h
        
def QuickSortFrames(A,frames=None,p=0,r=-1,level=0):
    if r is -1:
        r=len(A)

    if frames!=None:
        for i in range(len(A)):
            if i in range(p,r):
                A[i].color='blue'
            else:
                A[i].color='gray'                                
        newframe(frames,A)

    if p<r-1:
        q=Partition(A,p,r)
        A[q].color='yellow'
        newframe(frames,A)
        QuickSortFrames(A,frames,p,q,level+1)
        QuickSortFrames(A,frames,q+1,r,level+1)
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass    
    else:
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass

##########################################################
#
# RandomizedQuickSortFrames
#
##########################################################

def RandomizedPartitionFrames(A,p,r,frames=None):
    i=randint(p,r-1)
    if frames!=None:
        A[i].color='yellow'
        A[i].tag='x'
        newframe(frames,A)
        pass
    (A[p],A[i])=(A[i],A[p])
    return PartitionFrames(A,p,r,frames)


def RandomizedQuickSortFrames(A,frames, p=0,r=-1,level=0):
    if r is -1:
        r=len(A)
        pass
    
    if frames!=None:
        for i in range(len(A)):
            if i in range(p,r):
                A[i].color='blue'
            else:
                A[i].color='gray'                                
        newframe(frames,A)

    if p<r-1:
        q=RandomizedPartition(A,p,r)
        pass
    
        A[q].color='yellow'
        newframe(frames,A)

        RandomizedQuickSortFrames(A,frames,p,q,level+1)
        RandomizedQuickSortFrames(A,frames,q+1,r,level+1)
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass    
    else:
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass
    pass


""" This is old (follows Cormen and not Johnsonbaough)
def PartitionFrames(A,i,j,frames=None):
    x=A[i]
    if frames!=None:
        for k in range(i,j): A[k].color='white'
        A[i].color='yellow'
        A[i].tag='X'
        newframe(frames,A)        
        pass
    
    while true:
        j=j-1
        while A[j]>x:
            if frames!=None:
                A[j].color='green'
                newframe(frames,A)
                pass
            j=j-1
            pass
        if i<j and frames!=None:
            A[j].color='grey'
            A[j].tag='J'
            newframe(frames,A)
            pass
        while A[i]<x:
            if frames!=None:
                A[i].color='green'
                newframe(frames,A)
                pass
            i=i+1
            pass
        if i<j:
            if frames!=None:
                A[i].color='blue'
                A[i].tag='I'
                newframe(frames,A)
                pass
            
            (A[i],A[j])=(A[j],A[i])
            
            if frames!=None:
                A[i].tag=''
                A[i].color='green'
                A[j].tag=''
                A[j].color='green'
                newframe(frames,A)
                pass
            pass
        else:
            if frames!=None:
                A[j+1].color='yellow'
                A[j+1].tag='R'
                newframe(frames,A)
                pass
            return j+1
        pass
    pass


def QuickSortFrames(A,frames, p=0,r=-1,level=0):
    if r is -1:
        r=len(A)
        pass
    
    if frames!=None:
        for i in range(len(A)):
            if i in range(p,r):
                A[i].color='blue'
            else:
                A[i].color='gray'                                
        newframe(frames,A)

    if p<r-1:
        q=Partition(A,p,r)
        pass
    
        A[q].color='yellow'
        newframe(frames,A)

        QuickSortFrames(A,frames,p,q,level+1)
        QuickSortFrames(A,frames,q,r,level+1)
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass    
    else:
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass
    pass

##########################################################
#
# RandomizedQuickSortFrames
#
##########################################################

def RandomizedPartitionFrames(A,p,r,frames=None):
    i=randint(p,r-1)
    if frames!=None:
        A[i].color='yellow'
        A[i].tag='X'
        newframe(frames,A)
        pass
    (A[p],A[i])=(A[i],A[p])
    return PartitionFrames(A,p,r,frames)


def RandomizedQuickSortFrames(A,frames, p=0,r=-1,level=0):
    if r is -1:
        r=len(A)
        pass
    
    if frames!=None:
        for i in range(len(A)):
            if i in range(p,r):
                A[i].color='blue'
            else:
                A[i].color='gray'                                
        newframe(frames,A)

    if p<r-1:
        q=RandomizedPartition(A,p,r)
        pass
    
        A[q].color='yellow'
        newframe(frames,A)

        RandomizedQuickSortFrames(A,frames,p,q,level+1)
        RandomizedQuickSortFrames(A,frames,q,r,level+1)
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass    
    else:
        if frames!=None:
            for i in range(p,r): A[i].color='green'
            newframe(frames,A)
            pass
        pass
    pass
"""

##########################################################
#
# HeapSortFrames
#
##########################################################

def HeapifyFrames(A,i,frames=None,heapsize=-1):
    if frames!=None:
        A[i].color='yellow'
        newframe(frames,A)
        pass
    
    if heapsize<0:
        heapsize=len(A)
        pass
    
    left=2*i+1
    right=2*i+2

    if frames!=None:
        if left<heapsize: A[left].color='blue'
        if right<heapsize: A[right].color='blue'
        newframe(frames,A)
        pass

    if left<heapsize and A[left]>A[i]:
        largest=left
    else:
        largest=i
        pass
    
    if right<heapsize and A[right]>A[largest]:
        largest=right
        pass
    
    if largest!=i:
        (A[i], A[largest])=(A[largest], A[i])

        if frames!=None:
            if left<heapsize: A[left].color='green'
            if right<heapsize: A[right].color='green'
            A[largest].color='blue'
            A[i].color='green'
            newframe(frames,A)
            pass
        HeapifyFrames(A,largest,frames,heapsize)
        
    elif frames!=None:
        if left<heapsize: A[left].color='green'
        if right<heapsize: A[right].color='green'
        A[i].color='green'
        newframe(frames,A)
        pass
    pass

def BuildHeapFrames(A,frames=None):
    heapsize=len(A)
    i=int(heapsize/2)
    while i>0:
        i=i-1
        HeapifyFrames(A,i,frames)
        pass
    pass

def HeapExtractMaxFrames(A,frames=None):
    if len(A)<1:
        raise 'Heap Underflow'
    max=A[0]
    A[0].color='yellow'
    newframe(frames,A)
    A[0]=A[len(A)-1]
    del A[len(A)-1]
    HeapifyFrames(A,0,frames)
    return max

def HeapInsertFrames(A,node,frames=None):
    A.append(node)
    i=len(A)-1
    while i>0 and A[Parent(i)]<A[i]:
        if frames!=None:
            A[i].color='yellow'
            A[Parent(i)].color='green'
            newframe(frames,A)
        (A[i], A[Parent(i)])=(A[Parent(i)], A[i])
        newframe(frames,A)
        i=Parent(i)
    if frames!=None:
        A[i].color='green'
        newframe(frames,A)


def HeapSortFrames(A,frames):
    if frames!=None:
        newframe(frames,A)
        pass
    
    BuildHeapFrames(A)

    if frames!=None:
        for node in A: node.color='gray'
        newframe(frames,A)
        pass
    
    heapsize=len(A)
    i=heapsize
    while i>1:
        i=i-1
        (A[0],A[i])=(A[i],A[0])
        heapsize=heapsize-1
        HeapifyFrames(A,0,frames,heapsize)

        if frames!=None:
            A[heapsize].color='gray'
            newframe(frames,A)
            pass
        pass
    if frames!=None:
        A[0].color='gray'
        newframe(frames,A)
        pass
    return

##########################################################
#
# CountingSort
#
##########################################################

def CountingSortSmallFrames(A,frames=None):
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    n=len(A)
    C=[]
    k=Maximum(A)+1
    if frames!=None:
        newframe(frames,A)
    for j in range(k):
        C.append(0)
    for j in range(n):
        C[A[j].value]=C[A[j].value]+1
    i=0        
    for j in range(k):
        while C[j]>0:
            A[i].value=j
            A[i].color='green'
            if frames!=None:
                newframe(frames,A)
            C[j]=C[j]-1
            i=i+1
            
def CountingSortFrames(A,frames=None):
    i=0
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    B=[]
    C=[]
    k=Maximum(A).value+1
    for j in range(len(A)):
        A[j].tag='A[%i]' % (j)
    if frames!=None:
        newframe(frames,[Node('root'), List2Tree(A), Node('...', 'B'), Node('...', 'C')])
    for j in range(k):
        C.append(Node(0, 'C[%i]' %(j)))
    for j in range(len(A)):
        B.append(Node(0, 'B[%i]' %(j)))
        C[A[j].value].value=C[A[j].value].value+1
        if frames!=None:
            A[j].color='yellow'
            C[A[j].value].color='yellow'
            newframe(frames,[Node('root'), List2Tree(A), List2Tree(B), List2Tree(C)])
            A[j].color='white'
            C[A[j].value].color='white'
    for i in range(1,k):
        C[i].value=C[i].value+C[i-1].value
        if frames!=None:
            C[i].color='yellow'
            newframe(frames,[Node('root'), List2Tree(A), List2Tree(B), List2Tree(C)])
            C[i].color='white'

    j=len(A)-1
    while j>=0:
        B[C[A[j].value].value-1]=A[j]
        C[A[j].value].value=C[A[j].value].value-1
        if frames!=None:
            A[j].color='yellow'
            B[C[A[j].value].value-1].color='green'
            C[A[j].value].color='yellow'
            newframe(frames,[Node('root'), List2Tree(A), List2Tree(B), List2Tree(C)])
            A[j].color='white'
            C[A[j].value].color='white'
        j=j-1
    return B

##########################################################
#
# InorderTreeWalkFrames
#
##########################################################

def BSTInorderWalkFrames(tree,list,frames,fulltree=None):
    if fulltree==None:
        newframe(frames,tree)
        fulltree=tree
    if isNullTree(tree):
        return
    BSTInorderWalkFrames(tree[leftchild],list,frames,fulltree)
    list.append(tree[rootnode])
    tree[rootnode].color='green'
    newframe(frames,fulltree)
    BSTInorderWalkFrames(tree[rightchild],list,frames,fulltree)
    return list

##########################################################
#
# TreeSearchFrames
#
##########################################################

def BSTSearchFrames(tree,k,frames,fulltree=None):
    if fulltree==None:
        fulltree=tree
        newframe(frames,tree)
    if isNullTree(tree):
        return
    if k < tree[rootnode]:
        tree[rootnode].color='gray'
        newframe(frames,fulltree)
        return BSTSearchFrames(tree[leftchild],k,frames,fulltree)
    elif k > tree[rootnode]:
        tree[rootnode].color='gray'
        newframe(frames,fulltree)
        return BSTSearchFrames(tree[rightchild],k,frames,fulltree)
    else:
        tree[rootnode].color='green'
        newframe(frames,fulltree)
        return tree[rootnode]

##########################################################
#
# BST-InsertFrames
#
##########################################################

def BSTInsertFrames(tree, k, frames):
    if isNullTree(tree):
        k.parent=None
        tree=BinaryTree(k)
        newframe(frames,tree)
        return tree
    newframe(frames,tree)
    x=tree
    while not isNullTree(x):
        x[rootnode].color='grey'
        newframe(frames,tree)
        y=x
        if k < x[rootnode]:
            x=x[leftchild]            
        elif k > x[rootnode]:
            x=x[rightchild]
        else:
            return tree
    x=y
    k.parent=x
    if k<x[rootnode]:
        x[leftchild]=BinaryTree(k)
    else:
        x[rightchild]=BinaryTree(k)
    newframe(frames,tree)
    return tree

def List2BinaryTree(list):
    tree=[]
    for node in list:
        tree=BSTInsert(tree,node)
    return tree

##########################################################
#
# BreadthFirstSearchFrames
#
##########################################################

def BreadthFirstSearchFrames(graph,start,frames):
    vertices=graph[0]
    links=graph[1]
    blacknodes=[]
    graynodes=[start]
    vertices[start].color='gray'
    newframe(frames,graph)
    while len(graynodes)>0:
        k=Dequeue(graynodes)
        for link in Adjacents(vertices[k],graph):
            j=link.destination
            vertices[k].color='yellow'                
            link.color='yellow'
            if not j in blacknodes and not j in graynodes:
                Enqueue(graynodes,j)
                vertices[j].color='gray'                
                pass
            newframe(frames,graph)
            link.color=None
            pass
        blacknodes.append(k)
        vertices[k].color='black'
        newframe(frames,graph)
        pass
    return

##########################################################
#
# DepthFirstSearchFrames
#
##########################################################

def DepthFirstSearchFrames(graph,start,frames):
    vertices=graph[0]
    links=graph[1]
    blacknodes=[]
    graynodes=[start]
    vertices[start].color='gray'
    newframe(frames,graph)
    while len(graynodes)>0:
        k=Pop(graynodes)
        for link in Adjacents(vertices[k],graph):
            j=link.destination
            vertices[k].color='yellow'                
            link.color='yellow'
            if not j in blacknodes and not j in graynodes:
                Push(graynodes,j)
                vertices[j].color='gray'                
                pass
            newframe(frames,graph)
            link.color=None
            pass            
        blacknodes.append(k)
        vertices[k].color='black'
        newframe(frames,graph)
        pass
    return

##########################################################
#
# Minimum Spanning Treee KruskalFrames
#
##########################################################

def MSTKruskalFrames(graph, frames=[]):
    newframe(frames,graph)
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
            link.color='yellow'
            newframe(frames,graph)
            A=A+[(i,j)]
            UnionSets(S,i,j)
    return A

##########################################################
#
# Minimum Spanning Treee PrimFrames
#
##########################################################

def MSTPrimFrames(graph, r, frames=[]):
    vertices=graph[0]
    links=graph[1]

    Q=[]
    for i in range(len(vertices)):
        vertices[i].index=i
        vertices[i].d=Infinity
        vertices[i].tag='Inf.'
        Q.append(vertices[i])
    Q[r].parent=None
    Q[r].d=0
    Q[r].tag=0
    newframe(frames,graph)
    
    while len(Q)>0:
        u=ExtractMin(Q)
        for link in Adjacents(u,graph):
            v=vertices[link.destination] 
            w=link.length
            if v in Q and w<v.d:
                v.parent=u
                for item in links:
                    if item.destination is link.destination:
                        item.color=None
                link.color='yellow'
                v.parent=u
                v.d=w
                v.tag=w
                newframe(frames,graph)

##########################################################
#
# Single Source Shortest Path - DijkstraFrames
#
##########################################################

def DijkstraFrames(graph, r, frames=[]):
    vertices=graph[0]
    links=graph[1]

    Q=[]
    for i in range(len(vertices)):
        vertices[i].index=i
        vertices[i].d=Infinity
        vertices[i].tag='Inf.'
        Q.append(vertices[i])
    Q[r].parent=None
    Q[r].d=0
    Q[r].tag=0
    newframe(frames,graph)
    
    while len(Q)>0:
        u=ExtractMin(Q)
        for link in Adjacents(u,graph):
            v=vertices[link.destination] 
            w=link.length
            if v in Q and w+u.d<v.d:
                v.parent=u
                for item in links:
                    if item.destination is link.destination:
                        item.color=None
                link.color='yellow'
                v.parent=u
                v.d=w+u.d
                v.tag=w
                newframe(frames,graph)

##########################################################
#
# Single Source Shortest Path - BellmanFordFrames
#
##########################################################
            
def BellmanFordFrames(graph, s, frames=None):
    vertices=graph[0]
    links=graph[1]
    InitializeSingleSource(graph,s)
    newframe(frames,graph)
    for i in range(1,len(vertices)-1):
        for link in links:
            u=vertices[link.source]
            v=vertices[link.destination]
            Relax(u,v,graph)
            if frames!=None and v.parent is u:
                for item in links:
                    if vertices[item.destination].parent!=vertices[item.source]:
                        item.color=None
                if u.tag!=u.d or v.tag!=v.d or link.color!='yellow':
                    link.color='yellow'
                    u.tag=u.d
                    v.tag=v.d
                    newframe(frames,graph)
                    
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
# RunFiniteStateMachineFrames
#
##########################################################

def RunFiniteStateMachineFrames(graph, s, frames=None):
    vertices=graph[0]
    links=graph[1]
    for u in vertices: u.color='white'
    i=0
    vertices[i].color='blue'
    newframe(frames,graph)
    vertices[i].color='white'
    output=''
    history=''
    for c in s:
        check=1
        for link in links:
            if link.source==i and link.length.has_key(c):
                j=i
                i=link.destination
                vertices[i].color='blue'
                link.color='yellow'
                newframe(frames,graph)
                link.color=None
                vertices[i].color='white'
                k=link.length[c]
                output=output+k
                history=history+'(%i, %c) -> (%i, %s)\n' % (j,c,i,k)
                check=0
                break
        if check:
            history=history+'rejecting input char "%c"\n' % (c)
    return (history, output)

                        
