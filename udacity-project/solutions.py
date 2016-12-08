from pprint import pprint

"""Question 1
Given two strings s and t, determine whether some anagram of t is a substring 
of s. For example: if s = "udacity" and t = "ad", then the function returns 
True. Your function definition should look like: question1(s, t) and return 
a boolean True or False."""

def question1(s, t):
	""" Determines if string2 is a substring of string1 (forwards or backwards)
		Inputs: string1, string2
		Ouput: Boolean"""
	if s and t:
		if t in s:
			return True
		if t[::-1] in s:
			return True
	return False

"""
# Edge Cases
print question1(None, None) # Should print False
print question1('', '') # Should print False
print question1('something', '') # Should print False
print question1('', 'something') # Should print False
# Test Cases
print question1("udacity", "ad") # Should print True
print question1("test", "ad") # Should print False
print question1("testing", "test") # Should print True
"""


"""Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string."""

def question2(a):
	"""Determines the longest palindromic substring contained in a given string
		Inputs: string
		Outputs: string"""
	if a == None or a == '':
		return None
	longest = ''
	for index in range(len(a)):
		result = question2_helper(a[index:])
		if len(result) > len(longest):
			longest = result
	return longest

def question2_helper(a):
	result = ''
	for length in range(len(a) + 1):
		if is_a_palindrome(a[:length]) and length > len(result):
			result = a[:length]
	return result

def is_a_palindrome(a):
	if a == a[::-1]:
		return True
	return False

"""
# Edge Cases
print question2(None) # Prints "None"
print question2('') # Prints "None"
print question2("Split mirror tilpS") # Prints "ror", not "Split tilpS"
# Test Cases
print question2("No significant palindromes") # Prints "ifi"
print question2("Whole string gnirts elohW") # Prints the whole string
print question2("A substring example elpmaxe") # Prints "example elpmaxe"
"""


"""Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. 
The function definition should be question3(G)"""

class Node(object):
	def __init__(self, value):
		self.value = value
		self.edges = []
		self.visited = False

class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

class Graph(object):
	def __init__(self, nodes=None, edges=None):
		self.nodes = nodes or []
		self.edges = edges or []
		self.node_names = []
		self._node_map = {}

	def insert_node(self, new_node_val):
		"Insert a new node with value new_node_val"
		new_node = Node(new_node_val)
		self.nodes.append(new_node)
		self._node_map[new_node_val] = new_node
		return new_node

	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		"Insert a new edge, creating new nodes if necessary"
		nodes = {node_from_val: None, node_to_val: None}
		for node in self.nodes:
			if node.value in nodes:
				nodes[node.value] = node
				if all(nodes.values()):
					break
		for node_val in nodes:
			nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
		node_from = nodes[node_from_val]
		node_to = nodes[node_to_val]
		new_edge = Edge(new_edge_val, node_from, node_to)
		node_from.edges.append(new_edge)
		node_to.edges.append(new_edge)
		self.edges.append(new_edge)

	def get_adjacency_list(self):
		self.adjacencyList = {}
		for edge in self.edges:
			if edge.node_from.value in self.adjacencyList:
				self.adjacencyList[edge.node_from.value].append((
											edge.node_to.value, edge.value))
			else:
				self.adjacencyList[edge.node_from.value] = [(
											edge.node_to.value, edge.value)]
			if edge.node_to.value in self.adjacencyList:
				self.adjacencyList[edge.node_to.value].append((
											edge.node_from.value, edge.value))
			else:
				self.adjacencyList[edge.node_to.value] = [(
											edge.node_from.value, edge.value)]
		return self.adjacencyList

	def _clear_visited(self):
		for node in self.nodes:
			node.visited = False

	def bfs(self, node):
		self._clear_visited()
		edgeList = []
		node_queue = [node]
		node.visited = True
		while node_queue:
			node = node_queue.pop(0)
			for edge in node.edges:
				if not edge.node_to.visited:
					node_queue.append(edge.node_to)
					edge.node_to.visited = True
					edgeList.append(edge)
				elif not edge.node_from.visited:
					node_queue.append(edge.node_from)
					edge.node_from.visited = True
					edgeList.append(edge)
		return edgeList

def question3(G):
	minimumPathCost = float("inf")
	minimumPath = None
	for node in G.nodes:
		path = G.bfs(node)
		pathCost = 0
		for branch in path:
			pathCost += branch.value
		if pathCost < minimumPathCost:
			minimumPathCost = pathCost
			minimumPath = path
	minimumSpanningTree = Graph()
	for branch in minimumPath:
		minimumSpanningTree.insert_edge(branch.value, branch.node_from.value, 
										branch.node_to.value)
	return minimumSpanningTree.get_adjacency_list()

