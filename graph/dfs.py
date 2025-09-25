graph_adj_list = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def dfs_traversal(adj_list: dict, vertex):
    stack = [vertex]
    visisted = []
    while stack:
        node = stack.pop()
        if node not in visisted:
            visisted.append(node)
            for j in adj_list[node]:
                if j not in visisted:
                    stack.append(j)
    return visisted


print(dfs_traversal(graph_adj_list, "A"))
