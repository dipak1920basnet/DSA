# Replace ___ with your code

class MinHeap:
    def __init__(self):
        self.heap = []

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap elements
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    def insert(self, value):
        # a = self.heap
        self.heap.append(value)

        ind = len(self.heap) - 1
        while self.has_parent(ind) and self.heap[self.parent(ind)] > self.heap[ind] :
            self.swap(ind, self.parent(ind))
            ind = (self.parent(ind))
        return self.heap

        

heap = MinHeap()
array = [70, 20, 30, 40, 50, 60, 10, 80]
for i in array:
    heap.insert(i)
print(heap)