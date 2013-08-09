import os, sys

helptext="""
<html>

<head>
<meta http-equiv="Content-Language" content="en-us">
<meta name="GENERATOR" content="Microsoft FrontPage 5.0">
<meta name="ProgId" content="FrontPage.Editor.Document">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>ALGORITHMS ANIMATOR Documentation</title>
</head>

<body>

<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber1">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font color="#FFFFFF" size="6"><a name="Index"></a>ALGORITHMS ANIMATOR Program 
    Documentation</font></td>
  </tr>
</table>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="center"><b>
<font color="#0000FF" size="5"><a href="http://www.phoenixcollective.org/mdp">Massimo Di Pierro</a></font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="center">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="center">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="5">Table of 
Content</font></p>
<hr>
<ul>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#Overview">Overview</a></li>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#List">List</a><ul>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#ListReorderingAlgorithms">Reordering Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListReorderingAlgorithmsSwap">Swap</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListReorderingAlgorithmsRandomize">Randomize</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsDivideAndConquer">Stack Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListStackAlgorithmsPush">Push</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListStackAlgorithmsPop">Pop</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ListQueueAlgorithms">
    Queues Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#LstQueueAlgorithmsEnqueue">Enqueue</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListQueueAlgorithmsDequeue">Dequeue</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ListHeapAlgorithms">
    Heap Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListHeapAlgorithmsHeapify">Heapify</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#LstHeapAlgorithmsBuildHeap">BuildHeap</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListHeapAlgorithmsHeapExtractMax">HeapExtractMax</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListHeapAlgorithmsHeapInsert">HeapInsert</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsHeapSort">HeapSort</a> (cross listed)</li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListHeapAlgorithmsTreeHeap2List">tree(heap) to list</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ListSortAlgorithms">
    Sort Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsInsertionSort">InsertionSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsMergeSort">MergeSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsMergeSortDP">MergeSortDP</a> (non-recursive)</li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsQuickSort">QuickSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsRandomizedQuickSort">RandomizedQuickSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsHeapSort">HeapSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListSortAlgorithmsCountingSort">CountingSort</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ListOtherAlgorithms">
    Other Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListOtherAlgorithmsPartition">Partition</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListOtherAlgorithmsRandomizedPartition">RandomizedPartition</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListOtherAlgorithmsMinimum">Minimum</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#ListOtherAlgorithmsMaximum">Maximum</a></li>
    </ul>
    </li>
  </ul>
  </li>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#Tree">Tree</a><ul>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#TreeHeapAlgorithms">
    Heap Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeHeapAlgorithmsList2TreeHeap">list to tree(heap)</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#TreeBinaryTreeAlgorithms">Binary Search Tree Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsList2TreeBinary">list to tree(binary)</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsInorderTreeWalk">BST-InorderWalk</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsTreeSearch">BST-Search</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsTreeMinimum">BST-Minimum</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsTreeMaximum">BST-Maximum</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsTreeInsert">BST-Insert</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeBinaryTreeAlgorithmsTreeDelete">BST-Delete</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#TreeAVLTreeAlgorithms">
    AVL Tree Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeAVLTreeAlgorithmsList2TreeAVL">list to tree(AVL)</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeAVLTreeAlgorithmsRebalanceNode">AVL-RebalanceNode</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeAVLTreeAlgorithmsAVL-TreeInsert">AVL-Insert</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeAVLTreeAlgorithmsAVL-TreeDelete">AVL-Delete</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#TreeOtherAlgorithms">
    Other Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#TreeOtherAlgorithmsTreeDepth">TreeHeigth</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#TreeList2Tree">list to 
    tree</a></li>
  </ul>
  </li>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#Graph">Graph</a><ul>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#GraphAlgorithms">
    Algorithms</a><ul>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsSymmetrize">Symmetrize</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsBreadthFirstSearch">BreadthFirstSearch</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsBFS-TopologicalSort">BFS-TopologicalSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsDepthFirstSearch">DepthFirstSearch</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsDFS-TopologicalSort">DFS-TopologicalSort</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsMST-Kruskal">MST-Kruskal</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsMST-Prim">MST-Prim</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsBellman-Ford">Bellman-Ford</a></li>
      <li>
      <p style="margin-top: 0; margin-bottom: 0">
      <a href="#GraphAlgorithmsDijkstra">Dijkstra</a></li>
    </ul>
    </li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#GraphList2Graph">list 
    to graph</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#GraphTree2Graph">tree 
    to graph</a></li>
  </ul>
  </li>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#Examples">Examples</a><ul>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#ExamplesMakeRandomList">Make Random List</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ExamplesTimingSort">
    Timing (sort)</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0"><a href="#ExamplesTicTacToe">Tic 
    Tac Toe</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#ExamplesHuffmanEncoding">Huffman Encoding</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#ExamplesSequenceAlignment">Sequence Alignment</a></li>
  </ul>
  </li>
  <li>
  <p style="margin-top: 0; margin-bottom: 0"><a href="#Definitions">Definitions</a><ul>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsDivideAndConquer">Divide and Conquer</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsGreedyStrategy">Greedy Strategy</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsDinamicProgramming">Dynamic Programming</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsMemoization">Memoization</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsBacktracking">Backtracking</a></li>
    <li>
    <p style="margin-top: 0; margin-bottom: 0">
    <a href="#DefinitionsOrderOfGrowth">Order of Growth</a></li>
  </ul>
  </li>
</ul>
<hr>
<p style="margin-top: 0; margin-bottom: 0">For more on-line information about 
these and more algorithms visit <a href="http://www.nist.gov/dads/">NIST</a>.</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber2">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="Overview"></a>Overview</font></td>
  </tr>
</table>
<p>ALGORITHMS ANIMATOR is a Program written in <a href="http://www.python.org">Python</a> to 
display graphically some of the most common algorithms. </p>
<p>The program was written to the purpose to educate in the field of computer 
science under the belief that visualization of algorithm helps students to 
understand the underlying structure. A selection of algorithms from standard 
undergraduate textbooks on the subject has been implemented.</p>
<p>Students can built their own objects (Lists, Trees and Graphs) and run any of 
the implemented algorithms on their objects. Objects and can also be saved and 
loaded.</p>
<p>The program can also be used to generate PostScript representations of Lists, 
Trees and Graphs. </p>
<p>The name of the program ALGORITHMS ANIMATOR comes from the name of the algorithm class 
thought by the author of this program at DePaul University (Chicago, IL, USA).</p>
<p>Only two classes are required to understand the ALGORITHMS ANIMATOR code: class Node 
and class Link. The former is used to represent a Node in a List, in a Tree and 
in Graph. The latter is used to represent a link (edge) in a Graph. </p>
<p>Each Node has the following attributes:</p>
<ul>
  <li>index: a progressive index used to label (uniquely) each node in a List, 
  Tree or Graph. The index of a node is generated automatically by the program</li>
  <li>value: the attribute used to compare nodes, displayed in the center of the 
  node</li>
  <li>tag: displayed on the bottom right corner of the node</li>
  <li>color: used to demonstrate algorithms, displayed on the top left corner of 
  the node</li>
  <li>image: the filename of the GIF image, used to display the node</li>
  <li>parent: this attribute is used only in trees and is not displayed</li>
</ul>
<p>Each Link has the following attributes:</p>
<ul>
  <li>source: index of the source node</li>
  <li>destination: index of the destination node</li>
  <li>length: the length (weight) of the link</li>
  <li>color: the color used to display the link</li>
</ul>
<p>The Program has four main menus: <a href="#List">[List]</a>, <a href="#Tree">
[Tree]</a>, <a href="#Graph">[Graph]</a> and <a href="#Examples">[Examples]</a>. 
The Program, at each one time, keeps in memory one list (<b>self.list</b>), one 
tree (<b>self.tree</b>) and one graph (<b>self.graph</b>). Each of these tree 
objects can be created, modified, loaded and saved without affecting the other 
two. List algorithms act on self.list, tree algorithms act on self.tree and 
graph algorithms act on self.graph. The algorithms do not automatically store 
the the output back in self. For example if one creates a list and perform an
<a href="#ListSortAlgorithmsInsertionSort">InsertionSort </a>the sorted list is 
not stored into self.list. To store the sorted list into self.list click on the 
[Store] button when the frame showing the sorted list is visualized.</p>
<p>Every algorithms runs in its own animation-window. Each animation-windows 
displays the current animation frame and the following items:</p>
<ul>
  <li>A scrollbar to change the current animation frame</li>
  <li>A <b>[!]</b> button that displays the entire animation</li>
  <li>A <b>[+]</b> button that zoom in the frame</li>
  <li>A <b>[-]</b> button that zoom in the frame</li>
  <li>A <b>[PS]</b> button the produces a PostScript output for the frame</li>
  <li>A <b>[Store]</b> button that saves the object shown into the frame into 
  self.</li>
  <li>A <b>[?]</b> button that display a help page from the current document.</li>
</ul>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber3">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="List"></a>List</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A collection of items connected one to another.&nbsp; 
In the Program we do not differentiate a List from an Array.</p>
<p>In the ALGORITHMS ANIMATOR Program a list is represented as a Python list. For example to 
create a list choose [List][Create] and, at the prompt, type one of the 
following example lists:</p>
<blockquote>
  <p>[3,5,7,8,3,9]</p>
  <p>['a', 'b', 'c', 'd', 'e']</p>
</blockquote>
<p>Note that strings need to be in paranthesis.</p>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber7">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListReorderingAlgorithms"></a>List . Reordering Algorithms</font></td>
  </tr>
</table>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber8">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListReorderingAlgorithmsSwap"></a>List . Reordering Algorithms . 
    Swap</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Exchange the values of two nodes in a List, 
identified by the indices i and j.</p>
<p>The Program takes two integers i and j as input and swaps self.list[i] with 
self.list[j].</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber9">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListReorderingAlgorithmsRandomize"></a>List . Reordering Algorithms 
    . Randomize</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Shuffle the nodes in a List. We use the Python 
random generator (module random).</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber10">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListStackAlgorithms"></a>List . Stack Algorithms</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A collection of items in which only the most 
recently added item may be removed. The latest added item is at the top. Basic 
operations are push and pop. Also known as &quot;last-in, first-out&quot; or LIFO. </p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber11">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListStackAlgorithmsPush"></a>List . Stack Algorithms . Push</font></td>
  </tr>
</table>
<p>Insert a node as first element of the list A. Running time is in <i>O(1)</i></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber12">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListStackAlgorithmsPop"></a>List . Stack Algorithms . Pop</font></td>
  </tr>
</table>
<p>Remove and return the first element of the list A. Running time is in <i>O(1)</i></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber13">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListQueueAlgorithms"></a>List . Queue Algorithms </font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A set of items in which only the earliest added 
item may be accessed. Basic operations are add (to the tail) or enqueue and 
delete (from the head) or dequeue. Delete returns the item removed. Also known 
as &quot;first-in, first-out&quot; or FIFO. </p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber14">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="LstQueueAlgorithmsEnqueue"></a>List . Queue Algorithms . Enqueue</font></td>
  </tr>
</table>
<p>Insert a node as last element of the list A. Running time is in <i>O(1)</i></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber15">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListQueueAlgorithmsDequeue"></a>List . Queue Algorithms . Dequeue</font></td>
  </tr>
</table>
<p>Remove and return the first element of the list A. Running time is in <i>O(1)</i></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber16">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListHeapAlgorithms"></a>List . Heap Algorithms</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A complete binary tree where every node has a 
value more extreme (greater or less) than or equal to the key of its parent node 
(heap-property). A complete binary tree can be seen as a List where the 
parent-child relationship is implemented through the following algorithms:</p>
<table border="1" cellspacing="1" style="border-collapse: collapse" bordercolor="#111111" width="88%" id="AutoNumber87">
  <tr>
    <td width="100%"><font face="Courier" size="2">def Parent(i):<br>
&nbsp;&nbsp;&nbsp; return int((i-1)/2)<br>
    <br>
    def Left(i):<br>
&nbsp;&nbsp;&nbsp; return 2*i+1<br>
    <br>
    def Right(i):<br>
&nbsp;&nbsp;&nbsp; return 2*i+2</font></td>
  </tr>
</table>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber17">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListHeapAlgorithmsHeapify"></a>List . Heap Algorithms . Heapify</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Rearrange a heap to maintain the
<a href="#ListHeapAlgorithms">heap-property</a>, that is, the value of the root 
node is more extreme (greater or less) than or equal to the keys of its 
childrean nodes. If the root node's key is not more extreme, swap it with the 
most extreme child key, then recursively heapify that child's subtree. The child 
subtrees must be heaps to start. </p>
<p><em style="font-style: normal">For an array implementation, heapify takes
</em><em>O(</em>log<em> n)</em><em style="font-style: normal"> or </em><em>O(h)</em><em style="font-style: normal"> 
time under the comparison model, where </em><em>n</em><em style="font-style: normal"> 
is the number of nodes and </em><em>h</em><em style="font-style: normal"> is the
<a href="#TreeOtherAlgorithmsTreeDepth">height</a> of the tree.</em></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber18">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="LstHeapAlgorithmsBuildHeap"></a>List . Heap Algorithms . BuildHeap</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Convert a List/Array into a heap by executing
<em style="font-style: normal"><a href="#ListHeapAlgorithmsHeapify">heapify</a></em> 
progressively closer to the root. For an array of n nodes, this takes <i>O(n)</i> 
time under the comparison model.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber19">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListHeapAlgorithmsHeapExtractMax"></a>List . Heap Algorithms . 
    HeapExtractMax</font></td>
  </tr>
</table>
<p>The algorithm return the node with maximum value in a Heap (the root node) 
and restores the <a href="#ListHeapAlgorithms">heap-property</a>.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber20">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListHeapAlgorithmsHeapInsert"></a>List . Heap Algorithms . 
    HeapInsert</font></td>
  </tr>
</table>
<p>The algorithm appends a new node in a Heap and restores the
<a href="#ListHeapAlgorithms">heap-property</a>. Running time is in <i>O(</i>log
<i>n)</i></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber21">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListHeapAlgorithmsTreeHeap2List"></a>List . Heap Algorithms . 
    tree(heap) to list</font></td>
  </tr>
</table>
<p>Convert a heap from the tree representation (self.tree) to a list 
represenation (self.list).</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber22">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithms"></a>List . Sort Algorithms</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Arrange items in a predetermined order. There 
are dozens of algorithms, the choice of which depends on factors such as the 
number of items relative to working memory, knowledge of the orderliness of the 
items or the range of the<em> </em>values, the cost of comparing keys vs. the 
cost of moving items, etc. Most algorithms can be implemented as an
<em style="font-style: normal">in-place sort</em>, and many can be implemented 
so they are stable.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber23">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsInsertionSort"></a>List . Sort Algorithms . 
    InsertionSort</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Sort by repeatedly taking the next item and 
inserting it into the final data structure in its proper order with respect to 
items already inserted. Running time is in <em>O(n<sup>2</sup>)</em><em style="font-style: normal">. 
Average and worst case are in </em><em>Theta(n<sup>2</sup>)</em><em style="font-style: normal">. 
In the best case (presorted lists) is in </em><em>Theta(n)</em><em style="font-style: normal">.</em></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber24">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsMergeSort"></a>List . Sort Algorithms . MergeSort</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A <em style="font-style: normal">
<a href="#ListSortAlgorithms">sort</a></em> algorithm which splits the items to 
be sorted into two groups, recursively sorts each group, and
<em style="font-style: normal">merges</em> them into a final, sorted sequence. 
Run time for Merge is <i>Theta(n)</i>. Run time for MergeSort is <i>Theta(n</i> 
log<i> n)</i>.</p>
<p>MergeSort provides an example of <a href="#DefinitionsDivideAndConquer">
Divide and Conquer</a> strategy.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber25">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsMergeSortDP"></a>List . Sort Algorithms . 
    MergeSortDP (non-recursive)</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A <em style="font-style: normal">
<a href="#ListSortAlgorithms">sort</a></em> algorithm which splits the items to 
be sorted into two groups, <em style="font-style: normal">recursively</em> sorts 
each group, and <em style="font-style: normal">merges</em> them into a final, 
sorted sequence. Run time is <i>Theta(n</i> log<i> n)</i>.</p>
<p>MergeSortDP provides an example of <a href="#DefinitionsDinamicProgramming">
Dynamic Programming</a> strategy.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber26">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsQuickSort"></a>List . Sort Algorithms . QuickSort</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An in place <em style="font-style: normal">
<a href="#ListSortAlgorithms">sort</a></em> algorithm that uses the
<em style="font-style: normal"><a href="#DefinitionsDivideAndConquer">divide and 
conquer</a></em> paradigm. It picks an element from the array (the pivot),
<em style="font-style: normal"><a href="#ListOtherAlgorithmsPartition">
partitions</a></em> the remaining elements into those greater than and less than 
this pivot, and <em style="font-style: normal">recursively</em> sorts the 
partitions. There are many variants of the basic scheme above: to select the 
pivot, to partition the array, to stop the recursion on small partitions, etc.</p>
<p>QuickSort provides an example of <a href="#DefinitionsDivideAndConquer">
Divide and Conquer</a> strategy.</p>
<p><em style="font-style: normal">QuickSort has running time </em><em>Theta(n<sup>2</sup>)</em><em style="font-style: normal"> 
in the worst case, but it is typically (average case) </em><em>O(n </em>log<em> 
n)</em><em style="font-style: normal">. In practical situations, a finely tuned 
implementation of QuickSort beats most sort algorithms, including sort 
algorithms whose theoretical complexity is </em><em>O(n</em><em style="font-style: normal"> 
log</em><em> n)</em><em style="font-style: normal"> in the worst case. </em></p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber27">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsRandomizedQuickSort"></a>List . Sort Algorithms . 
    RandomizedQuickSort</font></td>
  </tr>
</table>
<p>Same as the <a href="#ListSortAlgorithmsQuickSort">QuickSort</a> but uses
<a href="#ListOtherAlgorithmsRandomizedPartition">RandomizedPartition</a> 
instead of <a href="#ListOtherAlgorithmsPartition">Partition</a>.</p>
<p>RandomizedQuickSort provides an example of
<a href="#DefinitionsDivideAndConquer">Divide and Conquer</a> strategy.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber30">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsHeapSort"></a>List . Sort Algorithms . HeapSort</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A <em style="font-style: normal">
<a href="#ListSortAlgorithms">sort</a></em> algorithm which builds a
<a href="#ListHeapAlgorithms"><em style="font-style: normal">heap</em>,</a> then 
repeatedly extracts the maximum item. Run time is <em>O(n</em><em style="font-style: normal"> 
log </em><em>n)</em>. In best case it is <i>O(n)</i>.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber28">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListSortAlgorithmsCountingSort"></a>List . Sort Algorithms . 
    CountingSort</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A 2-pass <em style="font-style: normal">
<a href="#ListSortAlgorithms">sort</a></em> algorithm that is efficient when the 
range of values is small and there many duplicate keys. The first pass counts 
the occurrences of each key in an auxiliary list/array, and then makes a running 
total so each auxiliary entry is the number of preceding keys. The second pass 
puts each item in its final place according to the auxiliary entry for that key. 
CountingSort runs in linear time, Theta(n).</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber29">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListOtherAlgorithms"></a>List . Other Algorithms</font></td>
  </tr>
</table>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber69">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListOtherAlgorithmsPartition"></a>List . Other Algorithms . 
    Partition</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Rearrange the elements of a list into two 
groups, typically, such that elements in the first group are less than a pivot 
value and elements in the second group are greater. Runs in linear time, <i>
Theta(n)</i>. </p>
<p>In the present implementation the pivot is choose to be the first element. 
Note that if the pivot is the minimum in the list, the function partition splits 
the list into two groups where the first only contains the pivot.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber31">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListOtherAlgorithmsRandomizedPartition"></a>List . Other Algorithms 
    . RandomizedPartition</font></td>
  </tr>
</table>
<p>Similar to partition but a random element in the list is used as pivot.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber32">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListOtherAlgorithmsMinimum"></a>List . Other Algorithms . Minimum</font></td>
  </tr>
</table>
<p>Find Minimum in a List or Array. Runs in linear time, <i>Theta(n)</i>.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber33">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ListOtherAlgorithmsMaximum"></a>List . Other Algorithms . Maximum</font></td>
  </tr>
</table>
<p>Find Maximum in a List or Array. Runs in linear time, <i>Theta(n)</i>.</p>
<p>[<a href="#List">Back to List</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber4">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="Tree"></a>Tree</font></td>
  </tr>
</table>
<p>(data structure) </p>
<p><strong>Definition:</strong> A data structure accessed beginning at the root 
node. Each node is either a leaf (has not children) or an internal node (has 
children). An internal node has one or more&nbsp; child nodes and is called the 
parent of its child nodes. All children of the same node are siblings. Contrary 
to a physical tree, the root is usually depicted at the top of the structure, 
and the leaves are depicted at the bottom. </p>
<p>A <span style="font-style: normal">connected</span>,
<span style="font-style: normal">undirected</span>,
<span style="font-style: normal">acyclic</span> <a href="#Graph">graph</a> is a 
Tree.</p>
<p>In the ALGORITHMS ANIMATOR Program a tree is represented as a Python list where the first 
element of the list is root node and the other elements are the children. A 
child can be a subtree. For example to create a tree choose [Tree][Create] and, 
at the prompt, type one of the following example trees:</p>
<blockquote>
  <p>['root','a','b','c']</p>
  <p>['root','a','b',['c',1,[2,7,8],3,4]]</p>
</blockquote>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber34">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeHeapAlgorithms"></a>Tree . Heap Algorithms</font></td>
  </tr>
</table>
<p>In the Program this menu contains the same algorithms as
<a href="#ListHeapAlgorithms">List . Heap Algorithms</a> but the heaps are 
displayed in tree representation as opposed to a list representation.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber37">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeHeapAlgorithmsList2TreeHeap"></a>Tree . Heap Algorithms . list 
    to tree(heap)</font></td>
  </tr>
</table>
<p>Convert a list (self.list) to a tree (self.tree).</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber35">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithms"></a>Tree . Binary Search Tree Algorithms</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A <a href="#Tree">tree</a> with at most two 
children for each node where every node's left sub-tree has values less than the 
node's value, and every right sub-tree has values greater. A new node is added 
as a leaf.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber36">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsList2TreeBinary"></a>Tree . Binary Tree 
    Algorithms . list to tree(binary)</font></td>
  </tr>
</table>
<p>Convert a list (self.list) into a binary tree (self.tree).</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber38">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsInorderTreeWalk"></a>Tree . Binary Tree 
    Algorithms . BST-InorderWalk</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Process all nodes of a tree by recursively 
processing the left sub-tree, then processing the root, and finally the right 
sub-tree.</p>
<p>BST-InorderWalk provides an example of <a href="#DefinitionsDivideAndConquer">
Divide and Conquer</a> strategy.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber39">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsTreeSearch"></a>Tree . Binary Tree 
    Algorithms . BST-Search</font></td>
  </tr>
</table>
<p>Search a binary (search) tree for an input value k.</p>
<p>BST-Search provides an example of <a href="#DefinitionsDivideAndConquer">
Divide and Conquer</a> strategy.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber40">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsTreeMinimum"></a>Tree . Binary Tree 
    Algorithms . BST-Minimum</font></td>
  </tr>
</table>
<p>Search a binary (search) tree for the node with minimum value.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber41">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsTreeMaximum"></a>Tree . Binary Tree 
    Algorithms . BST-Maximum</font></td>
  </tr>
</table>
<p>Search a binary (search) tree for the node with maximum value.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber42">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsTreeInsert"></a>Tree . Binary Tree 
    Algorithms . BST-Insert</font></td>
  </tr>
</table>
<p>Insert a new node in a binary search tree.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber43">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeBinaryTreeAlgorithmsTreeDelete"></a>Tree . Binary Tree 
    Algorithms . BST-Delete</font></td>
  </tr>
</table>
<p>Delete a node from a binary search tree.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber44">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeAVLTreeAlgorithms"></a>Tree . AVL Tree Algorithms</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A
<a href="http://www.nist.gov/dads/HTML/binarySearchTree.html">
<em style="font-style: normal">binary tree</em></a> where the<em> </em>height of 
the two subtrees (children) of each node differs by at most one (balance 
property). Look-up, insertion, and deletion are <em>O(</em><em style="font-style: normal">log</em><em> 
n)</em>, where <i>n</i> is the number of <em style="font-style: normal">nodes</em> 
in the tree.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber45">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeAVLTreeAlgorithmsList2TreeAVL"></a>Tree . AVL Tree Algorithms . 
    list to tree(AVL)</font></td>
  </tr>
</table>
<p>Convert a list (self.list) into an <a href="#TreeAVLTreeAlgorithms">AVL Tree</a> 
(self.tree)</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber46">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeAVLTreeAlgorithmsRebalanceNode"></a>Tree . AVL Tree Algorithms 
    . RebalanceNode</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Restore the <a href="#TreeAVLTreeAlgorithms">
balance property</a> of the node: the<em> </em>height of the two subtrees 
(children) of a node differs by at most one. Running time is in <i>O(1)</i>.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber47">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeAVLTreeAlgorithmsAVL-TreeInsert"></a>Tree . AVL Tree Algorithms 
    . AVL-Insert</font></td>
  </tr>
</table>
<p>Insert a new node into an <a href="#TreeAVLTreeAlgorithms">AVL Tree</a> and
<a href="#TreeAVLTreeAlgorithmsRebalanceNode">rebalance</a> the node and its 
ancestors. Running time is in O(log n) where n is the number of nodes in the 
tree.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber48">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeAVLTreeAlgorithmsAVL-TreeDelete"></a>Tree . AVL Tree Algorithms 
    .&nbsp; AVL-Delete</font></td>
  </tr>
</table>
<p>Delete a node from an <a href="#TreeAVLTreeAlgorithms">AVL Tree</a> and
<a href="#TreeAVLTreeAlgorithmsRebalanceNode">rebalance</a> its ancestors.&nbsp; 
Running time is in O(log n) where n is the number of nodes in the tree.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber49">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeOtherAlgorithms"></a>Tree . Other Algorithms</font></td>
  </tr>
</table>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber68">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="TreeOtherAlgorithmsTreeDepth"></a>Tree . Other Algorithms . 
    Tree Heigth</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> The maximum distance of any leaf from the root 
of a tree. If a tree has only one node (the root), the height is zero.</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber50">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4"><a name="TreeList2Tree">
    </a>Tree . list to tree</font></td>
  </tr>
</table>
<p>Convert a list (self.list) into a tree (self.tree)</p>
<p>[<a href="#Tree">Back to Tree</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber5">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="Graph"></a>Graph</font></td>
  </tr>
</table>
<p>In the ALGORITHMS ANIMATOR Program a graph G={V,E} is represented as a Python list 
containing two elements:</p>
<ul>
  <li>a list of vertices (nodes)</li>
  <li>a list of edges (links)</li>
</ul>
<p>. For example to create a graph choose [Graph][Create] and, at the prompt, 
type the following example graph:</p>
<blockquote>
  <p>[['a', 'b', 'c', 'd'], [[0,0,5], [0,1,3], [0,2,7], [3,1,9]]]</p>
</blockquote>
<p>where 'a', 'b', 'c' and 'd' are the values at the nodes and [0,0,5] is a link 
(of length 5) connecting node 0 (value='a') with itself, [0,1,3] is a link (of 
length 3) connecting node 0 (value='a') with node 1 (value='b'), etc. Undirected 
links can be represented as a couple of directed links in opposite direction and 
same length.</p>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber51">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4"><a name="GraphAlgorithms">
    </a>Graph . Algorithms</font></td>
  </tr>
</table>
<p>(data structure) </p>
<p><strong>Definition:</strong> A set of items connected by links (edges). Each 
item is called a node or vertex. Formally, a graph <i>G={V,E}</i> is a set of 
vetices (nodes) <i>V</i> and a set of edges (links) <i>E</i>.&nbsp; </p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber52">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsSymmetrize"></a>Graph . Algorithms . Symmetrize</font></td>
  </tr>
</table>
<p>Convert a directed graph (self.graph) into an undirected graph (self.graph).</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber56">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsBreadthFirstSearch"></a>Graph . Algorithms . 
    BreadthFirstSearch</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A search algorithm which considers neighbors of 
a node, that is, outgoing links of the node's predecessor in the search, before 
any outgoing link of the node. Extremes are searched last. This is typically 
implemented with a <a href="#ListQueueAlgorithms">queue</a>. Running time is in
<i>Theta(E+V)</i> where <i>V</i> is the number of vertices and <i>E</i> is the 
number of edges.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber53">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsBFS-TopologicalSort"></a>Graph . Algorithms . 
    BFS-TopologicalSort</font></td>
  </tr>
</table>
<p>IN PROGRESS</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber54">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsDepthFirstSearch"></a>Graph . Algorithms . 
    DepthFirstSearch</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Similar to
<a href="#GraphAlgorithmsBreadthFirstSearch">BreadthFirstSearch</a> but the
<a href="#ListQueueAlgorithms">queue</a> is replaced by a
<a href="#ListStackAlgorithms">stack</a>. Running time is in <i>Theta(E+V)</i> 
where <i>V</i> is the number of vertices and <i>E</i> is the number of edges.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber55">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsDFS-TopologicalSort"></a>Graph . Algorithms . 
    DFS-TopologicalSort</font></td>
  </tr>
</table>
<p>IN PROGRESS</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber57">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsMST-Kruskal"></a>Graph . Algorithms . MST-Kruskal</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An algorithm for computing a
<em style="font-style: normal">minimum spanning tree</em>. It maintains a set of 
partial minimum spanning trees, and repeatedly adds the shortest link in the 
graph whose nodes are in different partial minimum spanning trees. Running time 
is in <i>O(E</i> log <i>V)</i> where <i>V</i> is the number of vertices and <i>E</i> 
is the number of edges.</p>
<p>MST-Kruskal provides an example of <a href="#DefinitionsGreedyStrategy">
Greedy</a> strategy.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber58">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsMST-Prim"></a>Graph . Algorithms . MST-Prim</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An algorithm for computing a
<em style="font-style: normal">minimum spanning tree</em>. It builds upon a 
single partial minimum spanning tree, at each step adding a links connecting the 
node nearest to but not already in the current partial minimum spanning tree. 
Running time is in<i> O(E</i> + <i>V</i> log <i>V)</i> where <i>V</i> is the 
number of vertices and <i>E</i> is the number of edges.</p>
<p>MST-Prim provides an example of <a href="#DefinitionsGreedyStrategy">Greedy</a> 
strategy.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber59">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsBellman-Ford"></a>Graph . Algorithms . Bellman-Ford</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An efficient algorithm to find the shortest path 
from a single source node to all other nodes in a weighted, directed graph. The 
algorithm initializes the distance to the source node to 0 and all other 
vertices to Infinity. It then does <i>V-1</i> passes (<i>V</i> is the number of 
nodes) over all links relaxing, or updating, the distance to the destination of 
each link. Finally it checks each link again to detect negative weight cycles, 
in which case it returns false. Running time is in <em>O(V E)</em> where <i>V</i> 
is the number of vertices and <i>E</i> is the number of edges</p>
<p>Bellman-Ford provides an example of <a href="#DefinitionsGreedyStrategy">
Greedy</a> strategy.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber60">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="GraphAlgorithmsDijkstra"></a>Graph . Algorithms . Dijkstra</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An algorithm to find the shortest path from a 
single source node to all other vertices in a <em style="font-style: normal">
weighted, directed graph</em>. All weights must be nonnegative. Implementing the 
priority queue with a Fibonacci Heap makes the running time in <em>O(E + V </em>
log<em> V)</em>, where <i>V</i> is the number of vertices and <i>E</i> is the 
number of links.</p>
<p>Dijkstra provides an example of <a href="#DefinitionsGreedyStrategy">Greedy</a> 
strategy.</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber61">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4"><a name="GraphList2Graph">
    </a>Graph . list to graph</font></td>
  </tr>
</table>
<p>Convert a list (self.list) into a graph representation (self.graph).</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber62">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4"><a name="GraphTree2Graph">
    </a>Graph . tree to graph</font></td>
  </tr>
</table>
<p>Convert a tree (self.tree) into a graph representation (self.graph).</p>
<p>[<a href="#Graph">Back to Graph</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber6">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="Examples"></a>Examples</font></td>
  </tr>
</table>
<p>The menu <a href="#Examples">[Examples]</a> includes those algorithms that 
use lists, trees or graphs internally but do not belong to any of the other 
menus.</p>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber63">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ExamplesMakeRandomList"></a>Examples . Make Random List</font></td>
  </tr>
</table>
<p>The Program asks for an integer number, creates a random list and stores the 
list into self.list.</p>
<p>[<a href="#Examples">Back to Examples</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber64">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ExamplesTimingSort"></a>Examples . Timing (sort)</font></td>
  </tr>
</table>
<p>The Program runs all sorting algorithms and times them on the present 
architecture for different list sizes and produces a text report. The timing has 
three modes:</p>
<ul>
  <li>Time sorting algorithms on lists that are already ORDERED.</li>
  <li>Time sorting algorithms on RANDOM lists.</li>
  <li>Time sorting algorithms on lists that are in REVERSED order.</li>
</ul>
<p>[<a href="#Examples">Back to Examples</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber65">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ExamplesTicTacToe"></a>Examples . Tic Tac Toe</font></td>
  </tr>
</table>
<p>The Program produces the look-ahead tree for the Tic Tac Toe game. The user 
selects the initial moves and the height of the look-ahead tree. </p>
<p>[<a href="#Examples">Back to Examples</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber66">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ExamplesHuffmanEncoding"></a>Examples . Huffman Encoding</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A minimal variable-length character encoding 
based on the frequency of each character. First, each character becomes a 
trivial tree, with the character as the only node. The character's frequency is 
the tree's frequency. The two trees with the least frequencies are joined with a 
new root which is assigned the sum of their frequencies. This is repeated until 
all characters are in one tree. One code bit represents each level. Thus more 
frequent characters are near the root and are encoded with few bits, and rare 
characters are far from the root and are encoded with many bits.</p>
<p>The Program accepts the text to be compresses as input and produces a text 
report showing compression rules and compressed text. The Program also shows in 
an animation how the Huffman tree is built.</p>
<p>Huffman encoding provides an example of <a href="#DefinitionsGreedyStrategy">
Greedy</a> strategy.</p>
<p>[<a href="#Examples">Back to Examples</a> | <a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber67">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="ExamplesSequenceAlignment"></a>Examples . Sequence Alignment</font></td>
  </tr>
</table>
<p><strong>Definition:</strong> The problem of finding a maximum length (or 
maximum weight) subsequence of two or more lists/arrays/strings. Running time is 
in <i>Theta(n m)</i> where <i>n</i> and <i>m</i> is the length of the first and 
second list respectively.</p>
<p>The Program accepts two strings as input (stored into two separate lists) and 
computes the Longest Common Subsequence by aligning the two lists.</p>
<p>Determining the LCS (sequence alignment) provides an example of
<a href="#DefinitionsDinamicProgramming">Dynamic Programming</a> strategy.</p>
<p>[<a href="#Examples">Back to Examples</a> | <a href="#index">Back to Index</a>]</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber70">
  <tr>
    <td width="100%" bgcolor="#0000FF">
    <p style="margin-top: 0; margin-bottom: 0" align="center">
    <font size="6" color="#FFFFFF"><a name="Definitions"></a>Definitions</font></td>
  </tr>
</table>
<p>[<a href="#index">Back to Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber71">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsDivideAndConquer">Definitions . Divide and Conquer</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> The Divide-and-Conquer is a method of designing 
algorithms that (informally) proceeds as follows: Given an instance of the 
problem to be solved, split this into several, smaller, sub-instances (of the 
same problem) independently solve each of the sub-instances and then combine the 
sub-instance solutions so as to yield a solution for the original instance. This 
description raises the question: By what methods are the sub-instances to be 
independently solved? The answer to this question is central to the concept of 
the Divide-and-Conquer algorithm and is a key factor in gauging their 
efficiency. The solution depends on the problem.</p>
<p>The <a href="#ListSortAlgorithmsMergeSort">MergeSort</a> and
<a href="#ListSortAlgorithmsQuickSort">QuickSort</a> algorithms provide examples 
of Divide-and-Conquer..</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber72">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsGreedyStrategy">Definitions . Greedy Strategy</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Greedy algorithms work in phases. In each phase, 
a decision is made that appears to be good, without regard for future 
consequences. Generally, this means that some local optimum is chosen. This 
`take what you can get now' strategy is the source of the name for this class of 
algorithms. When the algorithm terminates, we hope that the local optimum is 
equal to the global optimum. If this is the case, then the algorithm is correct; 
otherwise, the algorithm has produced a suboptimal solution. If the best answer 
is not required, then simple greedy algorithms are sometimes used to generate 
approximate answers, rather than using the more complicated algorithms generally 
required to generate an exact answer. Frequently the Greedy Approach constitutes 
the basis of a heuristic approach. Even for problems which can be solved exactly 
by a greedy algorithm, establishing the correctness of the method may be a 
non-trivial process.</p>
<p>The <a href="#GraphAlgorithmsMST-Kruskal">Kruskal</a> and
<a href="#GraphAlgorithmsMST-Prim">Prim</a> algorithms provide examples of 
Greedy Strategy that leads to optimal solution.</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber73">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsDinamicProgramming">Definitions . Dinamic Programming</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> Dynamic Programming is a paradigm that is most 
often applied in the construction of algorithms to solve a certain class of 
optimization problems. That is problems which require the minimization or 
maximization of some measure. One disadvantage of using Divide-and-Conquer is 
that the process of recursively solving separate sub-instances can result in the 
same computations being performed repeatedly since identical sub-instances may 
arise. The idea behind dynamic Programming is to avoid this pathology by 
obviating the requirement to calculate the same quantity twice. The method 
usually accomplishes this by maintaining a table of sub-instance results. We say 
that Dynamic Programming is a Bottom-Up technique in which the smallest 
sub-instances are explicitly solved first and the results of these used to 
construct solutions to progressively larger sub-instances. In contrast, we say 
that the Divide-and-Conquer is a Top-Down technique.</p>
<p>The <a href="#ListSortAlgorithmsMergeSortDP">MergeSortDP</a> algorithm 
provides an example of Dynamic Programming.</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber74">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsMemoization">Definitions . Memoization</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An algorithmic technique which saves (memoizes) 
a computed answer for later reuse, rather than re-computing the answer each time 
it is needed. Usually the Memoization approach falls into the Dyncamic 
Programming even if it is a top-down approach. The reason being that both 
techniques use tables to store intermediate results.</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber75">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsBacktracking">Definitions . Backtracking</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> An algorithmic technique to find solutions by 
trying one of several choices. If the choice proves incorrect, computation <em>
backtracks</em> or restarts at the point of choice and tries another choice. It 
is often convenient to maintain choice points and alternate choices using 
recursion.</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>
<table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" id="AutoNumber76">
  <tr>
    <td width="100%" bgcolor="#0099CC"><font size="4">
    <a name="DefinitionsOrderOfGrowth">Definitions . Order of Growth</a></font></td>
  </tr>
</table>
<p><strong>Definition:</strong> A theoretical measure of the execution of an 
algorithm, usually the time or memory needed, given the problem size <i>n</i>, 
which is usually the number of items. Informally, saying some equation<i> f(n) = 
O(g(n))</i> means it is less than some constant multiple of <i>g(n)</i>. The 
notation is read, &quot;f of n is big oh of g of n&quot;. </p>
<p><strong>Formal Definition:</strong> <i>f(n) = O(g(n))</i> means there are 
positive constants <i>c</i> and <i>k</i>, such that <i>0 &lt;= f(n) &lt;= cg(n)</i> 
for all <i>n&lt;= k</i>. The values of <i>c</i> and <i>k</i> must be fixed for the 
function <i>f</i> and must not depend on <i>n</i>.</p>
<p><strong>Formal Definition:</strong> <i>f(n) = Omega(g(n))</i> means there are 
positive constants <i>c</i> and <i>k</i>, such that <i>0 &lt;= cg(n) &lt;= f(n)</i> 
for all <i>n &lt;= k</i>. The values of <i>c</i> and <i>k</i> must be fixed for the 
function <i>f</i> and must not depend on <i>n</i>.</p>
<p><strong>Formal Definition:</strong> <i>f(n) = Theta(g(n))</i> means there are 
positive constants <i>c<sub>1</sub></i>, <i>c<sub>2</sub></i>, and <i>k</i>, 
such that <i>0 &lt;= c<sub>1</sub>g(n) &lt;= f(n) &lt;= c<sub>2</sub>g(n)</i> for all <i>
n &lt;= k</i>. The values of <i>c<sub>1</sub></i>, <i>c<sub>2</sub></i>, and <i>k</i> 
must be fixed for the function <i>f</i> and must not depend on <i>n</i>.</p>
<p>[<a href="#Definitions">Back to Definitions</a> | <a href="#index">Back to 
Index</a>]</p>

</body>

</html>
"""

def getHelpFileName():
    filename=os.path.join(os.path.dirname(sys.executable), 'csc321index.html')
    file=open(filename, 'w')
    file.write(helptext)
    file.close()
    return 'file:///'+filename

    
