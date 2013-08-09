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

def TicTacToeWin(list):
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
    
def TicTacToeSub(tree,depth,n=9,sym=('X', 'O')):
    if depth>0:
        for i in range(n):
            if i not in tree[0].path:                
                if divmod(depth,2)[1]==0:
                    node=[Node('%s,%i' %(sym[0],i))]
                else:
                    node=[Node('%s,%i' %(sym[1],i))]
                    pass
                node[0].path=[]
                for k in tree[0].path+[i]: node[0].path.append(k)
                a=TicTacToeWin(node[0].path)
                
                if a>0:
                    node[0].winner=a
                else:
                    TicTacToeSub(node, depth-1, n, sym)
                tree.append(node)
                
def TicTacToe(root):
    dialog=Pmw.PromptDialog(root,
                            title='TicTacToe',
                            label_text='Initial Moves=',
                            entryfield_labelpos='w',
                            buttons=('OK', 'Cancel'))
    if dialog.activate()!='OK': return
    path=eval(dialog.get())
    dialog=Pmw.PromptDialog(root,
                            title='TicTacToe',
                            label_text='Game depth=',
                            entryfield_labelpos='w',
                            buttons=('OK', 'Cancel'))
    if dialog.activate()!='OK': return
    depth=eval(dialog.get())
            
    tree=[Node('root', '')]
    tree[0].path=path
    if divmod(len(path),2)[1]==1: sym=('0', 'X')
    else: sym=('X','O')
    TicTacToeSub(tree, depth, 9,sym)
    dialog=Pmw.Dialog(root)
    showTree(dialog.interior(),tree,bx=30)
    return tree

##########################################################
#
# Huffman Encoding
#
##########################################################

def SetHuffmanPath(tree,dict={},path=''):
    tree[1][0].value=path+'0'
    if len(tree[1])>1:
        SetHuffmanPath(tree[1],dict,path+'0')
    else:
        dict[tree[1][0].name[0]]=tree[1][0].value
    tree[2][0].value=path+'1'
    if len(tree[2])>1:
        SetHuffmanPath(tree[2],dict,path+'1')
    else:
        dict[tree[2][0].name[0]]=tree[2][0].value

def HuffmanFrequence(node):
    try:
        return node[0].value
    except:
        return node.value
    
def HuffmanEncoding(root):
    print 'Input text to compress:'
    text=raw_input()
    print 'Uncompressed size=%i bits\n' % (8*len(text))
    
    tree=[Node('Huffman')]
    dict={}
    for c in text:
        if not dict.has_key(c):
            dict[c]=1
        else:
            dict[c]=dict[c]+1
    for key in dict.keys():
        node=[Node(value=dict[key], name=key)]
        tree.append(node)

    frames=[]
    newframe(frames,tree)
    while len(tree)>3:
        MergeSort(tree,1)
        newframe(frames,tree)
        combined_frequence=HuffmanFrequence(tree[1])+HuffmanFrequence(tree[2])
        tree[1][0].color='green'
        tree[2][0].color='green'
        tree[1]=[Node(combined_frequence), tree[1], tree[2]]        
        del tree[2]
        newframe(frames,tree)

    dict={}
    SetHuffmanPath(tree,dict)
    newframe(frames,tree)
    ShowFrames(root,frames,showTree)
    print 'Compression rules:'
    for key in dict.keys():
        print "\t'"+key+"' -> "+dict[key]
    print
    print 'Compressed text:'
    size=0
    for c in text:
        print dict[c], 
        size=size+len(dict[c])
    print
    print 'Compressed size=%i bits' % (size) 
    return tree
    

##########################################################
#
# ResourceAllocation
#
##########################################################

class Investment:
    def __init__(self,amount,expected_return,other=[]):
        self.amount=amount
        self.expected_return=expected_return
        self.other=other

def ResourceTableLookup(project, money):
    best_investment=Investment(0,0)
    for investment in project:
        if investment.amount<=money and \
           investment.expected_return>best_investment.expected_return:
            best_investment=investment
    return deepcopy(best_investment)

def ResourceAllocation(root):
    money=float(raw_input('Total Money Available (in milion dollars)='))
    n=int(raw_input('Number of projects available='))
    projects=[]
    for i in range(n):
        print '\nProject #', i
        project=[]
        while true:
            amount=raw_input("Investment opprtunity ('.' to terminate)=")
            if amount=='.': break
            amount=float(amount)
            expected_return=float(raw_input('Expected return='))
            project.append(Investment(amount,expected_return))
        projects.append(deepcopy(project))

    oldtable=[]
    for i in range(0,len(projects)):
        newtable=[]
        for investment in projects[i]:
            if investment.amount<=money:
                remaining_money=money-investment.amount
                expected_return=investment.expected_return
                other_investments=ResourceTableLookup(oldtable,remaining_money)
                remaining_money=remaining_money-other_investments.amount
                total_expected_return=expected_return+other_investments.expected_return
                newtable.append(Investment(investment.amount+
                                           other_investments.amount,
                                           total_expected_return,
                                           other_investments.other+
                                           [(i,investment.amount)]))

        print '\nEvaluating Project n.', i
        print 'Invest.\tReturn.\t[Details..]'
        for investment in newtable:
            print investment.amount, '\t', investment.expected_return, '\t', investment.other
        oldtable=newtable

    tree=[Node('root')]
    for i in newtable:
        print i.amount
        print i.expected_return
        print investment.other
        list=[]
        for item in i.other:
            list.append(Node(repr(item)))
        tree.append(deepcopy([Node(i.expected_return)]+list))
    showTree(root, tree)

##########################################################
#
# SequenceAlignment
#
##########################################################

def Array2D(a,b,value=0):
    x=[]
    for i in range(a):
        y=[]
        for j in range(b):
            y.append(value)
        x.append(deepcopy(y))
    return x

def SequenceAlignment(root):
    S1=raw_input('Insert a DNA sequence S1=')
    S2=raw_input('Insert a DNA sequence S2=')
    L1=len(S1)
    L2=len(S2)
    A=Array2D(L2,L1,value=0)
    LCS=''
    minj=0
    frames=[]
    list=deepcopy(A[0])
    ColorList(list, 'white')
    if frames!=0:
        for j in range(0,L1):
            list[j].name=S1[j]
        newframe(frames,list)
    for i in xrange(L2):
        if minj==0:
            value=0
        elif minj<L1:
            value=A[i][minj-1]
        else:
            break
        for j in xrange(minj,L1):
            if S1[j]==S2[i]:
                LCS=LCS+S1[j]
                value=value+1
                for k in range(i,L2):
                    for n in range(j,L1):
                        A[k][n]=value
                        
                if frames!=0:
                    for k in range(0,L1):
                        list[k].value=A[i][k]
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
        ShowFrames(root,frames,showList)

    print
    print '  |',
    for j in xrange(L1):
        print S1[j],
    print
    for i in xrange(L2):
        print S2[i],'|',
        for j in xrange(L1):
            print A[i][j],
        print

    print
    print 'Maximum Longest Subsequence='+LCS 
    print 'Maximum Longest Subsequence Length=',A[L2-1][L1-1] 
    return







