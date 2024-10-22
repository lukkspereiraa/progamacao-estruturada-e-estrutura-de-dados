class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return 
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return 
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def print_pre_order(self, node):
        if node:
            print(node.value)

            self.print_pre_order(node.left)

            self.print_pre_order(node.right)
        

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(70)
bst.insert(60)
bst.insert(40)
bst.insert(80)
bst.print_pre_order(bst.root)