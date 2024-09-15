









def distance_dijkstra(graph, start_vertex, end_vertex): 
    # Return distance and path as (distance, [(A,B,2),(B,C,3)])
    path = []
    priority_queue = {vertex: float('inf') for vertex in graph.vertices}
    priority_queue[start_vertex] = 0
    # first set the values of start_vertex neighbors
    for neighbor in graph.adjacency_list[start_vertex]:
        priority_queue[neighbor] = graph.edges[(start_vertex, neighbor)]       
    current=start_vertex
    priority_queue.pop(start_vertex)

    while priority_queue:
        # get the vertex with the minimum distance
        current_vertex = min(priority_queue, key=priority_queue.get)
        # if the current vertex is the end vertex, break
        if current_vertex == end_vertex:
            break
        # get the distance of the current vertex
        current_distance = priority_queue.pop(current_vertex)
        # add the current vertex to the path
        path.append((current, current_vertex, current_distance))
        # update the current vertex
        current = current_vertex
        # relax the current vertex neighbors
        for neighbor in graph.adjacency_list[current_vertex]:
            distance = current_distance + graph.edges[(current_vertex, neighbor)]
            if distance < priority_queue[neighbor]:
                priority_queue[neighbor] = distance

    return (current_distance, path)        



    # BELLMEOM FORD ALGORITHM FOR NEGITIVE
def distance_bellman_ford(graph, start_vertex, end_vertex):
    # Initialize the variables
    distance = {vertex: float('inf') for vertex in graph.vertices}
    distance[start_vertex] = 0
    path = []

    # Relax it fro V-1 times
    for a in range(len(graph.vertices) - 1):
        for (u, v), weight in graph.edges.items():
            # relax the vertex
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                
                path.append((u, v, weight))

    # Check for negitivity
    for (u, v), weight in graph.edges.items():
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains a negative-weight cycle")
            return float('inf')

    # build a path TO RETURN 
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




