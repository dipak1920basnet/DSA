class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

root_node = BinaryTreeNode("root")
left_node = BinaryTreeNode("left")
right_node = BinaryTreeNode("right")


root_node.add_left_child(left_node)
root_node.add_right_child(right_node)

tree = BinaryTree(root_node)