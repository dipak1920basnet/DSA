class Graph:
    def __init__(self, vertex):
        self.size = vertex + 1
        self.matrix = [[0] * self.size for i in range(self.size)]

    def build_relation(self, from_, to_, directed=False, weight=1):
        if from_ < 1 or to_ < 1:
            print("vertex size starts with 1")
            return
        self.matrix[from_][to_] = weight
        if not directed:
            self.matrix[to_][from_] = weight

        # Print Matrix

    def print_matrix(self):
        for j in range(1, len(self.matrix)):
            print(self.matrix[j][1:])


new_graph = Graph(4)
# new_graph.build_matrix()
new_graph.build_relation(1, 2, directed=True, weight=21)
new_graph.build_relation(1, 3, directed=True, weight=31)
new_graph.build_relation(2, 3, weight=20)
new_graph.build_relation(2, 4, directed=True, weight=42)
new_graph.print_matrix()
