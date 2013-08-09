from csc321show import *
from csc321algorithms import *
from csc321frames import *
from Pmw import *
from copy import *


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

class ResourceAllocation:
    
    def ResourceTableLookup(self, project, money):
        best_investment=Investment(0,0)
        for investment in project:
            if investment.amount<=money and \
               investment.expected_return>best_investment.expected_return:
                best_investment=investment
        return deepcopy(best_investment)

    def __init__(self,root):
        
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
                    other_investments=self.ResourceTableLookup(oldtable,remaining_money)
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
        ShowSingle(root, tree, showTree, title='Investment Strategy')