"""
graph = Graph()
graph.insert_edge(2, 'A', 'B')
graph.insert_edge(5, 'B', 'C')
graph.insert_edge(10, 'A', 'C')
pprint(graph.get_adjacency_list()) # A simple case
# Full graph:
# {'A': [('B', 2), ('C', 10)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5), ('A', 10)]}
pprint(question3(graph))
# Minimum spanning tree should be:
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5)]}

graph2 = Graph()
graph2.insert_edge(1, 'A', 'B')
graph2.insert_edge(8, 'B', 'C')
graph2.insert_edge(2, 'C', 'D')
graph2.insert_edge(9, 'A', 'D')
pprint(graph2.get_adjacency_list()) # An hourglass case
# Full graph:
# {'A': [('B', 1), ('D', 9)],
#  'B': [('A', 1), ('C', 8)], 
#  'C': [('B', 8), ('D', 2)], 
#  'D': [('A', 9), ('C', 2)]}
pprint(question3(graph2))
# Minimum spanning tree should be:
# {'A': [('B', 1)],
#  'B': [('A', 1), ('C', 8)], 
#  'C': [('B', 8), ('D', 2)], 
#  'D': [('C', 2)]}

graph3 = Graph()
graph3.insert_edge(1, 'A', 'B')
graph3.insert_edge(2, 'B', 'C')
graph3.insert_edge(1, 'C', 'D')
graph3.insert_edge(2, 'D', 'E')
graph3.insert_edge(1, 'E', 'F')
graph3.insert_edge(2, 'F', 'A')
pprint(graph3.get_adjacency_list()) # An alternating circle case
# Full graph:
# {'A': [('B', 1), ('F', 2)],
#  'B': [('A', 1), ('C', 2)], 
#  'C': [('B', 2), ('D', 1)], 
#  'D': [('C', 1), ('E', 2)], 
#  'E': [('D', 2), ('F', 1)], 
#  'F': [('E', 1), ('A', 2)]}
pprint(question3(graph3))
# Minimum spanning tree should have one of the "2" edges removed:
# {'A': [('B', 1), ('F', 2)],
#  'B': [('A', 1), ('C', 2)],
#  'C': [('B', 2), ('D', 1)],
#  'D': [('C', 1)],
#  'E': [('F', 1)],
#  'F': [('A', 2), ('E', 1)]}
"""


"""Question 4
Find the least common ancestor between two nodes on a binary search tree. The 
least common ancestor is the farthest node from the root that is an ancestor 
of both nodes. For example, the root is a common ancestor of all nodes on the 
tree, but if both nodes are descendents of the root's left child, then that 
left child might be the lowest common ancestor. You can assume that both nodes 
are in the tree, and the tree itself adheres to all BST properties. The 
function definition should look like question4(T, r, n1, n2), where T is the 
tree represented as a matrix, where the index of the list is equal to the 
integer stored in that node and a 1 represents a child node, r is a 
non-negative integer representing the root, and n1 and n2 are non-negative 
integers representing the two nodes in no particular order. For example, one 
test case might be

question4([[0, 1, 0, 0, 0],
		   [0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0],
		   [1, 0, 0, 0, 1],
		   [0, 0, 0, 0, 0]],
		  3,
		  1,
		  4)
and the answer would be 3."""

class BST_Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = BST_Node(root)

	def insert(self, new_val):
		self.insertHelper(self.root, new_val)

	def search(self, value_1, value_2):
		return self.searchHelper(self.root, value_1, value_2)
		
	def print_tree(self):
		return self.preorder_print(self.root, None)

	def insertHelper(self, start, new_val):
		if new_val < start.value:
			if start.left == None:
				start.left = BST_Node(new_val)
			else:
				self.insertHelper(start.left, new_val)
		if new_val > start.value:
			if start.right == None:
				start.right = BST_Node(new_val)
			else:
				self.insertHelper(start.right, new_val)
	
	def searchHelper(self, start, value_1, value_2):
		if start:
			traversal = str(start.value)
			if start.value == value_1 or start.value == value_2:
				return traversal
			if start.value > value_1 and start.value > value_2:
				return self.searchHelper(start.left, value_1, value_2)
			if start.value < value_1 and start.value < value_2:
				return self.searchHelper(start.right, value_1, value_2)
			return traversal
		return False
		
	def preorder_print(self, start, traversal):
		if start:
			traversal = str(start.value)
			left = self.preorder_print(start.left, traversal)
			right = self.preorder_print(start.right, traversal)
			if left:
				traversal += '-' + left
			if right:
				traversal += '-' + right
			return traversal
		return False

def question4(T, r, n1, n2):
	tree = BST(r)
	nodes = [r]
	while len(nodes) > 0:
		row = T[nodes[0]]
		for column in range(len(row)):
			if row[column] == 1:
				tree.insert(column)
				nodes.append(column)
		del(nodes[0])
	return tree.search(n1, n2)

"""
print question4([[0, 1, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[1, 0, 0, 0, 1],
				[0, 0, 0, 0, 0]],
				3,
				1,
				4)
# Should print "3"

print question4([[0, 1, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0],
				[1, 0, 1, 0, 0]],
				4,
				1,
				2)
# Should print "2"

print question4([[0, 0, 0, 0, 0],
				[0, 0, 0, 1, 0],
				[0, 0, 0, 0, 0],
				[0, 0, 1, 0, 1],
				[0, 0, 0, 0, 0]],
				1,
				2,
				4)
# Should print "3"
"""


"""Question 5
Find the element in a singly linked list that's m elements from the end. For 
example, if a linked list has 5 elements, the 3rd element from the end is the 
3rd element. The function definition should look like question5(ll, m), where 
ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a 
node in the linked list. Return the value of the node at that position.
"""
class LinkedListNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		
	def append(self, new_element):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element
	
	def getStack(self):
		stack = []
		if self.head:
			current = self.head
			stack.append(current.data)
			while current.next:
				current = current.next
				stack.append(current.data)
		return stack

def question5(ll, m):
	stack = ll.getStack()
	if m < 1 or m > len(stack):
		return None
	return stack[-m]

ll = LinkedList(LinkedListNode(1))
for element in range(2, 7):
	ll.append(LinkedListNode(element))

print question5(ll, 0) # Should print "None"
print question5(ll, 1) # Should print "6"
print question5(ll, 4) # Should print "3"
print question5(ll, 6) # Should print "1"
print question5(ll, 7) # Should print "None"
