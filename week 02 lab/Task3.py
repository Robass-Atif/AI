

def bfs(graph, start_vertex):
    # visited list
    visited=[]
    # queue
    queue=[start_vertex]

    # while loop
    while queue:
     # first element from queue
       vertex= queue.pop(0)
       #    if vertex not in result array
       if vertex not in visited:
        #    add in array
           visited.append(vertex)
        #    add in queue
           queue.append()
           queue.extend(graph.get_neighbors(vertex))


def bfs_distance(graph, start_vertex,end_vertex): #return distance as 
    # visited list
    visited=[]
    # queue
    queue=[start_vertex]
    # distance
    distance=0
    # while loop
    while queue:
     # first element from queue
       vertex= queue.pop(0)
       #    if vertex not in result array
       if vertex not in visited:
        #    add in array
           visited.append(vertex)
        #    add in queue
           queue.append()
           queue.extend(graph.get_neighbors(vertex))
           if vertex==end_vertex:
               return distance
           distance+=1
    return 0    


def bfs_number_of_levels(graph, start_vertex,end_vertex): #return
   visited=[]
   # queue
   queue=[start_vertex]
   # level
   level=0
   while True:
       temp=queue.pop(0)
      #  check if vertex not in visited
       if temp not in visited:
           visited.append(temp)
           queue.extend(graph.get_neighbors(temp))
            #  compare with end vertex
           if temp==end_vertex:
               return level
           level+=1
   return 0

def bfs_draw_tree(graph, start_vertex):
      visited=[]
      queue=[start_vertex]
      while queue:
         vertex= queue.pop(0)
         if vertex not in visited:
               visited.append(vertex)
               queue.extend(graph.get_neighbors(vertex))
               print(vertex)  
               

