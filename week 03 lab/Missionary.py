from Graph import Graph
from Searchalgo import BestFirstSearch, DepthFirstSearch, UniformCostSearch, IterativeDeepeningSearch

class Missionary:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.graph = Graph()

    def start_state(self):
        return self.start

    def is_end(self, state):
        return state == self.goal

    def successors(self, state):
        result = []
        # Move with one missionary
        if state[2] == 1:
            result.append(('Move left', (state[0], state[1], 0), 1))
            # Move with one cannibal 
        if state[2] == 0:
            if state[0] > 0:  # Move with one cannibal
                result.append(('Move right with one cannibal', (state[0] - 1, state[1], 1), 1))
            if state[1] > 0:  # Move with one missionary
                result.append(('Move right with one missionary', (state[0], state[1] - 1, 1), 1))
            if state[0] > 0 and state[1] > 0:  # Move with both
                result.append(('Move right with both', (state[0] - 1, state[1] - 1, 1), 1))
        return result

start_state = (3, 3, 0)
goal_state = (0, 0, 1)

problem = Missionary(start_state, goal_state)

def priority_function(state, cost):
    return cost

bfs = BestFirstSearch(problem, priority_function)
print("Breath First Seaarch")
print(bfs.search())

dfs = DepthFirstSearch(problem)
print("Depth First Search")
print(dfs.search())

ucs = UniformCostSearch(problem)
print("Uniform Cost Search")
print(ucs.search())

ids=IterativeDeepeningSearch(problem)
print("Iterative Deepening Search")
print(ids.search())

