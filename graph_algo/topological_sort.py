vertices = ['A', 'B', 'C', 'D', 'E']  
adj_matrix = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0]
]

class Graph:
    def __init__(self, Vertices, adj_matrix):
        self.vertices = Vertices
        self.adj_matrix = adj_matrix
        self.graph = {i:[] for i in self.vertices}

    def build_graph(self):
        key = self.vertices
        # loop through matrix column
        for i in range(len(key)):
            li = self.adj_matrix[i]
            # loop through matrix row
            for j in range(len(li)):
                # in a row if there is 1 then connection is established
                if li[j] != 0:
                    self.graph[key[i]].append(key[j])
        print(self.graph)

    
new_graph = Graph(vertices, adj_matrix)
# new_graph.define_key()
new_graph.build_graph()

                    