
# Question 1
## Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a Boolean True or False.


```python
def perms(a):        
    if(len(a)==1): 
        return [a]
# Checks if the Length of Substring and returns to result  
    result=[]
# Else Creates an Empty list Result
    for i,v in enumerate(a):
        result += [v+p for p in perms(a[:i]+a[i+1:])]
# generates possible permutations for passed input parameter
    return result
def anagram(s, t):
    result= perms(t)
# Permutations of t stored in result
    if any(x in s for x in result):
# Checks if any item of the List result in Mainstring
        return True
    else:
        return False
# Returns True if Substring is in Main string else retruns False
```


```python
anagram('udacity','z')
```




    False




```python
anagram('abcd', 'dcb')
```




    True




```python
anagram('@$#', '$#')
```




    True



# Question 2
## Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.



```python
def question2(a):
    # Converts the string to lower case
    a = a.lower()
    # Creates an empty list result
    result = []
    #Generate substrings and compare them
    for i in range(len(a)):
        for j in range(0, i):
            #Substring
            string = a[j:i + 1]
            #Compare substring to its reverse of itself
            if string == string[::-1]:
                result.append(string)
    if result == []:
        print 'No Palindrome found in given string'
# If List is empty handle exception by Print Statement
    else:
        return max(result, key=len)
```


```python
question2('jhkhjashf')
```




    'jhkhj'




```python
question2('gfdjskghads')
```

    No Palindrome found in given string
    


```python
question2('aamadambb')
```




    'madam'



# Question 3
## Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
## Vertices are represented as unique strings. The function definition should be question3(G)


```python
#Wrapping Graph as a class
class Graph:
    def __init__(self,g):
        #Veritces of the Graph
        self.Vertices= []
        #Dictionary to store graph
        self.graph = [] 
        for i in g:
            #add each vertex from the given adjacency list
            self.addVertex(i)
            for j in g[i]:
                #add each edge from the given adjacency list
                self.addEdge(i,j[0],j[1])
    
    #Adding a vertex to the Graph
    def addVertex(self,a):
        self.Vertices.append(a)

    #Adding an edge the Graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
    # To find set of an element i using Path compression
    def findelement(self, p, i):
        if p[i] == i:
            return i
        return self.findelement(p, p[i])
 
    #To create union of two sets
    def createUnion(self, p, r, x, y):
        a = self.findelement(p, x)
        b = self.findelement(p, y)
        if r[a] < r[b]:
            p[a] = b
        elif r[a] > r[b]:
            p[b] = a
        else :
            p[b] = a
            r[a] += 1
 
    # The main function to construct MST using Kruskal's algorithm
    def minimumSpanningTree(self):
        #To store the final minimum spanning tree
        finalTree =[] 
        #Sorting all the edges in the graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])       
        i = 0 
        j = 0 
        parent = [] ;
        indexa=[];
        rank = [];
        g={}

        #Creating subsets
        for node in range(len(self.Vertices)):
            indexa.append(self.Vertices[node])
            parent.append(node)
            rank.append(0)
            g[self.Vertices[node]]=[]

        NumberofVertices=len(self.Vertices)
        #Pick the smallest edges and add them to the final Spanning tree if they dont form a cycle
        while j < NumberofVertices -1 :
            k,l,w =  self.graph[i]
            i = i + 1
            m = self.findelement(parent, indexa.index(k))
            n = self.findelement(parent ,indexa.index(l))
            if m != n:
                j = j + 1  
                finalTree.append((k,l,w))
                self.createUnion(parent, rank, m, n)          

        # creating the adjacency list structure from the edges of the final minimum spanning tree
        for i in finalTree:
            g[i[0]].append((i[1],i[2]))
            g[i[1]].append((i[0],i[2]))    
        return g

def question3(g):
    x=Graph(g)
    return x.minimumSpanningTree()
```


```python
x = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
print question3(x)
```

    {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
    


```python
x = {   'A': [('B', 4), ('F', 2)],
        'B': [('A', 4), ('C', 6),('F', 5)], 
        'C': [('B', 6), ('D', 3),('F', 1)], 
        'D': [('C', 3), ('E', 2)], 
        'E': [('D', 2), ('F', 4)], 
        'F': [('A', 2), ('B', 5),('C', 1), ('E', 4)] }
print question3(x)
```

    {'A': [('F', 2), ('B', 4)], 'C': [('F', 1), ('D', 3)], 'B': [('A', 4)], 'E': [('D', 2)], 'D': [('E', 2), ('C', 3)], 'F': [('C', 1), ('A', 2)]}
    


```python
x={'A': [('B', 2),('C', 10)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5),('A',10)]}
print question3(x)
```

    {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
    

# Question 4
## Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where Tis the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

##    and the answer would be 3.


```python
# Returns immediate parent/ancestor to the node n
def ancestor(T, n):
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1

# Returns all the ancestors to the node n
def getAncestors(T,r,n):
    parents=[]
# Get all the parents until the root node is found
    while n!=r:
        n=ancestor(T,n)
        parents.append(n)
    return parents

def question4(T, r, n1, n2):
    n1_ancestors= getAncestors(T,r,n1)
    n2_ancestors= getAncestors(T,r,n2)   
    for i in range(len(n1_ancestors)):
        for j in range(len(n2_ancestors)):
            if(n1_ancestors[i]==n2_ancestors[j]):
                return n1_ancestors[i]
    return -1
    
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
```

    3
    

# Question 5
## Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


```python
#Creating a node
class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

#Adding a new node to the end of the linked list
def createLinkedList(root, node):
    if root.next is None:
        root.next = node
    else:
        createLinkedList(root.next, node)

#Finding the length of the linked list
def length(root):
    count=0
    if root==None:
        return 0
    if root.next==None:
        return 1
    while root.next is not None:
        count=count+1
        root=root.next
    return count+1

#Finding the nth variable from the end of the linked list
def variableLocation(root, n):
    count = 1
    if n>length(root): 
        return "Please enter a valid length"
    location=length(root)-n+1
    while count is not location:
        count=count+1
        root=root.next
    return str(n)+" number from the end is: "+str(root.value)

#root Node
r = Node(9)

# nodes
a = Node(5)
b = Node(6)
c = Node(4)
d = Node(7)
e = Node(2)
f = Node(8)
g = Node(1)

#Adding nodes to Linked list
createLinkedList(r,a)
createLinkedList(r,b)
createLinkedList(r,c)
createLinkedList(r,d)
createLinkedList(r,e)
createLinkedList(r,f)
createLinkedList(r,g)

#Finding the elements.
print variableLocation(r,1)
print variableLocation(r,3)
print variableLocation(r,5)
print variableLocation(r,6)
print variableLocation(r,8)
```

    1 number from the end is: 1
    3 number from the end is: 2
    5 number from the end is: 4
    6 number from the end is: 6
    8 number from the end is: 9
    
