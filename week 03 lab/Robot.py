from Graph import Graph
from Searchalgo import BestFirstSearch,DepthFirstSearch,UniformCostSearch,IterativeDeepeningSearch

class RobotProblem:
    def __init__(self, initial_state, goal_state,grid):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = Graph()
        self.grid=grid
        self._build_graph()
        self.grid=grid

    def start_state(self):
        return self.initial_state

    def is_end(self, state):
        return state == self.goal_state

    

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
    def successors(self, state):
        # first check if the state is valid  if there 8 then in blockage
        result = []
        if self.grid[state[0]][state[1]] == 8:
            return result
        # if not then check for the successors
        node = self.graph.get_node(state)
        if node is not None:
            return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
    

grid = [
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0]
]    
problem = RobotProblem((0, 0), (3, 3),grid)
def priority_function(state, cost):
    return cost
bfs=BestFirstSearch(problem,priority_function)
print("Best First Search")
print(bfs.search())
dfs=DepthFirstSearch(problem)
print("Depth First Search")
print(dfs.search())
ucs=UniformCostSearch(problem)
print("Uniform Cost Search")
print(ucs.search())

ids=IterativeDeepeningSearch(problem)
print("Iterative Deepening Search")
print(ids.search())

