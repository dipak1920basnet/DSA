class Graph:
    def __init__(self, vertex):
        self.size = vertex
        self.matrix = []
        
    # Generate matrix
    def build_matrix(self):
        for i in range(self.size):
            inside = []
            for j in range(4):
                inside.append(0)
            self.matrix.append(inside)

    # Print Matrix
    def print_matrix(self):
        for j in self.matrix:
            print(j)

new_graph = Graph(4)
new_graph.build_matrix()
new_graph.print_matrix()

    
 



