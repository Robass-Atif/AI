

def is_acyclic(graph, start_vertex):
    visited = []
    stack = [(start_vertex, [start_vertex])]  
    
    while stack:
        vertex, path = stack.pop()
        
        if vertex in visited:
            continue
        
        visited.append(vertex)
        
        for neighbor in graph.adjacency_list[vertex]:
            # Check 
            if neighbor in path:
                return False
            
            # Add the neighbor 
            stack.append((neighbor, path + [neighbor]))
    
    return True  

# PATH OF CYCLE WHICH HAVE CYCLE
def pathOfCycle(graph, start_vertex):
    visited = []
    # (vertex, path)
    stack = [(start_vertex, [start_vertex])]  
    
    while stack:
        # pop
        vertex, path = stack.pop()
        
        if vertex in visited:
            # CYCLE DETECTED
            if vertex == path[0]:  
                return path  
            continue
        
        visited.append(vertex)
        
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return None  

# TELL THAT HOW MANY NUM OF CYCLE IN GRAPH
def numOfCycles(graph, start_vertex): #return number cycle
    visited=[]
    stack=[(start_vertex, [start_vertex])]
    count=0
    while stack:
        vertex, path=stack.pop()
        if vertex in visited:
            if vertex==path[0]:
                count+=1
            continue
        visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in visited:
                stack.append((neighbor, path+[neighbor]))

    return count



    