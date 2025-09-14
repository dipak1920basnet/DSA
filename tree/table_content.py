# Replace ___ with your code

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root = None):
        self.root = root

    def get_toc(self, node = None, level = 0):
        # write your code here
        if not node:
            return None
        if node:
            print(" "*level,node.data)

        for children in node.children:
            self.get_toc(children, level + 1)

# creating our root node
root = TreeNode("Book")

# creating the children of root
child1 = TreeNode("Chapter 1")
child2 = TreeNode("Chapter 2")

# creating sections
child1_1 = TreeNode("Section 1.1")
child1_2 = TreeNode("Section 1.2")
child2_1 = TreeNode("Section 2.1")
child2_2 = TreeNode("Section 2.2")

# creating our sub-sections
child1_1_1 = TreeNode("Sub-Section 1.1.1")
child1_1_2 = TreeNode("Sub-Section 1.1.2")
child1_2_1 = TreeNode("Sub-Section 1.2.1")
child1_2_2 = TreeNode("Sub-Section 1.2.2")

child2_1_1 = TreeNode("Sub-Section 2.1.1")
child2_1_2 = TreeNode("Sub-Section 2.1.2")
child2_2_1 = TreeNode("Sub-Section 2.2.1")
child2_2_2 = TreeNode("Sub-Section 2.2.2")


# add chapters to the root node
root.add_child(child1)
root.add_child(child2)

# add sections to chapter1
child1.add_child(child1_1)
child1.add_child(child1_2)

# add sections to chapter2
child2.add_child(child2_1)
child2.add_child(child2_2)

# add subsections to section 1_1
child1_1.add_child(child1_1_1)
child1_1.add_child(child1_1_2)

# add subsections to section1_2
child1_2.add_child(child1_2_1)
child1_2.add_child(child1_2_2)

# add subsection to section2_1
child2_1.add_child(child2_1_1)
child2_1.add_child(child2_1_2)

# add subsection to section2_2
child2_2.add_child(child2_2_1)
child2_2.add_child(child2_2_2)
# creating our tree
tree = Tree(root)

# print the TOC
tree.get_toc(root,0)