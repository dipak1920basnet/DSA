class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, Node):
        self.left = Node

    def add_right(self,Node):
        self.right = Node

class Tree:
    def __init__(self, node):
        self.root = node

    def pre_order(self, root):
        if root is None:
            return None
        
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)

    def in_order(self, root):
        if root is None:
            return None
        
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)

