import heapq
from Graph import Graph, Node, Edge



class BestFirstSearch:
    def __init__(self, problem, priority_function):
        self.problem = problem
        self.priority_function = priority_function

    def search(self):
        start = self.problem.start_state()
        
        # Check if the start state is already the goal
        if self.problem.is_end(start):
            return [start]
        
        frontier = []
        heapq.heappush(frontier, (self.priority_function(start, 0), start))
        explored = set()
        print(f"Start State: {start}")
        parent = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            priority, state = heapq.heappop(frontier)
            
            # Check if we've reached the goal state
            if self.problem.is_end(state):
                path = []
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path)), cost_so_far[path[0]]  # Fix here, use path[0]

            # Explore successors
            for action, next_state, cost in self.problem.successors(state):
                new_cost = cost_so_far[state] + cost
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = self.priority_function(next_state, new_cost)
                    heapq.heappush(frontier, (priority, next_state))
                    parent[next_state] = state
        
        # Return None if no path is found
        return None



# Uniform Cost Search (UCS)
class UniformCostSearch:
    def __init__(self, problem):
        self.problem = problem

    def ucs_priority(self, state, cost):
        # Priority is just the cumulative cost
        return cost

    def search(self):
        bfs = BestFirstSearch(self.problem, self.ucs_priority)
        return bfs.search()

# Depth First Search (DFS)
class DepthFirstSearch:
    def __init__(self, problem):
        self.problem = problem

    def dfs_priority(self, state, cost):
        # Higher depth is prioritized, emulate DFS with negative depth
        return -cost

    def search(self):
        bfs = BestFirstSearch(self.problem, self.dfs_priority)
        return bfs.search()

# Iterative Deepening Search (IDS)
class IterativeDeepeningSearch:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        start = self.problem.start_state()

        def dls(state, depth, parent, cost):
            if self.problem.is_end(state):
                path = []
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path)), cost  # Return the path and cost

            if depth == 0:
                return None

            # Explore successors
            for action, next_state, next_cost in self.problem.successors(state):
                if next_state not in parent:
                    parent[next_state] = state
                    result = dls(next_state, depth - 1, parent, cost + next_cost)
                    if result is not None:
                        return result
            return None

        depth = 0
        while True:
            parent = {start: None}
            result = dls(start, depth, parent, 0)
            if result is not None:
                return result
            depth += 1

        return None


# Example problem class for testing

