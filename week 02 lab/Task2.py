def dfs(graph, start_vertex):
    # List of visited nodes
    visited = []

    # Stack to store vertices of the graph
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        # Check if vertex has already been visited
        if vertex not in visited:
            visited.append(vertex)
            # Push vertex neighbors onto the stack
            stack.extend(graph.get_neighbors(vertex))

    return visited
