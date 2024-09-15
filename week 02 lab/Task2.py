
# DFS ALGORITHM OF GRAPH
def dfs(graph, start_vertex):
    # list of visted nodes
    visited = []

    # stack to store vertex of graph
    stack = [start_vertex]

    while stack:

        vertex = stack.pop()
        # check either vertex present in list or not
        if vertex not in visited:
            visited.append(vertex)
            # push vertex neighbour in stack
            stack.extend(graph.get_neighbors(vertex))


    return visited





    


   