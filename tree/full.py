# Replace ___ with your code


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

    def is_full_binary_tree(self, node=None):
        # write your code here
        if node is None:
            node = self.root 

        if not node.left and not node.right:
            return True

        if node.left and node.right:
            return (self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right))
         
        return False


# take user input
input_str = input()
inputs = input_str.split()

root, node1, node2, node3, node4, node5, node6 = [
    BinaryTreeNode(val.strip()) for val in inputs
]

root.add_left_child(node1)
root.add_right_child(node2)
node1.add_left_child(node3)
node1.add_right_child(node4)
node2.add_left_child(node5)
node2.add_right_child(node6)

# call the function
tree = BinaryTree(root)
print(tree.is_full_binary_tree())
