class Graph:
    def __init__(self):
        self.vertices = []  # List to store vertex names
        self.edges = []  # List to store edges as tuples (start, end)
        self.is_directed = False  # To store whether the graph is directed
        self.adjacency_list = {}  # Dictionary to store adjacency lists

    def read_graph_from_file(self, filename):
        """
        Reads the graph from a file with the specified format.
        Input: filename - name of the file containing the graph.
        """
         # Stub: implement file reading logic
        # pass
        with open(filename, 'r') as f:
            vertex = f.readline().strip().split('_')
            if vertex[1]=='1':
                self.is_directed=True

            
            

            
            vertexlist=f.readline().strip().split() 
            for i in range(len(vertexlist)):
                self.vertices.append(vertexlist[i])

            count=f.readline().strip()

            for line in f:
                edge=line.strip().split()
                self.edges.append((edge[0],edge[1]))
                if edge[0] in self.adjacency_list:
                    self.adjacency_list[edge[0]].append(edge[1])
                else:
                   
                    self.adjacency_list[edge[0]]=[edge[1]]
                if self.is_directed == False:
                    if edge[1] in self.adjacency_list:
                        self.adjacency_list[edge[1]].append(edge[0])
                    else:
                    
                        self.adjacency_list[edge[1]]=[edge[0]]


    def get_vertex_count(self):
        """
        Returns the total number of vertices in the graph.
        Output: int - number of vertices.
        """
        return len(self.vertices)

    def get_edge_count(self):
        """
        Returns the total number of edges in the graph.
        Output: int - number of edges.
        """
        return len(self.edges)

    def is_graph_directed(self):
        """
        Returns whether the graph is directed or not.
        Output: bool - True if the graph is directed, False otherwise.
        """
        return self.is_directed

    def get_neighbors(self, vertex):
        """
        Returns the neighbors of the given vertex.
        Input: vertex - the vertex whose neighbors are to be returned.
        Output: list - list of neighboring vertices.
        """
        return self.adjacency_list.get(vertex, [])


 

def main():

    filename = input("Enter the filename: ")
    graph = Graph()
    graph.read_graph_from_file(filename)
    print("Number of vertices: ", graph.get_vertex_count())
    print("Number of edges: ", graph.get_edge_count())
    print("Is the graph directed: ", graph.is_graph_directed())

    while True:
        # Prompt for a vertex in each iteration
        vertex = input("Enter the vertex to get neighbors: ")
        
        if vertex in graph.vertices:
            print("Neighbors of ", vertex, ": ", graph.get_neighbors(vertex))
        else:
            print("Vertex not found in the graph")
        
        
        choice = input("Do you want to continue? (Y/N): ")
        if choice.upper() == 'N':  
            break
    





# Call main()
main()
