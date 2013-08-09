from csc321show import *
from csc321algorithms import *
from csc321frames import *
from Pmw import *
from copy import *

##########################################################
#
# TimingSort
#
##########################################################

class TimingSort:
    def __init__(self, root):
        self.root=root
        self.dialog=Toplevel(root)
        self.dialog.title('Timing Sort Algorithms')
        Label(self.dialog,text="""Running this timing algorithms may take several minutes.""",
              wraplength=200, justify=LEFT).pack(side=TOP, padx=5, pady=5)
        self.var=IntVar()
        frame=Frame(self.dialog, borderwidth=2, relief=RIDGE)
        for text, value in [('Random lists', 0),
                            ('Presorted lists', 1),
                            ('Reversed lists', 2)]:
            Radiobutton(frame, text=text, value=value, variable=self.var).pack(side=LEFT)
        self.var.set(0)
        frame.pack(side=TOP, padx=5, pady=5)
        frame=Frame(self.dialog)
        Button(frame, text='OK', comman=self.timingGo).pack(side=LEFT) 
        Button(frame, text='Cancel', comman=self.timingCancel).pack(side=LEFT) 
        frame.pack(side=TOP)
        self.dialog.resizable(false,false)        
        pass

    def timingCancel(self):
        self.dialog.destroy()

    def timingGo(self):
        mode=['RANDOM', 'ORDERED', 'REVERSED'][self.var.get()]
        Pmw.showbusycursor()
        s1=Timing(InsertionSort,mode)
        s2=Timing(MergeSort,mode)
        s3=Timing(MergeSort,mode)
        s4=Timing(HeapSort,mode)
        s5=Timing(QuickSort,mode)
        s6=Timing(RandomizedQuickSort,mode)
        s7=Timing(CountingSort,mode)
        Pmw.hidebusycursor()
        self.dialog.destroy()

        dialog = Pmw.TextDialog(self.root, title = 'Timing Sort Algorithms (results)', text_font=('Courier', 10))
        dialog.maxsize(600,250)
        dialog.insert('end', 'Sorting %s Lists\n\n' % (mode)) 
        dialog.insert('end', 'i\tInser.\tMerge\tMergeDP\tHeap\tQuick\tRQuick\tCounting\n') 
        for i in range(len(s1)):
            dialog.insert('end', '%d\t' % (s1[i][0]))
            dialog.insert('end', '%s\t' % (s1[i][1]))
            dialog.insert('end', '%s\t' % (s2[i][1]))
            dialog.insert('end', '%s\t' % (s3[i][1]))
            dialog.insert('end', '%s\t' % (s4[i][1]))
            dialog.insert('end', '%s\t' % (s5[i][1]))
            dialog.insert('end', '%s\t' % (s6[i][1]))
            dialog.insert('end', '%s\n' % (s7[i][1]))
        dialog.configure(text_state = 'disabled')
