# Replace ___ with your code


class MinHeap:
    def __init__(self):
        self.heap = []

    # return the number of nodes in a heap
    def size(self):
        return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap values
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right_child
    def right_child(self, index):
        return 2 * index + 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while (
            self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]
        ):
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index

    # delete from heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        index = 0
        while self.has_left_child(index):
            left_value_index = self.left_child(index)
            root_value = self.heap[index]
            a = self.heap[left_value_index]
            if self.has_right_child(index):
                right_value_index = self.right_child(index)
                b = self.heap[right_value_index]
                if b < a and root_value > b:
                    self.swap(right_value_index, index)
                    index = right_value_index
                    continue
            if root_value > a:
                self.swap(left_value_index, index)
                index = left_value_index
        
        return root


# example usage:
heap = MinHeap()
array = [1, 2, 5, 3, 4, 6, 7]
for i in array:
    heap.insert(i)
print(f"Root: {heap.extract_min()}")
print(heap)
