class MDP:
    def __init__(self, grid, start, end, slip_prob):
        self.grid = grid
        self.start = start
        self.end = end
        self.slip_prob = slip_prob
        self.states = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        self.actions_list = ['up', 'down', 'left', 'right']

    def start_state(self):
        return self.start

    def is_end(self, state):
        return state == self.end

    def discount(self):
        return 1  # No discount for this problem

    def next_state(self, state, action):
        x, y = state
        if action == 'up':
            return (x - 1, y) if x > 0 else state
        elif action == 'down':
            return (x + 1, y) if x < len(self.grid) - 1 else state
        elif action == 'left':
            return (x, y - 1) if y > 0 else state
        elif action == 'right':
            return (x, y + 1) if y < len(self.grid[0]) - 1 else state
        else:
            return state

    def actions(self, state):
        x, y = state
        actions = []
        if x > 0 and self.grid[x][y]!='X' :
            actions.append('up')
        if x < len(self.grid) - 1 and self.grid[x][y]!='X':
            actions.append('down')
        if y > 0 and self.grid[x][y]!='X':
            actions.append('left')
        if y < len(self.grid[0]) - 1 and self.grid[x][y]!='X':
            actions.append('right')
        return actions

    def transition(self, state, action, next_state):
        x, y = next_state
        if self.grid[x][y] == 'X':  # Volcano
            return self.slip_prob
        else:
            return 1 - self.slip_prob

    def reward(self, state):
        x, y = state
        if self.grid[x][y] == '20':  # Goal reward
            return 20
        elif self.grid[x][y] == 'X':  # Volcano penalty
            return -50
        else:
            return 0  # Neutral reward

    def value_iteration(self, num_iters=10):
        values = {(row, col): 0 for row in range(len(self.grid)) for col in range(len(self.grid[0]))}
        
        for _ in range(num_iters):
            new_values = values.copy()
            
            for state in self.states:
                if self.is_end(state):
                    continue
                
                action_values = []
                
                for action in self.actions(state):
                    next_state = self.next_state(state, action)
                    transition_prob = self.transition(state, action, next_state)
                    reward = self.reward(next_state)
                    
                    value = transition_prob * (reward + self.discount() * values[next_state])
                    action_values.append(value)
                
                new_values[state] = max(action_values) if action_values else 0
            
            values = new_values
        
        return values

    def best_policy(self):
        # Find the best policy based on the value function
        policy = {}
        values = self.value_iteration()

        for state in self.states:
            if self.is_end(state):
                continue

            best_action = None
            best_value = float('-inf')

            for action in self.actions(state):
                next_state = self.next_state(state, action)
                transition_prob = self.transition(state, action, next_state)
                reward = self.reward(next_state)

                value = transition_prob * (reward + self.discount() * values[next_state])

                if value > best_value:
                    best_value = value
                    best_action = action

            policy[state] = best_action

        return policy

    def print_grid(self, values, policy):
        action_symbols = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
        
        print("Grid Values and Best Actions:")
        
        # Print the grid values and actions
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                state = (row, col)
                value = round(values[state], 1)
                action = policy.get(state, ' ')
                symbol = action_symbols.get(action, ' ')
                print(f"{value} {symbol}", end="\t")
            print()
        
        # Print the path from start to end
        path = self.get_path(self.start, self.end, policy)
        print("Path from start to end:", path)

    def get_path(self, start, end, policy):
        path = []
        current_state = start

        while current_state != end:
            action = policy.get(current_state)
            if action is None:
                break  # If no action is found, exit the loop

            path.append((current_state, action))  # Append current state and action to path
            # Move to the next state based on the action
            current_state = self.next_state(current_state, action)

        return path
            
       

# Example Grid
grid = [[' ', ' ', 'X', ' ' ],
        [' ', ' ', 'X', ' '],
        [' ', ' ', '20', 'X'],
        [' ', ' ', ' ', ' ']]
       

start = (0, 0)
end = (2, 2)

# Instantiate the MDP
game = MDP(grid, start, end, 0.1)

# Run value iteration and print the value function and policy
value_function = game.value_iteration()
policy = game.best_policy()

# Print the grid with values and actions
game.print_grid(value_function, policy)
