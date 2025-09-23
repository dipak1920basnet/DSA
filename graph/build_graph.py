class Graph:
    def __init__(self, vertex):
        self.size = vertex
        self.matrix = []

    # Generate matrix
    def build_matrix(self):
        for i in range(self.size + 1):
            inside = []
            for j in range(self.size + 1):
                inside.append(0)
            self.matrix.append(inside)

    # Print Matrix
    def print_matrix(self):
        for j in range(1, len(self.matrix)):
            print(self.matrix[j][1:])

    def build_relation(self, from_, to_, directed=False, weight=1):
        if from_ < 1 or to_ < 1:
            print("vertex size starts with 1")
            return
        self.matrix[from_][to_] = weight
        if not directed:
            self.matrix[to_][from_] = weight


new_graph = Graph(4)
new_graph.build_matrix()
new_graph.build_relation(1, 2, directed=True, weight=21)
new_graph.build_relation(1, 3, directed=True, weight=31)
new_graph.build_relation(2, 3, weight=20)
new_graph.build_relation(2, 4, directed=True, weight=42)
new_graph.print_matrix()
