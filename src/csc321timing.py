from csc321algorithms import *
from time import *

def Timing(f, mode='ORDERED', size=40, repeat=40):
    t=[]
    for i in range(1,10):
        x=0
        for j in range(repeat):
            A=[]
            if mode=='REVERSE':
                A=range(i*size)
                A.reverse()
            elif mode=='RANDOM':
                for k in range(i*size):
                    A.append(randint(0, i*size))
            elif mode=='ORDERED':
                A=range(i*size)
            b=clock()
            f(A)
            x=x+(clock()-b)
        t.append('%.2f' % (1000.0/size*x))
    return t

