import heapq

class SearchProblem:
    def __init__(self, graph, start, goal_state):
        self.graph = graph
        self.start = start
        self.goal_state = goal_state

    def start_state(self):
        return self.start

    def is_end(self, state):
        return state == self.goal_state

    def successors(self, state):
        node = self.graph.get_node(state)
        if node is None:
            return []
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]


class Node:
    def __init__(self, state):
        self.state = state
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, action, cost, next_node):
        self.action = action
        self.cost = cost
        self.next_node = next_node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, state):
        if state not in self.nodes:
            self.nodes[state] = Node(state)
        return self.nodes[state]

    def add_edge(self, state_from, action, cost, state_to):
        node_from = self.add_node(state_from)
        node_to = self.add_node(state_to)
        edge = Edge(action, cost, node_to)
        node_from.add_edge(edge)

    def get_node(self, state):
        return self.nodes.get(state, None)


def read_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes_section = False
        edges_section = False
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("graph"):
                nodes_section = False
                edges_section = False
            elif line.startswith("nodes"):
                nodes_section = True
                edges_section = False
            elif line.startswith("edges"):
                nodes_section = False
                edges_section = True
            elif nodes_section:
                nodes = line.split()
                for node in nodes:
                    graph.add_node(node)
            elif edges_section:
                parts = line.split()
                if len(parts) == 2:
                    state_from, state_to = parts
                    graph.add_edge(state_from, 'edge', 1, state_to)
                elif len(parts) == 3:
                    state_from, state_to, cost = parts
                    graph.add_edge(state_from, 'edge', int(cost), state_to)
    return graph









# eight puzzle problem
class EightPuzzleProblem():
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.graph = Graph()
        self._build_graph()
    
    def start_state(self):
        return self.initial_state
    
    def is_end(self, state):
        return state == ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    
    
       

    def _build_graph(self):

        rows=3
        cols=3
        


        for i in range(rows):
            for j in range(cols):
                state = (i, j)
                self.graph.add_node(state)
                if i > 0:
                    self.graph.add_edge(state, 'up', 1, (i - 1, j))
                if i < rows - 1:
                    self.graph.add_edge(state, 'down', 1, (i + 1, j))
                if j > 0:
                    self.graph.add_edge(state, 'left', 1, (i, j - 1))
                if j < cols - 1:
                    self.graph.add_edge(state, 'right', 1, (i, j + 1))            


    
class MazeProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = Graph()
        self._build_graph()

    def start_state(self):
        return self.initial_state

    def is_end(self, state):
        return state == self.goal_state

    def successors(self, state):
        node = self.graph.get_node(state)
        if node is not None:
            return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
        return []

    def _build_graph(self):
        
        rows = self.goal_state[0] + 1
        cols = self.goal_state[1] + 1
        for i in range(rows):
            for j in range(cols):
                state = (i, j)
                self.graph.add_node(state)
                if i > 0:
                    self.graph.add_edge(state, 'up', 1, (i - 1, j))
                if i < rows - 1:
                    self.graph.add_edge(state, 'down', 1, (i + 1, j))
                if j > 0:
                    self.graph.add_edge(state, 'left', 1, (i, j - 1))
                if j < cols - 1:
                    self.graph.add_edge(state, 'right', 1, (i, j + 1))





class MissionariesCannibalsProblem:
   def __init__(self, initial_state, goal_state):
         self.initial_state = initial_state
         self.goal_state = goal_state
         self.graph = Graph()
         self.build_graph()

   def start_state(self):
           return self.initial_state
   def is_end(self, state):
              return state == self.goal_state
   
   def successors(self, state):
         node = self.graph.get_node(state)
         if node is not None:
              return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
         return []

   def build_graph(self):
   

        for m in range(3):
            for c in range(3):
                for b in range(2):
                    state = (m, c, b)
                    self.graph.add_node(state)
                    if b == 1:
                        self.graph.add_edge(state, 'move 1M', 1, (m - 1, c, 0))
                        self.graph.add_edge(state, 'move 2M', 1, (m - 2, c, 0))
                        self.graph.add_edge(state, 'move 1C', 1, (m, c - 1, 0))
                        self.graph.add_edge(state, 'move 2C', 1, (m, c - 2, 0))
                        self.graph.add_edge(state, 'move 1M 1C', 1, (m - 1, c - 1, 0))
                    else:
                        self.graph.add_edge(state, 'move 1M', 1, (m + 1, c, 1))
                        self.graph.add_edge(state, 'move 2M', 1, (m + 2, c, 1))
                        self.graph.add_edge(state, 'move 1C', 1, (m, c + 1, 1))
                        self.graph.add_edge(state, 'move 2C', 1, (m, c + 2, 1))
                        self.graph.add_edge(state, 'move 1M 1C', 1, (m + 1, c + 1, 1))




       




# main function
