# Build a list of list for adjencty list
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    def build_list(self):
        for _ in range(self.vertex + 1):
            self.graph.append([])

    def add_vertex(self, vertexs: set, is_directed=False, weight=None):
        from_, to_ = vertexs
        if from_ <= 0 or to_ <= 0:
            print("There should be atlease one vertex")

        if not weight:
            self.graph[from_].append(to_)
            if not is_directed:
                self.graph[to_].append(from_)

        if weight:
            self.graph[from_].append((to_, weight))
            if not is_directed:
                self.graph[to_].append((from_, weight))

    def print_list(self):
        for i in range(1, len(self.graph)):
            print(self.graph[i])


new_graph = Graph(4)
new_graph.build_list()
new_graph.print_list()
