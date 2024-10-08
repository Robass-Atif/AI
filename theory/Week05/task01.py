class MDPGrid:
    def __init__(self):
        self.grid = [
            [5, 0, 0, 0],
            [0, -50, 0, 70],
            [0, -50, 0, 0],
            [0, 0, 0, 0]
        ]
        self.size = 4 
        self.start_state_pos = (1, 0)  
        self.end_states = [(1, 3), (1, 1), (2, 1)]  

    def start_state(self):
        return self.start_state_pos

    def is_goal(self, state):
        return state in self.end_states

    def actions(self, state):
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
        negative_states = [(1, 1), (2, 1)]
        if next_state in negative_states:
            return 0
        else:
            return 1

    def reward(self, state, action, next_state):
        x, y = next_state
        return self.grid[x][y]

# Move the policy evaluation function outside the class
def policy_evaluation(mdp, policy, discount=1, epsilon=0.01):
    value = [[0 for _ in range(mdp.size)] for _ in range(mdp.size)]
    delta = float('inf')
    
    while delta > epsilon:
        delta = 0
        for x in range(mdp.size):
            for y in range(mdp.size):
                state = (x, y)
                if mdp.is_goal(state):
                    continue
                v = value[x][y]
                action = policy[state]
                total_value = 0
                next_state = mdp.get_next_state(state, action)
                prob = mdp.transition_prob(state, action, next_state)
                reward = mdp.reward(state, action, next_state)
                total_value += prob * (reward + discount * value[next_state[0]][next_state[1]])
                value[x][y] = total_value
                delta = max(delta, abs(v - value[x][y]))
    
    return value

# Move the value iteration function outside the class
def value_iteration(mdp, discount=0.9, epsilon=0.01):
    value = [[0 for _ in range(mdp.size)] for _ in range(mdp.size)]
    policy = {}
    delta = float('inf')
    
    while delta > epsilon:
        delta = 0
        for x in range(mdp.size):
            for y in range(mdp.size):
                state = (x, y)
                if mdp.is_goal(state):
                    continue
                v = value[x][y]
                
                best_action_value = float('-inf')
                best_action = None
                for action in mdp.actions(state):
                    total_value = 0
                    next_state = mdp.get_next_state(state, action)
                    prob = mdp.transition_prob(state, action, next_state)
                    reward = mdp.reward(state, action, next_state)
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

# Instantiate the MDPGrid
mdp_grid = MDPGrid()

# Perform value iteration using the external function
policy, value = value_iteration(mdp_grid)

# Print the value function
print("Value Function:")
for row in value:
    print(row)

# Print the policy
print("\nPolicy:")
for row in range(mdp_grid.size):
    for col in range(mdp_grid.size):
        state = (row, col)
        action = policy.get(state, ' ')
        print(action, end='\t')
    print()

# Find the path using the computed policy

