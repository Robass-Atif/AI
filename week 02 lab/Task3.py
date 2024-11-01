def bfs(graph, start_vertex):
    visited, queue = [], [start_vertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.get_neighbors(vertex))
    return visited

def bfs_distance(graph, start_vertex, end_vertex):
    visited, queue, distance = [], [start_vertex], 0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.get_neighbors(vertex))
            if vertex == end_vertex:
                return distance
            distance += 1
    return 0

def bfs_number_of_levels(graph, start_vertex, end_vertex):
    visited, queue, level = [], [start_vertex], 0
    while True:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.get_neighbors(vertex))
            if vertex == end_vertex:
                return level
            level += 1
    return 0

def bfs_draw_tree(graph, start_vertex):
    visited, queue = [], [start_vertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.get_neighbors(vertex))
            print(vertex)
