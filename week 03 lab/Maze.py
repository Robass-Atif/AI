from Graph import Graph
from Searchalgo import BestFirstSearch,DepthFirstSearch,UniformCostSearch

class MazeProblem:
    def __init__(self, initial_state, goal_state,grid):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = Graph()
        self.grid=grid
        self._build_graph()

    def start_state(self):
        return self.initial_state

    def is_end(self, state):
        return state == self.goal_state

    def successors(self, state):
       result=[]
       node = self.graph.get_node(state)
       if node is not None:
           for edge in node.edges:
               if self.grid[edge.next_node.state[0]][edge.next_node.state[1]] != 8:
                   result.append((edge.action, edge.next_node.state, edge.cost))
       
       return result
        

    def _build_graph(self):
        rows=len(self.grid)
        cols=len(self.grid[0])

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
       





grid = [
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0]
] 

problem = MazeProblem((0, 0), (3, 3),grid)
def priority_function(state, cost):
    return cost
bfs=BestFirstSearch(problem,priority_function)
print(bfs.search())
dfs=DepthFirstSearch(problem)
print(dfs.search())
ucs=UniformCostSearch(problem)
print(ucs.search())
