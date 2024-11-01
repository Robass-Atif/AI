def distance_dijkstra(graph, start_vertex, end_vertex):
    path = []
    priority_queue = {vertex: float('inf') for vertex in graph.vertices}
    priority_queue[start_vertex] = 0

    for neighbor in graph.adjacency_list[start_vertex]:
        priority_queue[neighbor] = graph.edges[(start_vertex, neighbor)]       
    current = start_vertex
    priority_queue.pop(start_vertex)

    while priority_queue:
        current_vertex = min(priority_queue, key=priority_queue.get)
        if current_vertex == end_vertex:
            break
        current_distance = priority_queue.pop(current_vertex)
        path.append((current, current_vertex, current_distance))
        current = current_vertex
        for neighbor in graph.adjacency_list[current_vertex]:
            distance = current_distance + graph.edges[(current_vertex, neighbor)]
            if distance < priority_queue[neighbor]:
                priority_queue[neighbor] = distance

    return (current_distance, path)

def distance_bellman_ford(graph, start_vertex, end_vertex):
    distance = {vertex: float('inf') for vertex in graph.vertices}
    distance[start_vertex] = 0
    path = []

    for _ in range(len(graph.vertices) - 1):
        for (u, v), weight in graph.edges.items():
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                path.append((u, v, weight))

    for (u, v), weight in graph.edges.items():
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains a negative-weight cycle")
            return float('inf')

    shortest_path = []
    current_vertex = end_vertex
    while current_vertex != start_vertex:
        for (u, v, weight) in path:
            if v == current_vertex and distance[u] + weight == distance[v]:
                shortest_path.append((u, v, weight))
                current_vertex = u
                break
    shortest_path.reverse()

    return (distance[end_vertex], shortest_path)
