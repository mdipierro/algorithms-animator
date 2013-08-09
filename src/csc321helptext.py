ListHelp=('List Data Structure',
"""
A list is collection of nodes stored in a sequential order.
A list can be implemented as an resizable array or as a linked list.
In the present implementation each node has the following attributes:

1) A progressive index (in square brackets, [x])
2) A value (represented in blue)
3) A tag (represented in black)
4) A color (the color of the circle at the north-west corner of the node)
5) Additional persistent data (not visible)
6) An image (gif file) used to represent the node

The tag, color, data and image of a node are optional attributes
used by the algorithms.
The progressive index is assigned automatically by the program.

A List is used to implement stack and queue objects.
""")

TreeHelp=('Tree Data Structure',
"""
A tree is collection of nodes where each node can have one parent node
(connected from above) and/or children nodes (commected below).
The parent of the children nodes is the node itself.

In the present implementation each node has the following attributes:

1) A progressive index (in square brackets, [x])
2) A value (represented in blue)
3) A tag (represented in black)
4) A color (the color of the circle at the north-west corner of the node)
5) Additional persistent data (not visible)
6) An image (gif file) used to represent the node

The tag, color, data and image of a node are optional attributes
used by the algorithms.
The progressive index is assigned automatically by the program.

In the case of Heaps there are two progressive indeces: the one
connected with the tree representation of the heap (on the left)
and the one connected with the list representation of the heap
(on the right). The latter is the one used by the heap algorithms.
""")

GraphHelp=('Graph Data Structure',
"""
A graph is collection of nodes (also called vertices) and
collections of links (also called edges).
A graph G = [V, E] where V is a list of nodes and E is a list of links.

In the present implementation each node has the following attributes:

1) A value (represented in blue)
2) A color (the color of the circle at the north-west corner of the node)
3) A progressive index (in square brackets, [x])
4) A tag (represented in black)
5) Additional persistent data (not visible)
6) An image (gif file) used to represent the node

The tag, color, data and image of a node are optional attributes
used by the algorithms.
The progressive index is assigned automatically by the program.

A link [x,y,w] represents a connection between node [x] to node [y].
w([x], [y]) is the distance associated with the link connecting
node [x] with node [y]. w is 1 by default.

A link in this program is always directed. An undirected link
is represented as a couple of links with opposite directionality.
""")

InsertionSortHelp =('InsertionSort Algorithm',
"""
The Insertion Sort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

Given a list of n elements the algorithm assumes that the first\n
i elements are already sorted (in green), selects node [i] as pivot
(in blue) and swaps it with the nodes on the left until all i+1 nodes
in the list are completely sorted.

The algorithms iteratively loops from i=2 until i=n.

The Insertion Sort is O(n^2).
""")

MergeSortHelp =('MergeSort Algorithm',
"""
The Merge Sort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

[SORRY, NO MORE HELP IS AVALABLE]

The Merge Sort is O(n log n).
""")

MergeSortDPHelp =('MergeSortDP (non-recursive) Algorithm',
"""
The Merge Sort (DP) algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value). DP here stands
for Dynamic Programming.

The MergeSortDP differs from the MergeSort because it has a
non-recursive structure.

[SORRY, NO MORE HELP IS AVALABLE]

The Merge Sort is O(n log n).
""")

HeapSortHelp =('HeapSort Algorithm',
"""
The HeapSort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

[SORRY, NO MORE HELP IS AVALABLE]

The HeapSort is O(n log n).
""")

QuickSortHelp =('QuickSort Algorithm',
"""
The QuickSort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

[SORRY, NO MORE HELP IS AVALABLE]

The QuickSort is O(n log n).
""")

RandomizedQuickSortHelp =('RandomizedQuickSort Algorithm',
"""
The RandomizedQuickSort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

[SORRY, NO MORE HELP IS AVALABLE]

The RandomizedQuickSort differs from the regular QuickSort bacause is
uses function RandomizedPartition in place of function Partition.
The RandomizedQuickSort is faster then the QuickSort on non-random data.

The RandomizedQuickSort is O(n log n).
""")

CountingSortHelp =('CountingSort Algorithm',
"""
The Counting Sort algorithm sorts elements (nodes) in a list
according with their values (i.e. attribute value).

[SORRY, NO MORE HELP IS AVALABLE]

The Counting Sort is O(n). The Counting sort achieves such a speed by using
extra information about the data to be sorted: it uses the fact that data is
bound from above and below.
""")

PartitionHelp =('Partition Algorithm',
"""
The Partition algorithm takes the value of the first node in the list (pivot)
and reorder the elements in the list into two partitions such that all nodes in
the first partition have values less than the pivot and all nodes in the
second partition have values higher of equal than the pivot.
The algorithms returns the location of the first node of the second partition.

[SORRY, NO MORE HELP IS AVALABLE]

The Partition algortihm is O(n).
""")

RandomizedPartitionHelp =('RandomizedPartition Algorithm',
"""
The RandomizedPartition algorithm takes the value of a random node in the list (pivot)
and reorder the elements in the list into two partitions such that all nodes in
the first partition have values less than the pivot and all nodes in the
second partition have values higher of equal than the pivot.
The algorithms returns the location of the first node of the second partition.

In practice the algorithm choose the pivot at random, exchange it with the first node
and calls the regular Partition algorithm.

[SORRY, NO MORE HELP IS AVALABLE]

The RandomizedPartition algortihm is O(n).
""")

