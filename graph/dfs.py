def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

graph_node = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(dfs(graph_node, 'A'))
