
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
