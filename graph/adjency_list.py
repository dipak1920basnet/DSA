# Build a list of list for adjencty list
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        # builds empty adjency list
        self.graph = [[] for _ in range(self.vertex + 1)]

    # add vertices to graph
    def add_vertex(self, edges: tuple[int, int], is_directed=False, weight=None):
        from_, to_ = edges
        length = len(self.graph)
        if from_ not in range(1, length) or to_ not in range(1, length):
            raise ValueError(
                f"There edge range should be in between 1 to {self.vertex}"
            )

        if not weight:
            self.graph[from_].append(to_)
            if not is_directed:
                self.graph[to_].append(from_)

        if weight:
            self.graph[from_].append((to_, weight))
            if not is_directed:
                self.graph[to_].append((from_, weight))

    # prints the ajdency list
    def print_list(self):
        for i in range(1, len(self.graph)):
            print(f"{i} -> {self.graph[i]}")


new_graph = Graph(4)
new_graph.print_list()
