import random

class MDPGrid:
    def __init__(self, grid, start_state, end_states, slip_prob=0.1):
        # Use the input grid, start state, and end states
        self.grid = grid
        self.size = len(grid)  # Automatically determine grid size based on input
        self.start_state_pos = start_state  # Starting position
        self.end_states = end_states  # List of END states with rewards
        self.slip_prob = slip_prob  # Probability of slipping into unintended state

    def start_state(self):
        return self.start_state_pos

    def is_goal(self, state):
        return state in self.end_states

    def actions(self, state):
        # Actions: 'UP', 'DOWN', 'LEFT', 'RIGHT'
        actions = []
        x, y = state
        if x > 0:
            actions.append('UP')
        if x < self.size - 1:
            actions.append('DOWN')
        if y > 0:
            actions.append('LEFT')
        if y < self.size - 1:
            actions.append('RIGHT')
        return actions

    def get_next_state(self, state, action):
        x, y = state
        if action == 'UP':
            return (x - 1, y)
        elif action == 'DOWN':
            return (x + 1, y)
        elif action == 'LEFT':
            return (x, y - 1)
        elif action == 'RIGHT':
            return (x, y + 1)

    def transition_prob(self, state, action, next_state):
  
        intended_next_state = self.get_next_state(state, action)
        
        if next_state == intended_next_state:
          
            return 1 - self.slip_prob
 
        possible_slips = [self.get_next_state(state, a) for a in self.actions(state) if a != action]
        if next_state in possible_slips:
    
            return self.slip_prob / len(possible_slips)
        
        return 0 

    def reward(self, state, action, next_state):
    
        x, y = next_state
        return self.grid[x][y]

    def policy_evaluation(self, policy, discount=1, epsilon=0.01):
     
        value = [[0 for _ in range(self.size)] for _ in range(self.size)]
        delta = float('inf')
        
        while delta > epsilon:
            delta = 0
            for x in range(self.size):
                for y in range(self.size):
                    state = (x, y)
                    if self.is_goal(state):
                        continue
                    v = value[x][y]
                  
                    action = policy[state]
                    total_value = 0
                    for next_state in self.actions(state):
                        prob = self.transition_prob(state, action, self.get_next_state(state, action))
                        reward = self.reward(state, action, next_state)
                        total_value += prob * (reward + discount * value[next_state[0]][next_state[1]])
                    value[x][y] = total_value
                    delta = max(delta, abs(v - value[x][y]))
        
        return value

    def value_iteration(self, discount=0.9, epsilon=0.01):
    
        value = [[0 for _ in range(self.size)] for _ in range(self.size)]
        policy = {}
        delta = float('inf')
        
        while delta > epsilon:
            delta = 0
            for x in range(self.size):
                for y in range(self.size):
                    state = (x, y)
                    if self.is_goal(state):
                        continue
                    v = value[x][y]
                 
                    best_action_value = float('-inf')
                    best_action = None
                    for action in self.actions(state):
                        total_value = 0
                        next_state = self.get_next_state(state, action)
                        prob = self.transition_prob(state, action, next_state)
                        reward = self.reward(state, action, next_state)
                        total_value += prob * (reward + discount * value[next_state[0]][next_state[1]])
                        if total_value > best_action_value:
                            best_action_value = total_value
                            best_action = action
                    value[x][y] = best_action_value
                    policy[state] = best_action
                    delta = max(delta, abs(v - value[x][y]))
        
        return policy, value

def find_path(grid, policy):
    state = grid.start_state()
    path = [] 
    
    while not grid.is_goal(state):
        action = policy.get(state, None) 
        if action is None:
            print("No action available from state:", state)
            return
        
        next_state = grid.get_next_state(state, action)  
        path.append((state, action))  
        state = next_state  
    
    
    path.append((state, "Goal"))  
    
    print("Path from start to goal:", path)


def input_mdp_grid():
    size = int(input("Enter the size of the grid (e.g., 4 for a 4x4 grid): "))
    grid = []
    for i in range(size):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated values for rewards): ").split()))
        grid.append(row)
    
    start_state = tuple(map(int, input("Enter the start state (e.g., '1 0' for row 1, column 0): ").split()))
    end_states = [tuple(map(int, input(f"Enter goal state {i + 1} (e.g., '1 3'): ").split())) for i in range(int(input("Enter number of goal states: ")))]
    
    slip_prob = float(input("Enter the slip probability (e.g., 0.1 for 10%): "))
    
    return MDPGrid(grid, start_state, end_states, slip_prob)


mdp_grid = input_mdp_grid()
policy, value = mdp_grid.value_iteration()


print("Value Function:")
for row in value:
    print(row)


print("\nPolicy:")
for row in range(mdp_grid.size):
    for col in range(mdp_grid.size):
        state = (row, col)
        action = policy.get(state, ' ')
        print(action, end='\t')
    print()


find_path(mdp_grid, policy)
