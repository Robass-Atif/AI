from Task01 import Graph
from Searchalgo import BestFirstSearch, DepthFirstSearch, UniformCostSearch

class EightPuzzleProblem:
    def __init__(self, initial_state, goal_state, grid):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = Graph()
        self.grid = grid
        self._build_graph()

    def start_state(self):
        return self.initial_state

    def is_end(self, state):
        return state == self.goal_state

    def _build_graph(self):
        rows = len(self.grid)
        cols = len(self.grid[0])

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
        result = []
        i, j = self.findSpace(state)
        if i > 0:
            newState = self.swap(state, i, j, i - 1, j)
            result.append(('up', newState, 1))
        if i < len(state) - 1:
            newState = self.swap(state, i, j, i + 1, j)
            result.append(('down', newState, 1))
        if j > 0:
            newState = self.swap(state, i, j, i, j - 1)
            result.append(('left', newState, 1))
        if j < len(state[0]) - 1:
            newState = self.swap(state, i, j, i, j + 1)
            result.append(('right', newState, 1))
        return result

    def swap(self, state, i, j, newi, newj):
        newState = []
        for row in state:
            newState.append(list(row))
        newState[i][j], newState[newi][newj] = newState[newi][newj], newState[i][j]
        return tuple([tuple(row) for row in newState])

    def findSpace(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return i, j

ep = EightPuzzleProblem(((1, 2, 3), (4, 5, 6), (7, 8, 0)), ((0, 1, 2), (3, 4, 5), (6, 7, 8)), ((1, 2, 3), (4, 5, 6), (7, 8, 0)))

def priority_function(state, cost):
    return cost

bfs = BestFirstSearch(ep, priority_function)
print("Best First Search")
print(bfs.search())

dfs = DepthFirstSearch(ep)
print("Depth First Search")
print(dfs.search())

ucs = UniformCostSearch(ep)
print("Uniform Cost Search")
print(ucs.search())
