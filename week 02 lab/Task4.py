def is_acyclic(graph, start_vertex):
    visited, stack = [], [(start_vertex, [start_vertex])]  
    while stack:
        vertex, path = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor in path:
                return False
            stack.append((neighbor, path + [neighbor]))
    return True

def pathOfCycle(graph, start_vertex):
    visited, stack = [], [(start_vertex, [start_vertex])]
    while stack:
        vertex, path = stack.pop()
        if vertex in visited:
            if vertex == path[0]:
                return path
            continue
        visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

def numOfCycles(graph, start_vertex):
    visited, stack, count = [], [(start_vertex, [start_vertex])], 0
    while stack:
        vertex, path = stack.pop()
        if vertex in visited:
            if vertex == path[0]:
                count += 1
            continue
        visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return count
