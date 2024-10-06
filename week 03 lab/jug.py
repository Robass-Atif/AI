from Graph import Graph
from Searchalgo import BestFirstSearch, DepthFirstSearch, UniformCostSearch

class JugProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = Graph()

    def start_state(self):
        return self.initial_state

    def is_end(self, state):
        return state == self.goal_state

    def successors(self, state):
        successors = []
        if state[0] < 4:
            successors.append(('Fill 4', (4, state[1]), 1))
        if state[1] < 3:
            successors.append(('Fill 3', (state[0], 3), 1))
        if state[0] > 0:
            successors.append(('Empty 4', (0, state[1]), 1))
        if state[1] > 0:
            successors.append(('Empty 3', (state[0], 0), 1))
        if state[0] > 0 and state[1] < 3:
            amount = min(state[0], 3 - state[1])
            successors.append(('Pour 4->3', (state[0] - amount, state[1] + amount), 1))
        if state[1] > 0 and state[0] < 4:
            amount = min(state[1], 4 - state[0])
            successors.append(('Pour 3->4', (state[0] + amount, state[1] - amount), 1))
        return successors

jug = JugProblem((4, 1), (2, 0))

def priority_function(state, cost):
    return cost

print("Best First Search")
print(BestFirstSearch(jug, priority_function).search())

print("Depth First Search")
print(DepthFirstSearch(jug).search())

print("Uniform Cost Search")
print(UniformCostSearch(jug).search())