HeapifyHelp =('Heapify Algorithm',
"""
The Heapify algorithms take as input a heap and a node and enforces the
heap property on the node and its descendants. The heap property says that
the value of a node cannot be less than the values of its descendant nodes.

The Heapify algorithm compares the value of a node with its two children.
If any of them has has a value larger than the value of the present node
the present node is exchanged with the largest of the children. The Heapify
algorithm then recursively calls itself starting from the child node that has
been changed.
""")

BuildHeapHelp =('BuildHeap Algorithm',
"""
The BuildHeap algorithm eforces the heap property on al nodes by calling Heapify
on all nodes in reversed order. The heap property says that
the value of a node cannot be less than the values of its descendant nodes.
""")

HeapExtractMaxHelp =('HeapExtractMax Algorithm',
"""
A Heap stucture can be used as priority queue. In fact the heap property
ensures that the element at the top of the heap has largest value.
It is therefore possible to extract (select and remove) this node in O(1) time.
""")

HeapInsertHelp =('HeapInsert Algorithm',
"""
A Heap stucture can be used as priority queue.
The HeapInsert algortihms allows to insert a new node in the heap by comparing
the value of the new node with the value of nodes present in the list, moving
down the tree. This is done by preserving the heap property.

The HeapInsert algorithm runs in O(log n).
""")

MinimumHelp =('Minimum Algorithm',
"""
The Minimum algorithm finds the Node in a list with minimum value.
This is achieved by assuming the first node in the list is the minimum and
iterating on the remaining nodes, comparing each of them with the minimum.
If a node is found to be less than the minimum that node is the new minimum.

This algortihm runs in O(n).
""")

MaximumHelp =('Maximum Algorithm',
"""
The Maximum algorithm finds the Node in a list with maximum value.
This is achieved by assuming the first node in the list is the maximum and
iterating on the remaining nodes, comparing each of them with the maximum.
If a node is found to be less than the maximum that node is the new maximum.

This algortihm runs in O(n).
""")
   
InorderTreeWalkHelp=('Inorder Tree Walk Algorithm',
"""
The InorderTreeWalk algorithm provides a unique map of a binary tree into a list.
""")
   

TreeSearchHelp=('Binary Tree Search Algorithm',
"""
The TreeSearch algorithm searches for a given value in a binary tree.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   

TreeMinimumHelp=('Binary Tree Minimum Algorithm',
"""
The TreeMinimum algorithm finds the node in a binary tree having minimum value.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   

TreeMaximumHelp=('Binary Tree Maximum Algorithm',
"""
The TreeMaximum algorithm finds the node in a binary tree having maximum value.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   

TreeInsertHelp=('Binary Tree Insert Algorithm',
"""
The TreeInsert algorithm inserts a new node ina binary tree.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   

TreeDeleteHelp=('Binary Tree Delete Algorithm',
"""
The TreeDelete algorithms removes a node for a binary tree.
It usually takes as input a pointer to the node t be deleted.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")

AVLRebalanceNodeHelp=('AVL-Tree Rebalance Node Algorithm',
"""
Sorry, ho help available
""")

AVLTreeInsertHelp=('AVL-Tree Insert Algorithm',
"""
The TreeInsert algorithm inserts a new node ina binary tree.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   
AVLTreeDeleteHelp=('AVL-Tree Delete Algorithm',
"""
The TreeDelete algorithms removes a node for a binary tree.
It usually takes as input a pointer to the node t be deleted.

Assuming the tree is properly balanced, it runs in O(log n).
It can run in O(n) on a degerate tree.
""")
   
BreadthFirstSearchHelp=('Breadth First Search Algorithm',
"""
The BreadthFirstSearch algorithm visits all nodes (vertices) in a graph
starting from an input node.

The algorithm procedes by "discovering" all nodes connected to the present node
(gray nodes) and visiting each of them in the order they where discovered
(the first node dicovered is explored first).
Once a node is visited more nodes are discovered and so on.

Once all discovevered nodes connected to a visited nodes have themselves
been visited, the node is marked as "explored" (green).

The BFS algorithm implies a sorting order among the nodes according with the
time they are discovered/explored.
""")
   

DepthFirstSearchHelp=('Depth First Search Algorithm',
"""
The DepthFirstSearch algorithm visits all nodes (vertices) in a graph
starting from an input node.

The algorithm procedes by "discovering" all nodes connected to the present node
(gray nodes) and visiting each of them in the order they where discovered.
(the last node dicovered is explored first).
Once a node is visited more nodes are discovered and so on.

Once all discovevered nodes connected to a visited nodes have themselves
been visited, the node is marked as "explored" (green).

The DFS algorithm implies a sorting order among the nodes according with the
time they are discovered/explored.
""")
   

MSTKruskalHelp=("Kruskal's Minimum Spanning Tree Algorithm",
"""
Sorry, Help not available.
""")

MSTPrimHelp=("Prim's Minimum Spanning Tree Algorithm",
"""
Sorry, Help not available.
""")


BellmanFordHelp=('Bellman-Ford Algorithm',
"""
Sorry, Help not available.
""")
   

DijkstraHelp=('Dijkstra Algorithm',
"""
Sorry, Help not available.

...and the present impementation of the algorithm does not work.
""")   

