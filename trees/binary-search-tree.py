class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insertHelper(self.root, new_val)

    def search(self, find_val):
        return self.searchHelper(self.root, find_val)
        
    def print_tree(self):
        return self.preorder_print(self.root, None)

    def insertHelper(self, start, new_val):
        if new_val < start.value:
            if start.left == None:
                start.left = Node(new_val)
            else:
                self.insertHelper(start.left, new_val)
        if new_val > start.value:
            if start.right == None:
                start.right = Node(new_val)
            else:
                self.insertHelper(start.right, new_val)
    
    def searchHelper(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            if start.value > find_val:
                return self.searchHelper(start.left, find_val)
            if start.value < find_val:
                return self.searchHelper(start.right, find_val)
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

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

print tree.print_tree()