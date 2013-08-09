from csc321show import *
from csc321algorithms import *
from csc321frames import *
from Pmw import *
from copy import *

class HuffmanEncoding:
    
    def SetHuffmanPath(self, tree,dict={},path=''):
        tree[1][0].value=path+'0'
        if len(tree[1])>1:
            self.SetHuffmanPath(tree[1],dict,path+'0')
        else:
            dict[tree[1][0].tag[0]]=tree[1][0].value
        tree[2][0].value=path+'1'
        if len(tree[2])>1:
            self.SetHuffmanPath(tree[2],dict,path+'1')
        else:
            dict[tree[2][0].tag[0]]=tree[2][0].value

    def HuffmanFrequence(self, node):
        try:
            return node[0].value
        except:
            return node.value

    def __init__(self, root, selftree=None):
        dialog=Pmw.PromptDialog(root, title='Huffman Encoding',
                                label_text='Text to compress:',
                                entryfield_labelpos='w',
                                entry_font=('Courier', 10),
                                buttons=('OK', 'Cancel'),
                                hull_width=40)
        if dialog.activate()!='OK': return
        text=dialog.get()

        dialog = Pmw.TextDialog(root, title = 'Huffman Encoding', text_font=('Courier', 12))
        dialog.maxsize(400,400)
        dialog.insert('end', 'Text to compress:\n'+text)
        dialog.insert('end', '\n\nUncompressed size: %i\n' % (8*len(text)))

        tree=[Node('Huffman')]
        dict={}
        for c in text:
            if not dict.has_key(c):
                dict[c]=1
            else:
                dict[c]=dict[c]+1
        for key in dict.keys():
            node=[Node(value=dict[key], tag=key)]
            node[0].data='frequence=%i' % dict[key]
            tree.append(node)

        frames=[]
        newframe(frames,tree)
        while len(tree)>3:
            MergeSort(tree,1)
            newframe(frames,tree)
            combined_frequence=self.HuffmanFrequence(tree[1])+self.HuffmanFrequence(tree[2])
            tree[1][0].color='green'
            tree[2][0].color='green'
            tree[1]=[Node(combined_frequence), tree[1], tree[2]]
            tree[1][0].data='frequence=%i' % combined_frequence
            del tree[2]
            newframe(frames,tree)
            
        tree[1][0].color='green'
        tree[2][0].color='green'
        newframe(frames,tree)

        dict={}
        self.SetHuffmanPath(tree,dict)
        newframe(frames,tree)
        ShowFrames(root,frames,showTree, title='Huffman Encoding Tree',save=selftree)
        dialog.insert('end', '\nCompression Rules:\n')
        for key in dict.keys():
            dialog.insert('end', "\t'"+key+"'-> "+dict[key]+"\n")

        dialog.insert('end', '\nCompressed Text:\n')
        size=0
        for c in text:
            dialog.insert('end', dict[c]+" ")        
            size=size+len(dict[c])

        dialog.insert('end', '\n\nCompressed Size: %i\n' % (size))
        dialog.configure(text_state = 'disabled')
        return

