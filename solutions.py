
# Technical Interview - Python

# Question1:
# Checks if the Length of Substring and returns to result
# Returns True if anagram of t is in Main string else retruns False
def question1(s, t):
    if not t:
        return "Please enter a valid string t"
    if not s:
        return "Please enter a valid string s"
    if len(t)>len(s):
        return "Length of t should be greater than equal to s"
    #compare substring of s with t and checking if anagram of t is in s
    for i in range(len(s) - len(t) + 1):
        if(sorted(s[i: i+len(t)])==sorted(t)):
            return True
    return False
# Testcase1:
print question1(None, "dat")
# Output: Please enter a valid string s

# Testcase2:
print question1("apple", None)
# Output: Please enter a valid string t

# Testcase3:
print question1("Udacity", "dca")
# Output: True

# Testcase4:
print question1("abcd", "dca")
# Output: False

# Testcase5:
print question1("abcd", "dcabe")
# Output: Length of t should be greater than equal to s

# ------------------------------------------------------------------------------

# Question2:

def question2(a):
    if not a:
        return "Please enter a valid string"
    # Converts the string to lower case
    a = a.lower()
    # Creates an empty list result
    result = ""
    #Generate substrings and compare them
    for i in range(len(a)):
        for j in range(0, i):
            #Substring
            string = a[j:i + 1]
            # We will check if its a palindrome only if the length of this string
            #is greater than the palindrome found already in this string
            if(len(string)>len(result)):
            #Compare substring to its reverse of itself
                if string == string[::-1]:
                    result=string
    # If result is empty
    if result == "":
        print 'No Palindrome found in given string'
    else:
        return result

# Testcase1:
question2('jhkhjashf')
# Output:jhkhj

# Testcase2:
question2('gfdjskghads')
# Output:No Palindrome found in given string

# Testcase3:
question2('aamadambb')
# Output:'madam'

# Testcase4:
question2('fkjdhflldshfkfsldkhjklsdhsfjafabcdeffedcbadsaksdjhf')
# Output:'abcdeffedcba'

# Testcase5:
question2('talk to hannah ottoman')
# Output:'to hannah ot'

# Testcase6:
question2('')
# Output: 'Please enter a valid string'

# Testcase7:
question2(None)
# Output: 'Please enter a valid string'

# ------------------------------------------------------------------------------

# Question3:

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
            if k not in indexa or l not in indexa:
                return "Please the check the tree you entered-Invalid Vertex"
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

# Testcase1:
x = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
print question3(x)
# Output: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}

# Testcase2:
x = {   'A': [('B', 4), ('F', 2)],
        'B': [('A', 4), ('C', 6),('F', 5)],
        'C': [('B', 6), ('D', 3),('F', 1)],
        'D': [('C', 3), ('E', 2)],
        'E': [('D', 2), ('F', 4)],
        'F': [('A', 2), ('B', 5),('C', 1), ('E', 4)] }
print question3(x)
# Output: {'A': [('F', 2), ('B', 4)], 'C': [('F', 1), ('D', 3)], 'B': [('A', 4)], 'E': [('D', 2)], 'D': [('E', 2), ('C', 3)], 'F': [('C', 1), ('A', 2)]}

# Testcase3:
x={'A': [('B', 2),('C', 10)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5),('A',10)]}
print question3(x)
# Output: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}

# Testcase4:
# A vertex was specified in the tree-but the vertex was not a key in the dictionary
x={'A': [('B', 1),('C', 10)],
 'B': [('D', 2), ('C', 5)],
 'C': [('B', 5),('A',10)]}
print question3(x)
# Output: Please the check the tree you entered-Invalid Vertex

# Testcase5:
# Adding an extra Key/Vertex with no value/edge to it
x={'A': [('B', 1),('C', 10)],
 'B': [('A', 1), ('C', 5)],
 'C': [('B', 5),('A',10)],
  'D':[('E',2)]}
print question3(x)
# Output: Please the check the tree you entered-Invalid Vertex

# ------------------------------------------------------------------------------

# Question4:

# Returns immediate parent/ancestor to the node n
def ancestor(T, n):
    no_of_rows = len(T)
    for i in range(no_of_rows):
        if T[i][n] == 1:
            return i
    return -1

#Returns the lowest common ancestor
def question4(T, r, n1, n2):
#     print len(T)
    if (n1>len(T)-1 or  n2>len(T)-1):
        return "Please enter a valid Integer in the tree"
    n1_ancestors=[]
    while n1!=r:
        n1=ancestor(T,n1)
        n1_ancestors.append(n1)
    if len(n1_ancestors)==0:
        return "Please enter a valid Integer in the tree"
    while n2!=r:
        n2=ancestor(T,n2)
        if n2==-1:
            return "Please enter a valid Integer in the tree"
        if n2 in n1_ancestors:
            return n2
    return -1

# Testcase1:
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,0,4)
# Output: 3

# Testcase2:
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,5)
# Output: Please enter a valid Integer in the tree

# Testcase3:
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,5,1)
# Output: Please enter a valid Integer in the tree

# Testcase4:
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,2)
# Output: Please enter a valid Integer in the tree

# Testcase5:
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# Output: 3

# Testcase6:
print question4([[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,2)
# Output: 0

# ------------------------------------------------------------------------------

# Question5:

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
def question5(root, n):
    count = 1
    if n>length(root) or n <0:
        return "Please enter a valid location in the Linked list"
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

# Testcase1:
print question5(r,1)
# Output: 1 number from the end is: 1

# Testcase2:
print question5(r,3)
# Output: 3 number from the end is: 2

# Testcase3:
print question5(r,5)
# Output: 5 number from the end is: 4

# Testcase4:
print question5(r,6)
# Output: 6 number from the end is: 6

# Testcase5:
print question5(r,8)
# Output: 8 number from the end is: 9

# Testcase6:
print question5(r,9)
# Output: Please enter a valid location in the Linked list

# Testcase7:
print question5(r,-1)
# Output: Please enter a valid location in the Linked list

# ------------------------------------------------------------------------------